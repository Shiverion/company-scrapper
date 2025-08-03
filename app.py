import os
import requests
from bs4 import BeautifulSoup
from typing import List
from dotenv import load_dotenv
from openai import OpenAI as OpenAIClient
import gradio as gr

load_dotenv(override=True)

openai_api_key = os.getenv('OPENAI_API_KEY')
google_api_key = os.getenv('GOOGLE_API_KEY')


class Website:
    def __init__(self, url: str):
        self.url = url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"

        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()

        self.text = soup.body.get_text(separator="\n", strip=True)

    def get_contents(self) -> str:
        return f"Webpage Title:\n{self.title}\nWebpage Contents:\n{self.text}\n\n"


class Chatbot:
    def __init__(self):
        self.system_message = "You are a helpful assistant that responds in markdown"
        self.openai = OpenAIClient(api_key=openai_api_key)
        self.gemini = OpenAIClient(
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            api_key=google_api_key
        )
       

    def stream_gpt(self, prompt: str):
        messages = [
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": prompt}
        ]
        stream = self.openai.chat.completions.create(
            model='gpt-4o',
            messages=messages,
            stream=True
        )
        result = ""
        for chunk in stream:
            result += chunk.choices[0].delta.content or ""
            yield result
       

    def stream_gemini(self, prompt: str):
        messages = [
            {"role": "system", "content": self.system_message},
            {"role": "user", "content": prompt}
        ]
        stream = self.gemini.chat.completions.create(
            model='gemini-2.5-flash',
            messages=messages,
            stream=True
        )
        result = ""
        for chunk in stream:
            result += chunk.choices[0].delta.content or ""
            yield result
        

    def stream_brochure(self, company_name: str, url: str, model: str):
        yield ""
        prompt = f"Please generate a company brochure for {company_name}. Here is their landing page:\n"
        prompt += Website(url).get_contents()
        if model == "GPT":
            yield from self.stream_gpt(prompt)
        elif model == "Gemini":
            yield from self.stream_gemini(prompt)
        else:
            raise ValueError("Unknown model selected.")


chatbot = Chatbot()

view = gr.Interface(
    fn=chatbot.stream_brochure,
    inputs=[
        gr.Textbox(label="Company name:"),
        gr.Textbox(label="Landing page URL including http:// or https://"),
        gr.Dropdown(["Gemini", "GPT"], label="Select model")
    ],
    outputs=gr.Markdown(label="Brochure:"),
    flagging_mode="never"
)

if __name__ == "__main__":
    view.launch()
