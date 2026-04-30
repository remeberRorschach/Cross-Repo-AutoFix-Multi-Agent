from .base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def __init__(self, config):
        prompt = "你是一位资深架构师，负责分析上游变更并制定跨仓库的级联修复长链策略。你需要输出结构化的修复步骤。"
        super().__init__("Planner", prompt, config)
