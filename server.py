import os
import asyncio
import requests
from mcp.server import Server
from mcp.types import Tool, TextContent
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

FIGMA_TOKEN = os.getenv("FIGMA_TOKEN")
FIGMA_FILE_ID = os.getenv("FIGMA_FILE_ID")

# Create the MCP server
server = Server("figma-text-extractor")

def get_figma_file():
    """Fetch the Figma file via API"""
    url = f"https://api.figma.com/v1/files/{FIGMA_FILE_ID}"
    headers = {"X-Figma-Token": FIGMA_TOKEN}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return {"error": f"Figma API Error: {response.status_code}"}
    
    return response.json()

def extract_text_from_node(node, depth=0):
    """Extract text from a Figma node recursively"""
    result = []
    
    # If it's a text node, extract the text
    if node.get("type") == "TEXT" and node.get("characters"):
        indent = "  " * depth
        name = node.get("name", "Unnamed")
        text = node.get("characters", "")
        result.append(f"{indent}[{name}]: {text}")
    
    # Traverse children nodes
    if "children" in node:
        for child in node["children"]:
            result.extend(extract_text_from_node(child, depth + 1))
    
    return result

def extract_sections_content():
    """Extract text content from ALL frames/sections in the Figma file"""
    figma_data = get_figma_file()
    
    if "error" in figma_data:
        return figma_data
    
    sections = {}
    
    # Navigate through the Figma document structure
    document = figma_data.get("document", {})
    
    # Search through pages
    for page in document.get("children", []):
        if page.get("type") == "CANVAS":
            # Find all top-level elements (frames, groups, etc.)
            for i, element in enumerate(page.get("children", [])):
                element_type = element.get("type", "")
                element_name = element.get("name", f"Element {i}")
                
                # Capture all container types (Frames, Groups, Components, Sections)
                if element_type in ["FRAME", "GROUP", "COMPONENT", "SECTION"]:
                    section_key = f"section_{i+1}"
                    
                    sections[section_key] = {
                        "name": element_name,
                        "type": element_type,
                        "content": extract_text_from_node(element)
                    }
    
    return sections

# Declare the tools available to Claude
@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="get_figma_content",
            description="Extract all text content from ALL frames/sections of the Figma file",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="get_section",
            description="Extract content from a specific section by number (section_1, section_2, etc.)",
            inputSchema={
                "type": "object",
                "properties": {
                    "section": {
                        "type": "string",
                        "description": "The section to extract (e.g., section_1, section_2, section_7)"
                    }
                },
                "required": ["section"]
            }
        )
    ]

# Implement what happens when Claude calls the tools
@server.call_tool()
async def call_tool(name: str, arguments: dict):
    if name == "get_figma_content":
        # Extract all content from the Figma file
        sections = extract_sections_content()
        
        if "error" in sections:
            return [TextContent(
                type="text",
                text=f"Error: {sections['error']}"
            )]
        
        # Format the response nicely
        result = f"# Figma File Content ({len(sections)} sections found)\n\n"
        
        for section_key, section_data in sections.items():
            result += f"## {section_data['name']}\n\n"
            result += "\n".join(section_data['content'])
            result += "\n\n---\n\n"
        
        return [TextContent(type="text", text=result)]
    
    elif name == "get_section":
        # Extract a specific section
        section_key = arguments.get("section")
        sections = extract_sections_content()
        
        if "error" in sections:
            return [TextContent(
                type="text",
                text=f"Error: {sections['error']}"
            )]
        
        if section_key not in sections:
            available = ", ".join(sections.keys())
            return [TextContent(
                type="text",
                text=f"Section {section_key} not found. Available sections: {available}"
            )]
        
        section_data = sections[section_key]
        result = f"# {section_data['name']}\n\n"
        result += "\n".join(section_data['content'])
        
        return [TextContent(type="text", text=result)]
    
    return [TextContent(type="text", text="Tool not recognized")]

# Start the MCP server
async def main():
    from mcp.server.stdio import stdio_server
    
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )

if __name__ == "__main__":
    asyncio.run(main())
