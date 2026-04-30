import openai
from typing import List, Dict, Any

class BaseAgent:
    def __init__(self, name: str, system_prompt: str, config: Dict):
        self.name = name
        self.system_prompt = system_prompt
        self.client = openai.OpenAI(api_key=config['llm']['api_key'])
        self.model = config['llm']['model']

    def chat(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
