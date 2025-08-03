# 🏢 Company Brochure Scraper & Generator

Ever needed to generate a company brochure, *fast*, using just their website?  
This tool scrapes a company's landing page and uses LLMs (GPT-4o or Gemini 2.5 Flash) to generate a markdown-formatted brochure. Built with 💻 Python, 🌐 BeautifulSoup, and 🔮 OpenAI + Gemini.

---

## ⚙️ Features

- 🌐 Scrape text & title from any landing page
- 🧠 Generate brochures using:
  - OpenAI GPT-4o
  - Gemini 2.5 Flash (via OpenAI-compatible endpoint)
- 🖼️ Simple, elegant UI via Gradio
- 🔃 Streaming text generation
- ⚡ Fast setup using `uv` (Python's next-gen package manager)
- 🚀 Deployed on [Hugging Face Spaces](https://huggingface.co/spaces/Shiverion/Company_Scrapper)

---

## 🧠 Tech Stack

| Layer        | Tech                      |
|--------------|---------------------------|
| Language     | Python 3.11+              |
| UI           | Gradio                    |
| Web Scraping | BeautifulSoup             |
| LLMs         | OpenAI GPT-4o, Gemini 2.5 |
| Package Mgmt | [`uv`](https://github.com/astral-sh/uv)       |
| Env Mgmt     | `dotenv`                  |

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/Shiverion/company-scrapper.git
cd company-scrapper
```
### 2. Setup dependencies using uv
```bash
uv sync
```
This will create a .venv folder and install dependencies from requirements.txt in a flash.

### 3. Setup your Environment Variables
```env
OPENAI_API_KEY=your_openai_key_here
GOOGLE_API_KEY=your_gemini_key_here
```

🚀 How to Run
```
uv run app.py
```
This launches a Gradio interface where you:
- Enter a company name
- Paste the landing page URL (must include https://)
- Choose your preferred LLM (GPT or Gemini)
- Get a beautiful, markdown-formatted brochure — live-streamed!

---
  🧪 Example Use Case
Input:
  Company name: Shiverion AI
  URL: https://shiverion.my.canva.site/
  Model: Gemini
Output:
  A full markdown brochure describing services, tone, and vibe, scraped and generated directly from the landing page.

🌍 Live Demo
Coming soon on Hugging Face Spaces 🚀
Want to deploy? Just copy-paste this repo to your own Hugging Face account and you're good to go.

✨ Author
Crafted with markdown magic by [@Shiverion](https://github.com/Shiverion)
💼 [Linkedin](www.linkedin.com/in/izzulhaq-iqbal) • 📧 miqbal.izzulhaq@gmail.com

📄 License
MIT License — use it, remix it, build on it.
