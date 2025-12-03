<img width="1024" height="1024" alt="AI" src="https://github.com/user-attachments/assets/e7655d37-bc6f-4337-9297-39ff2b4b3602" />

<img width="1916" height="1080" alt="page0" src="https://github.com/user-attachments/assets/40826b1a-487c-466a-b515-84a7d916f62e" />

Our App:-- https://blockbuster-movie-appuction-ai-agent.streamlit.app/



https://github.com/user-attachments/assets/ca3a284b-4b4f-43eb-8de3-fff4ea098274


https://github.com/user-attachments/assets/93912371-933c-460f-a7c9-3c3ed21f1700




---


# 🎬 Blockbuster Movie Production AI Agent

### From Idea to Blockbuster — Create with AI  
*Lights, Camera, AI Action — Your Movie Journey Starts Here!*

---

## 🚀 Project Overview

The **Blockbuster Movie Production Agent 🎬** is a cutting-edge **Streamlit-based AI web application** that empowers creatives, writers, producers, and film enthusiasts to ideate, plan, and simulate the full production lifecycle of a blockbuster movie.

Harnessing the power of **OpenAI GPT** and **SerpAPI**, this app enables users to take an idea from inception to cinematic simulation — all in a visually stunning, interactive environment.

---

## 🎯 Purpose

To provide an AI-powered end-to-end assistant for planning blockbuster movies — including character creation, script structure, casting, budgeting, marketing, and more — using real-world data and intelligent workflows.

---

## ✨ Key Features

### 🎨 UI & Branding
- **Neon glassmorphism** style with animations
- Dynamic sidebar with **developer info**, **branding**, and **progress tracker**
- Animated logos, sparkles, and a polished cinematic theme

### 🔐 API Key Management
- Uses **Streamlit Cloud secrets** to handle `OpenAI` and `SerpAPI` keys securely
- No `.env` file required for deployment

---

## 📝 Workflow Steps

### 🟢 Step 1: Movie Name & Genre
- Enter a custom movie name or use AI suggestions
- Select genre(s) with a **"Surprise Me"** genre mashup option
- Define **target audience** and **estimated runtime**

### 🧑‍🎭 Step 2: Character Builder
- Choose **3–5 main characters**
- For each: AI-suggested name, traits, backgrounds, or full randomization
- Option to manually edit or fine-tune each character

### 💰 Step 3: Budget & Production
- Set an **estimated budget**, **shooting location**, and **timeline**
- Interactive inputs for realistic production planning

---

## 🤖 AI-Powered Production Pipeline

- **Script Outline Generator**  
  Structured 3-act plot with twists and climaxes  
- **Virtual Casting Call**  
  Suggests actors (based on SerpAPI), bios, and audition lines  
- **Production Plan**  
  AI-generated logistics, timeline, and cost-saving ideas  
- **Risk Analysis**  
  AI-generated risk management plan  
- **Movie Concept Summary**  
  High-level summary for pitching or sharing  

---

## 🔧 Advanced AI Tools

- 🎥 **Trailer Script Generator**  
  Dramatic voice-over, hooks, and taglines

- 🌍 **Global Release Planner**  
  Strategic release windows, target markets, and distribution plans

- 📢 **Audience Feedback Simulation**  
  Emulates social media and viewer response post-release

- 🎵 **Soundtrack & Composer Suggestions**  
  Recommends styles, musicians, and royalty-free tracks

- 📜 **Legal & Copyright Checklist**  
  Covers rights, credits, trademarks, and legal docs

- 💼 **Festival & Awards Strategy**  
  Lists suitable festivals, awards, deadlines, and campaign strategies

- 📈 **Budget Breakdown & ROI Estimator**  
  Predicts ROI, revenue streams, and investment returns

- 🤝 **Real-Time Collaboration Demo**  
  Prototype for shared workspace between creative teams

- 🌟 **Talent Discovery & Social Media Insights**  
  Suggests emerging talent with social reach and casting relevance

---

## 📊 Progress Tracking

- Sidebar **progress bar** updates interactively as users move through each production step

---

## 🧰 Technologies Used

| Tool | Purpose |
|------|---------|
| 🧠 OpenAI GPT | Natural language generation |
| 🔍 SerpAPI | Real-world casting, talent, location, and film info |
| 🧪 Streamlit | UI framework for interactive apps |
| 🐍 Python | Core app logic, randomization, session management |
| 🎨 Custom CSS/HTML | Advanced visual UI, glassmorphism, animation |

---

## 📦 Project Structure

```

📁 blockbuster-movie-production-ai-agent/
│
├── app.py                  # Main Streamlit app logic
├── components/             # Custom component UIs (character builder, planner)
├── assets/                 # Logos, animated SVGs, and styles
├── utils/                  # Helper functions (API calls, genre data, randomizer)
├── .streamlit/secrets.toml # Streamlit Cloud API keys
├── requirements.txt        # Python dependencies
└── README.md               # Project overview and documentation

````


````markdown
# 🧠 AI Workflow Architecture & Logic | Blockbuster Movie Production Agent 🎬

This section provides a deep dive into the internal **architecture**, **LangGraph-based decision logic**, and **AI workflow** that powers the Blockbuster Movie Production AI Agent.

---

## 🏗️ Overall Architecture

```text
                ┌─────────────────────────────┐
                │      Streamlit Frontend     │◄────────────┐
                └─────────────────────────────┘             │
                          │                                 │
                          ▼                                 │
              ┌─────────────────────────────┐              │
              │   User Input Interface      │              │
              └─────────────────────────────┘              │
                          │                                 │
                          ▼                                 │
              ┌─────────────────────────────┐              │
              │    LangGraph Decision Tree  │ ─────────────┘
              └─────────────────────────────┘
                          │
          ┌───────────────┼─────────────────────────────┐
          ▼               ▼                             ▼
┌────────────────┐ ┌────────────────────┐     ┌────────────────────┐
│ GPT Function A │ │ SerpAPI Integration│     │    Custom Logic    │
│ (Ideation)     │ │ (Casting & Talent) │     │ (Cost, Risks, etc) │
└────────────────┘ └────────────────────┘     └────────────────────┘
          ▼               ▼                             ▼
          └───────────────┴───────────────┬─────────────┘
                                          ▼
                             ┌──────────────────────────┐
                             │ Output to Streamlit UI   │
                             └──────────────────────────┘
````

---

## 🔁 Workflow Breakdown (LangGraph-style)

The app's backend decision flow is modeled using a **LangGraph**-like agent system, where each step depends on previous user input and AI output.

### 🛠️ Step-by-Step Flow:

#### 1. **Start: Home Screen**

* Prompt: Welcome screen with logo, theme, and user input
* Decision: Proceed to step 1 or load previous session

#### 2. **Step 1 – Movie Name & Genre**

* User can:

  * Type movie name
  * Use AI to generate one
  * Choose genre or “Surprise Me”
  * Set target audience, runtime
* **LangGraph Decision**:

  * If genre = "Mixed" → Activate dual-tone genre pipeline
  * If name = blank → Use GPT to generate thematic name

#### 3. **Step 2 – Character Builder**

* Choose 3–5 characters
* For each:

  * Name, traits, backstory (via GPT)
  * Optional: User manual override
* **LangGraph Checkpoints**:

  * Loop back if less than 3 characters defined
  * If user clicks "Randomize All" → bulk generate via GPT batch call

#### 4. **Step 3 – Budget & Production Planner**

* Enter budget, shooting location, timeline
* GPT generates:

  * Script outline
  * Production schedule
  * Budget advice
* **LangGraph Decision**:

  * If budget < \$500K → Suggest indie strategies
  * If location = India → Modify timeline + permit estimates

#### 5. **Script & Plot Engine**

* GPT builds a:

  * Three-act story structure
  * Plot twists
  * Mood boards (textual description)
* Output to Streamlit in markdown

#### 6. **Virtual Casting (via SerpAPI)**

* Match actor profiles based on:

  * Character traits
  * Budget bracket
* Fetch real actor bios & availability
* Generate audition lines for each

#### 7. **Production Plan + Risk Analysis**

* GPT generates:

  * Shooting schedule
  * Timeline compression logic
  * Common risks + mitigation (e.g. weather, availability)

#### 8. **Concept Recap & Summary**

* AI summarizes full movie concept
* Export as:

  * PDF
  * Logline
  * Script-ready summary

#### 9. **Advanced Tools (Optional)**

* Trailer Script Generator 🎥
* Audience Feedback Simulator 💬
* ROI Estimator 📊
* Music Recommender 🎵
* Legal Checklist 📜
* Talent Discovery (via trending actor APIs) 🌟
* Festival Planner 🏆

---

## 🌐 LangGraph Decision Logic Map

```text
[Start]
   |
   v
[Movie Details Step]───"Surprise Me?"───> GPT Genre & Title Generator
   |
   v
[Character Builder]───"Randomize All?"─> Batch GPT Gen
   |
   v
[Budget + Location]───"Budget < 500K?"──> Indie Logic
   |
   v
[Script Outline]
   |
   v
[Cast Mapping]───"Character Trait to Actor Match"──> SerpAPI
   |
   v
[Plan & Risk Engine]
   |
   v
[Final Movie Summary]───"Export?"──> PDF + Copy
   |
   v
[Advanced Tools?]───"Yes"──> Trailer | ROI | Feedback | Legal
   |
   v
[END]
```

---

## 🧠 Intelligence Stack

| Component         | Role                                              |
| ----------------- | ------------------------------------------------- |
| `OpenAI GPT-4`    | All creative generation: names, scripts, concepts |
| `SerpAPI`         | Real actor lookup, bios, casting data             |
| `LangGraph Agent` | Decision management between steps                 |
| `Streamlit State` | Tracks user progress and interactions             |
| `Python logic`    | Randomization, formatting, validations            |

---

## ✅ Summary

This project doesn’t just use AI — it orchestrates AI through **multi-step decisions**, **external data fusion**, and **real-time generation** using LangGraph-style workflows. Each choice a user makes alters the **flow**, enabling a unique, **adaptive cinematic production journey** with every run.

> **Your creative companion from concept to credits.** 🎬✨

---

```





---

## 🧪 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/abhishekkumar62000/Blockbuster-Movie-Production-AI-Agent.git
   cd blockbuster-movie-production-ai-agent
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Add your API keys to `.streamlit/secrets.toml`:

   ```toml
   OPENAI_API_KEY = "your-openai-key"
   SERPAPI_API_KEY = "your-serpapi-key"
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

---

## 🌐 Live Demo

Hosted on **Streamlit Cloud**
👉 [Try the Live App Here](https://your-app-url.streamlit.app) *(replace with your actual link)*

---

## 👨‍💻 Author

**Code with Abhi**
🔗 GitHub: [@codewithabhi](https://github.com/abhishekkumar62000)

---

## 📣 Summary

The **Blockbuster Movie Production Agent 🎬** is more than just an app — it’s a full-scale AI production studio in your browser. With interactive tools, intelligent workflows, and cinematic polish, users can turn an idea into a feature-length movie concept in minutes.

Whether you're a filmmaker, screenwriter, or creative thinker — this is your AI-powered launchpad to Hollywood-style storytelling.



4. Optionally, export the diagram from [https://mermaid.live](https://mermaid.live) as a PNG/SVG and upload it to your repo `/assets/` folder.

---

## ❤️ **Made with Passion by Abhishek Yadav & Open-Source Contributors!** 🚀✨


<h1 align="center">© LICENSE <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Telegram-Animated-Emojis/main/Symbols/Check%20Box%20With%20Check.webp" alt="Check Box With Check" width="25" height="25" /></h1>

<table align="center">
  <tr>
     <td>
       <p align="center"> <img src="https://github.com/malivinayak/malivinayak/blob/main/LICENSE-Logo/MIT.png?raw=true" width="80%"></img>
    </td>
    <td> 
      <img src="https://img.shields.io/badge/License-MIT-yellow.svg"/> <br> 
This project is licensed under <a href="./LICENSE">MIT</a>. <img width=2300/>
    </td>
  </tr>
</table>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="900">




 <hr>

<div align="center">
<a href="#"><img src="assets/githubgif.gif" width="150"></a>
	
### **Thanks for checking out my GitHub Profile!**  

 ## 💌 Sponser

  [![BuyMeACoffee](https://img.buymeacoffee.com/button-api/?text=Buymeacoffee&emoji=&slug=codingstella&button_colour=FFDD00&font_colour=000000&font_family=Comic&outline_colour=000000&coffee_colour=ffffff)](https://www.buymeacoffee.com/abhishekkumar62000)

## 👨‍💻 Developer Information  
**Created by:** **Abhishek Kumar**  
**📧 Email:** [abhiydv23096@gmail.com](mailto:abhiydv23096@gmail.com)  
**🔗 LinkedIn:** [Abhishek Kumar](https://www.linkedin.com/in/abhishek-kumar-70a69829a/)  
**🐙 GitHub Profile:** [@abhishekkumar62000](https://github.com/abhishekkumar62000)

<p align="center">
  <img src="https://github.com/user-attachments/assets/6283838c-8640-4f22-87d4-6d4bfcbbb093" width="120" style="border-radius: 50%;">
</p>
</div>  


`Don't forget to give A star to this repository ⭐`


`👍🏻 All Set! 💌`

</div>

---
