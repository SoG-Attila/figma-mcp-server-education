# Teaching Guide: Figma MCP Server Workshop
### For Educators Teaching AI Automation

This guide provides detailed lesson plans, teaching tips, and troubleshooting strategies for successfully running the Figma MCP Server workshop with business students.

---

## 📋 Workshop Overview

**Target Audience:** MBA/Business students with no coding background  
**Duration:** 6 hours (1 full day)  
**Class Size:** 15-30 students (ideal)  
**Language:** English (materials), adaptable to other languages  
**Success Rate:** 80%+ students have working server by end of day

---

## 🎯 Learning Objectives

By the end of this workshop, students should be able to:

1. **Conceptual Understanding:**
   - Explain what an API is and how it works
   - Understand the Model Context Protocol (MCP)
   - Identify automation opportunities in business workflows

2. **Technical Skills:**
   - Install Python and manage packages
   - Set up development environments
   - Configure API tokens and credentials
   - Read and modify simple configuration files

3. **Practical Application:**
   - Connect Figma to Claude AI automatically
   - Generate marketing content using AI + structured data
   - Troubleshoot common technical issues
   - Think programmatically about business problems

---

## 📅 Detailed Schedule (6 Hours)

### Part 1: Setup (3 hours)

#### 09:00-09:30 | Theory & Context (30 min)
**Topics to cover:**
- What is an API? (Use real-world analogies)
- Introduction to Model Context Protocol
- Why connect tools together?
- Use cases: Marketing automation, content generation
- Overview of what students will build

**Teaching Tips:**
- Use restaurant/waiter analogy for APIs
- Show live demo of final result first (motivation!)
- Emphasize: "You don't need to be a programmer"
- Show examples of content generated from Figma

**Slides to prepare:**
1. API concept with visuals
2. MCP architecture diagram
3. Figma → MCP → Claude flow
4. Example outputs (calendars, emails, etc.)

---

#### 09:30-11:15 | Workshop Part 1 (1h45)
**Focus:** Python installation and project setup

**Step-by-step:**
1. **Python Installation (20 min)**
   - Windows: Microsoft Store method
   - Mac: Homebrew or download
   - Verification: `python --version`

2. **Project Setup (30 min)**
   - Create folder structure
   - Virtual environment creation
   - Activate venv
   - Install dependencies

3. **Figma Token & File ID (20 min)**
   - Create Figma account (if needed)
   - Generate personal access token
   - Find file ID from URL
   - Create `.env` file

4. **Create Server Files (35 min)**
   - Copy `.env.example` → `.env`
   - Copy `server.py` (or type it)
   - Test server runs without errors

**Common Issues:**
- ⚠️ Windows: Execution policy blocks venv activation
  - Solution: `Set-ExecutionPolicy RemoteSigned` (admin)
- ⚠️ Mac: Python vs Python3 confusion
  - Solution: Use `python3` explicitly
- ⚠️ Forgot to activate venv before pip install
  - Solution: Reactivate and reinstall

**Teaching Assistant Tasks:**
- Circulate to help with Python installation
- Check everyone's venv is activated (look for `(venv)`)
- Verify tokens are correct format (start with `figd_`)

---

#### 11:15-11:30 | Break (15 min)

**Use this time to:**
- Check progress on Slack/chat
- Identify students who need extra help
- Prepare for Claude Desktop setup

---

#### 11:30-13:00 | Workshop Part 2 (1h30)
**Focus:** Claude Desktop configuration and testing

**Step-by-step:**
1. **Install Claude Desktop (15 min)**
   - Download from claude.ai
   - Install and sign in
   - Quick tour of interface

2. **Find Python Path (10 min)**
   - Windows: `where.exe python`
   - Mac: `which python3`
   - Note the venv path!

3. **Configure Claude Desktop (30 min)**
   - Locate config file
   - Edit JSON configuration
   - Replace paths with student's paths
   - Common JSON errors

4. **Testing & Validation (30 min)**
   - Restart Claude Desktop
   - Check MCP server status (Settings → Developer)
   - First prompt: "What MCP tools do you have?"
   - Extract content from Figma

5. **Celebration! (5 min)**
   - Acknowledge success
   - Screenshot of working setup
   - Quick show-and-tell

**Common Issues:**
- ⚠️ Config file doesn't exist
  - Solution: Create manually
- ⚠️ Windows paths with single backslash
  - Solution: Use `\\` double backslashes
- ⚠️ Wrong Python path (system vs venv)
  - Solution: Must be venv path!
- ⚠️ Typos in JSON (missing comma, quote)
  - Solution: Use JSON validator online

**Success Indicators:**
- ✅ Green "running" status in Claude
- ✅ Claude lists "figma-text-extractor" tool
- ✅ Can extract content from Figma file

---

### Part 2: Content Strategy (3 hours)

#### 13:00-14:00 | Lunch Break

**Optional:**
- Keep lab open for students who want extra help
- Office hours for stragglers

---

#### 14:00-15:30 | Content Strategy Workshop (1h30)
**Focus:** Using the tool to generate marketing content

**Structure:**
1. **Demo Session (20 min)**
   - Show 5-6 powerful prompts live
   - Generate content calendar
   - Create email sequence
   - Write social media posts
   - Demonstrate prompt refinement

2. **Prompt Engineering Mini-Lesson (15 min)**
   - Anatomy of a good prompt
   - Be specific vs vague
   - Provide context
   - Define output format
   - Iterative refinement

3. **Group Exercise (30 min)**
   - In pairs: Create content for fictional brand
   - Use provided Figma template
   - Generate 3 different deliverables
   - Share results with class

4. **Discussion (25 min)**
   - What worked well?
   - What was challenging?
   - Business applications
   - Other tools to connect

**Example Prompts to Demonstrate:**
```
1. "Extract all content from my Figma file"

2. "Based on the persona in section_1, create a 2-week 
   Instagram content calendar with captions and hashtags"

3. "Using the customer journey, write a 3-email welcome 
   sequence with subject lines"

4. "Analyze the messaging framework and suggest improvements 
   for clarity and emotional impact"

5. "Create a creative brief for a designer based on the 
   content strategy in section_3"
```

---

#### 15:30-15:45 | Break (15 min)

---

#### 15:45-16:45 | Practical Exercises (1h)
**Focus:** Students work independently, you provide support

**Exercise Options:**

**Option A: Marketing Campaign**
- Choose a real or fictional product
- Fill in Figma template with strategy
- Generate:
  - 2-week content calendar
  - Email sequence (3 emails)
  - Social media posts (5 posts)
  - Landing page copy

**Option B: Personal Brand**
- Define personal positioning
- Create content strategy in Figma
- Generate:
  - LinkedIn posts (5)
  - Newsletter content plan
  - About page copy
  - Portfolio case study structure

**Option C: Business Use Case**
- Students bring their own business challenge
- Structure in Figma
- Use Claude to generate solutions

**Deliverable:**
- Save all generated content
- Document prompts used
- Note what worked/didn't work

---

#### 16:45-17:00 | Wrap-Up & Assignment (15 min)

**Recap:**
- What we built today
- Key concepts learned
- Real-world applications

**Assignment:**
Present the homework (see below)

**Next Steps:**
- Office hours schedule
- Forum/Slack for questions
- Resources for going further

**Survey:**
- Quick feedback form
- What went well
- What to improve
- Confidence level (1-10)

---

## 📝 Homework Assignment

**Due:** 1 week after workshop

**Part 1: Deliverables (70% of grade)**
Using your Figma MCP server, generate:
1. 2-week editorial calendar for a brand
2. 3 LinkedIn posts on a professional topic
3. Email welcome sequence (3 emails)
4. 1-page content strategy document
5. Creative brief for a design project

**Requirements:**
- Save all outputs (PDF or docs)
- Include the prompts you used
- Show iteration (version 1 vs refined version)

**Part 2: Reflection Essay (30% of grade)**
Write 500-750 words addressing:
1. What automation opportunities do you see in your future career?
2. What other tools would you like to connect to AI?
3. How has your understanding of AI changed?
4. What was most challenging? Most exciting?

**Bonus:**
- Connect a different tool using MCP
- Create a video tutorial for classmates
- Share template on GitHub

---

## 🎓 Pedagogical Strategies

### For Non-Technical Students

**Do:**
- ✅ Use analogies (restaurant, post office, translator)
- ✅ Celebrate small wins loudly
- ✅ Normalize errors ("errors are feedback")
- ✅ Pair technical with non-technical students
- ✅ Show business value constantly

**Don't:**
- ❌ Assume prior knowledge
- ❌ Use technical jargon without explaining
- ❌ Rush through installation steps
- ❌ Make students feel "stupid" for asking
- ❌ Skip the "why" to jump to "how"

### Building Confidence

**Techniques:**
1. **Show before tell:** Demo the end result first
2. **Normalize struggle:** "Everyone has this issue"
3. **Peer support:** Pair programming reduces anxiety
4. **Quick wins:** First successful test = celebration
5. **Reframe errors:** "Errors mean you're learning"

### Engagement Tactics

1. **Real examples:** Use brands students know
2. **Personal relevance:** "How would YOU use this?"
3. **Competition:** "First to generate 5 posts wins ___"
4. **Show-and-tell:** Students demo their work
5. **Humor:** Keep it light, laugh at tech quirks

---

## 🆘 Troubleshooting Guide

### Pre-Workshop

**Issue:** Students don't have admin rights
- **Prevention:** Send requirements 1 week in advance
- **Solution:** IT department pre-installs Python
- **Backup:** Use cloud Python environment (Replit, Colab)

**Issue:** Mixed Mac and Windows
- **Preparation:** Test tutorial on both OS
- **Solution:** Have OS-specific TAs
- **Tip:** Create quick reference cards for each OS

### During Workshop

**Issue:** Student falls behind
- **Strategy:** Pair with student who's ahead
- **Strategy:** TA provides 1-on-1 catch-up
- **Strategy:** Skip to pre-configured version

**Issue:** API errors (403, 401)
- **Cause:** Invalid Figma token
- **Solution:** Generate new token
- **Prevention:** Have students test tokens early

**Issue:** Config file errors
- **Cause:** JSON syntax errors, wrong paths
- **Solution:** Use JSON validator
- **Prevention:** Provide working templates to copy

**Issue:** Virtual environment issues
- **Cause:** Not activated, wrong Python
- **Solution:** Restart from venv creation
- **Prevention:** Visual check (see `(venv)`)

### Post-Workshop

**Issue:** Server stops working after reboot
- **Cause:** Paths changed, token expired
- **Solution:** Verify paths, regenerate token
- **Office hours:** Dedicated session for fixes

**Issue:** Student wants to extend project
- **Encourage:** Share extension ideas
- **Resources:** Point to MCP docs
- **Bonus:** Offer extra credit

---

## 📊 Assessment Rubrics

### Workshop Participation (Pass/Fail)
- Attended full workshop
- Completed setup steps
- Server working by end of day (or arranged makeup)

### Assignment Grading

**Deliverables (70 points):**
- All 5 deliverables submitted: 40 pts
- Quality of outputs: 15 pts
- Variety of prompts used: 10 pts
- Evidence of iteration: 5 pts

**Reflection Essay (30 points):**
- Thoughtful analysis: 15 pts
- Specific examples: 10 pts
- Writing quality: 5 pts

**Total: 100 points**

**Bonus (up to 10 points):**
- Extended functionality
- Tutorial created
- Template shared

---

## 🎯 Success Metrics

### During Workshop
- **80%+** students have server running by end
- **90%+** understand MCP concept
- **70%+** succeed at first extraction
- **5+** questions asked per student (engagement)

### Post-Workshop
- **100%** have working server (with office hours help)
- **3+** deliverables per student on average
- **8/10** satisfaction score
- **90%+** would recommend to peers

### Long-Term
- Students use tool in other courses
- Students add to portfolio/resume
- Students teach others
- Alumni mention it in job interviews

---

## 💡 Advanced Topics (Optional)

### For Quick Learners

**Extension Projects:**
1. Add image extraction from Figma
2. Support multiple Figma files
3. Add caching to reduce API calls
4. Create web interface for non-technical users
5. Connect other tools (Notion, Airtable, etc.)

**Resources:**
- MCP documentation
- Figma API docs
- Python advanced tutorials

### Guest Speakers

**Invite:**
- Engineers who build AI integrations
- Marketing automation experts
- Product managers using no-code tools
- Startup founders using AI

---

## 🔄 Iteration & Improvement

### After Each Workshop

**Collect:**
- Student feedback (survey)
- TA observations
- Technical issues log
- Time spent on each section

**Analyze:**
- Which steps took longest?
- Where did most errors occur?
- What confused students most?
- What worked really well?

**Improve:**
- Update tutorial screenshots
- Add more examples
- Clarify confusing sections
- Pre-configure more options

### Version History

**Track:**
- Tutorial versions
- Code changes
- Platform updates (Mac, Windows, Claude)
- New features added

---

## 📚 Resources for Teachers

### Pre-Workshop Prep

**Technical:**
- Test on Windows and Mac
- Have backup computers ready
- Prepare USB drives with installers
- Screenshot every step yourself

**Materials:**
- Print quick reference guides
- Prepare Figma template
- Create example prompts list
- Set up course forum/Slack

### During Workshop

**Equipment:**
- Projector for live demo
- Secondary screen for code
- Microphone for large rooms
- TAs with laptops to help

**Digital:**
- Shared Google Doc for questions
- Slack channel for quick help
- Screen sharing for debugging
- Backup files on USB

### Post-Workshop

**Follow-up:**
- Office hours (2-3 sessions)
- Email with resources
- Forum for peer help
- Showcase of best work

---

## 🤝 Working with Teaching Assistants

### TA Briefing (Before Workshop)

**Preparation:**
- TAs complete tutorial themselves
- Review common issues
- Assign sections (Mac vs Windows)
- Set up communication channel

**Responsibilities:**
- Circulate during setup
- Help with technical issues
- Document new problems
- Encourage struggling students

**Communication:**
- Slack channel for quick coordination
- Signal when section complete
- Flag students needing extra help
- Share solutions to new issues

### TA Ratio

**Ideal:** 1 TA per 15 students
**Minimum:** 1 TA per 25 students
**Large class:** 2 TAs + professor

---

## 📞 Support Resources

### For Teachers

**Community:**
- GitHub Discussions
- Share experiences with other educators
- Contribute improvements

**Technical:**
- MCP documentation
- Anthropic support
- Figma developer docs

### For Students

**During course:**
- Office hours
- TA support
- Peer study groups
- Course forum

**After course:**
- Tutorial documentation
- Example prompts
- Troubleshooting guide
- Alumni network

---

## 🎓 Integration with Curriculum

### Standalone Workshop
- One-day technical skills session
- Certificate of completion
- Portfolio piece

### Part of Marketing Course
- Module on AI automation
- Builds to campaign project
- Recurring tool in assignments

### Part of Tech for Business Course
- API integration module
- Followed by other integrations
- Final project: Build your own

---

## 📄 Additional Materials

**Download from repository:**
- Student tutorial (HTML)
- Example prompts (MD)
- Server code (PY)
- Configuration templates
- Troubleshooting guide

**Create for your class:**
- Figma template (your domain)
- Assignment rubric (your grading)
- Pre-class checklist
- Post-class survey

---

## 🌟 Teaching Philosophy

**Core Principles:**
1. **Learn by doing:** Hands-on from minute one
2. **No shame:** All questions are good questions
3. **Business first:** Why before how
4. **Celebrate wins:** Every success matters
5. **Support network:** Peers help peers

**Remember:**
- Your enthusiasm is contagious
- Errors are learning opportunities
- Business students CAN do technical work
- The goal is empowerment, not perfection

---

## 📝 Feedback & Contributions

**Improve these materials:**
- Open issues on GitHub
- Submit pull requests
- Share teaching stories
- Suggest new examples

**Connect with author:**
- GitHub: @SoG-Attila
- Share your success stories
- Collaborate on improvements

---

**Good luck with your workshop!** 🎓

Your students are about to discover they can build real AI integrations. The confidence this gives them is transformative.

*Teaching AI should be accessible, practical, and empowering.*

---

**Created by:** Axel TASCIYAN  
**For:** Educators teaching AI automation to business students  
**License:** Educational use only (non-commercial)
