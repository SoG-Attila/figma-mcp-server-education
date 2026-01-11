# Figma MCP Server for Claude AI
### Educational Material for Teaching AI Automation

Connect Figma designs to Claude AI and teach students about AI automation, APIs, and the Model Context Protocol (MCP).

![MCP](https://img.shields.io/badge/MCP-Enabled-blue)
![Python](https://img.shields.io/badge/Python-3.12%2B-green)
![License](https://img.shields.io/badge/License-Educational-orange)

---

## 📚 About This Educational Material

**Created by:** Prof. Axel TASCIYAN  
**Institutions:** HEC Paris MBA & EMLYON Business School  
**Purpose:** Teaching AI automation and MCP integration to business students  
**Level:** No coding experience required

This repository contains complete teaching materials for a hands-on workshop where students learn to:
- Connect external data sources (Figma) to AI tools (Claude)
- Understand APIs and the Model Context Protocol
- Automate content generation workflows
- Build practical AI integrations

---

## ⚠️ LICENSE NOTICE

**This is educational material for non-commercial teaching use.**

- ✅ **Permitted:** Use in educational courses and workshops
- ✅ **Permitted:** Adaptation for your teaching needs
- ✅ **Permitted:** Sharing with other educators
- ❌ **Not permitted:** Commercial use or sale
- 📧 **Commercial licensing:** Contact via GitHub

See [LICENSE](LICENSE) file for full terms.

---

## 🎯 What This Teaches

### Learning Objectives
Students will be able to:
- ✅ Understand how APIs connect different software tools
- ✅ Grasp the concept of Model Context Protocol (MCP)
- ✅ Set up a Python development environment
- ✅ Connect external data sources to AI tools
- ✅ Automate content extraction and generation workflows
- ✅ Troubleshoot common technical issues

### Practical Applications
After completing this workshop, students can automate:
- 📅 Content calendar generation from marketing personas
- ✉️ Email campaigns from strategic frameworks
- 🌐 Website copy from Figma wireframes
- 📊 Content strategy analysis and optimization
- 🚀 Any workflow that starts with structured Figma content

---

## 👩‍🏫 For Teachers

### Workshop Format
- **Duration:** 6 hours (1 day workshop)
- **Target Audience:** Business students with no coding background
- **Class Size:** Works well with 15-30 students
- **Prerequisites:** Computers with admin rights, Figma and Claude accounts

### Teaching Materials Included
1. **Student Tutorial** (`docs/student-tutorial-figma-mcp.html`) - 90-minute step-by-step guide
2. **Teaching Guide** (`TEACHING-GUIDE.md`) - Lesson plan, tips, common issues
3. **Example Prompts** (`examples/prompts.md`) - 30+ ready-to-use Claude prompts
4. **Server Code** (`server.py`) - Well-commented for learning
5. **Configuration Templates** (`.env.example`, config examples)

### Recommended Schedule
```
09:00-09:30  Theory (MCP, APIs, use cases)
09:30-11:15  Workshop Part 1 (Install Python, create project)
11:15-11:30  Break
11:30-13:00  Workshop Part 2 (Claude Desktop setup, testing)
13:00-14:00  Lunch
14:00-15:30  Content strategy workshop (examples & demos)
15:30-15:45  Break
15:45-16:45  Practical exercises
16:45-17:00  Q&A & homework assignment
```

### Tips for Success
- Pair technical and non-technical students
- Have TAs ready to help (1 TA per 15 students ideal)
- Test all setups on both Windows and Mac beforehand
- Celebrate small wins to build student confidence
- Emphasize that coding knowledge is NOT required

See **[TEACHING-GUIDE.md](TEACHING-GUIDE.md)** for detailed instructor notes.

---

## 🎓 For Students

### Quick Start
1. **Download this repository** (Code → Download ZIP)
2. **Open the tutorial:** `docs/student-tutorial-figma-mcp.html` in your browser
3. **Follow every step** (~90 minutes)
4. **Start creating!** Use Claude to generate content from your Figma files

### Prerequisites
- Computer: Windows 10/11 or macOS 10.15+
- Administrator access to install software
- [Figma account](https://figma.com) (free)
- [Claude account](https://claude.ai) (free)

### What You'll Build
By the end of this tutorial, you will have:
- ✅ A working MCP server running on your computer
- ✅ Claude Desktop connected to your Figma files
- ✅ The ability to automate content generation
- ✅ Understanding of AI automation workflows

---

## 📁 Repository Structure

```
figma-mcp-server/
├── README.md                    ← You are here
├── LICENSE                      ← Educational use license
├── TEACHING-GUIDE.md            ← For instructors
├── server.py                    ← MCP server code
├── .env.example                 ← Configuration template
├── requirements.txt             ← Python dependencies
├── .gitignore                   ← Git ignore rules
│
├── docs/
│   └── student-tutorial-figma-mcp.html  ← Main tutorial
│
├── examples/
│   └── prompts.md               ← Example Claude prompts
│
└── CONTRIBUTING.md              ← Guide for educators
```

---

## 🛠️ Technical Stack

**For Educators (You don't need to be an expert in these):**
- **Python 3.12+** - Programming language (students install via Microsoft Store/Homebrew)
- **MCP (Model Context Protocol)** - Anthropic's standard for AI tool integration
- **Figma API** - For reading design file content
- **Claude Desktop** - AI interface with MCP support

**Python Libraries:**
- `mcp` - Model Context Protocol SDK
- `requests` - HTTP library for API calls
- `python-dotenv` - Environment variable management

---

## 🚀 Getting Started (For Teachers)

### 1. Review the Materials
- Read `TEACHING-GUIDE.md` for lesson plan and tips
- Open `docs/student-tutorial-figma-mcp.html` to see student experience
- Review `server.py` to understand what students build

### 2. Prepare Your Setup
- Test the tutorial on both Windows and Mac if possible
- Create your own Figma template file for students to duplicate
- Set up your own MCP server to demonstrate live
- Prepare examples of content generation prompts

### 3. Customize for Your Course
- Adapt the Figma template to your course focus
- Modify example prompts for your industry/domain
- Adjust workshop timing to fit your schedule
- Add assignments relevant to your curriculum

### 4. Share with Students
- Fork this repository or download ZIP
- Share the repository link with students before class
- Ensure students have created Figma and Claude accounts
- Send pre-class checklist for computer requirements

---

## 📖 How to Use in Your Course

### Option 1: Standalone Workshop
Use this as a one-day technical skills workshop teaching AI automation.

### Option 2: Part of Larger Course
Integrate into digital marketing, content strategy, or AI for business courses.

### Option 3: Self-Paced Learning
Share materials for students to complete independently with office hours support.

---

## 💡 Example Prompts for Students

Once the server is running, students can try:

**Extract content:**
```
Show me all the content from my Figma file
```

**Generate content calendar:**
```
Based on the persona in section_1 of my Figma file, 
create a 2-week content calendar for Instagram
```

**Create email sequence:**
```
Using the customer journey in my Figma file, 
write a 3-email welcome sequence
```

More examples in [`examples/prompts.md`](examples/prompts.md)

---

## 🆘 Common Student Issues & Solutions

### "Could not connect to MCP server"
- Check paths in config file (no typos)
- Windows: Use double backslashes `\\`
- Restart Claude Desktop completely

### "Figma API Error: 403"
- Token is invalid/expired → Create new token
- Update `.env` file with new token

### "ModuleNotFoundError"
```bash
# Activate venv and reinstall
source venv/bin/activate  # or .\venv\Scripts\Activate on Windows
pip install mcp requests python-dotenv
```

See tutorial for complete troubleshooting guide.

---

## 🌟 Student Success Stories

**What students have built:**
- Automated social media calendars for startups
- Email campaign generators for personal brands
- Content strategy tools for internships
- Portfolio projects showcasing AI skills

---

## 📝 Assignments & Assessment

### Example Assignment
**Generate 5 deliverables from your Figma content:**
- [ ] 2-week editorial calendar
- [ ] 3 social media posts
- [ ] Email sequence (3 emails)
- [ ] 1-page content strategy
- [ ] Creative brief for designer

**Written reflection (500 words):**
- What automation opportunities do you see for your career?
- What other tools would you like to connect to AI?
- What did you learn about AI and marketing automation?

---

## 🔄 Extending the Project

### For Advanced Students
- Extract image metadata from Figma
- Support multiple Figma files
- Add caching to reduce API calls
- Export to different formats (JSON, CSV, Markdown)

### Connect Other Tools
Apply the same pattern to:
- Notion databases
- Google Sheets
- Airtable bases
- GitHub repositories

---

## 🤝 Contributing (For Educators)

Want to improve these materials? See [CONTRIBUTING.md](CONTRIBUTING.md)

**Ways to contribute:**
- Share teaching tips and tricks
- Report issues in the tutorial
- Suggest improvements to code examples
- Add new use cases and prompts
- Translate materials to other languages

---

## 📚 Additional Resources

**For Students:**
- [MCP Documentation](https://modelcontextprotocol.io)
- [Figma API Docs](https://www.figma.com/developers/api)
- [Claude API Docs](https://docs.anthropic.com)
- [Python Tutorial](https://www.python.org/about/gettingstarted/)

**For Teachers:**
- [Anthropic Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Teaching AI Tools](https://www.anthropic.com/education)

---

## 📄 License

**Educational Use License** - Free for teaching purposes, non-commercial use only.

See [LICENSE](LICENSE) file for full terms.

For commercial licensing: Contact via GitHub (@SoG-Attila)

---

## 👥 Credits

**Created by:** Axel TASCIYAN  
**Teaching at:** HEC Paris MBA & EMLYON Business School  
**Year:** 2026

**Built with:**
- [MCP Protocol](https://modelcontextprotocol.io) by Anthropic
- [Figma API](https://www.figma.com/developers/api)
- [Claude AI](https://claude.ai)

---

## 📞 Support

**For Teachers:**
- Open an issue on GitHub
- Share experiences in Discussions
- Connect with other educators using this material

**For Students:**
- Follow the tutorial troubleshooting section
- Ask your instructor or teaching assistant
- Check the examples folder for guidance

---

## 🎓 About the Creator

Axel TASCIYAN teaches Digital Marketing and AI Automation at leading business schools. This material was developed to help business students understand and leverage AI tools practically, without requiring technical backgrounds.

**Philosophy:** Learn by doing, immediate practical application, business-focused outcomes.

---

**For Educational Use Only** 🎓

*Making AI accessible to business students worldwide*

*Last updated: January 2026*
