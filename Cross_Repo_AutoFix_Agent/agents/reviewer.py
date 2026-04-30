from .base_agent import BaseAgent

class ReviewerAgent(BaseAgent):
    def __init__(self, config):
        prompt = "你是一位严格的代码审计师。如果你发现代码存在逻辑错误或测试未通过，请详细列出原因并触发 Reflection 机制让 Coder 重写。"
        super().__init__("Reviewer", prompt, config)
