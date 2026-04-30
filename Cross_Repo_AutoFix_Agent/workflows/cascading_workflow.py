import time
from agents.planner import PlannerAgent
from agents.coder import CoderAgent
from agents.reviewer import ReviewerAgent

class AutoFixWorkflow:
    def __init__(self, config):
        self.planner = PlannerAgent(config)
        self.coder = CoderAgent(config)
        self.reviewer = ReviewerAgent(config)

    def run(self, change_event: str):
        print(f"[Workflow] 检测到上游变更: {change_event}")
        
        # Step 1: Planning
        plan = self.planner.chat(f"针对以下变更制定修复计划: {change_event}")
        print(f"[Planner] 修复方案已生成。")

        # Step 2 & 3: Coding & Review with Reflection Loop
        max_retries = 3
        for i in range(max_retries):
            code_fix = self.coder.chat(f"执行以下计划: {plan}")
            print(f"[Coder] 第 {i+1} 次代码修复尝试...")

            review_result = self.reviewer.chat(f"审计以下修复代码: {code_fix}")
            if "APPROVED" in review_result.upper():
                print(f"[Reviewer] 审计通过！修复完成。")
                return code_fix
            else:
                print(f"[Reviewer] 发现缺陷，触发自我反思 (Reflection)...")
                plan = f"修正以下错误后重新编写代码: {review_result}"
        
        return "Workflow failed after max retries."
