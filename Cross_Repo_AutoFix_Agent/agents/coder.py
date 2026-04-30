from .base_agent import BaseAgent

class CoderAgent(BaseAgent):
    def __init__(self, config):
        prompt = "你是一位精通多语言的开发工程师，负责根据规划策略编写高质量的修复代码。请确保代码符合原库的编程风格。"
        super().__init__("Coder", prompt, config)
