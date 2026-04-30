import yaml
from workflows.cascading_workflow import AutoFixWorkflow

def main():
    # 模拟配置加载
    config = {
        'llm': {'api_key': 'sk-xxxx', 'model': 'gpt-4', 'max_tokens': 2000}
    }
    
    workflow = AutoFixWorkflow(config)
    
    # 模拟一个上游库 API 修改导致下游崩溃的场景
    event = "Upstream Auth-Lib: login() function signature changed from login(user, pass) to login(credentials_dict)."
    
    print("=== Cross-Repo AutoFix 系统启动 ===")
    workflow.run(event)
    print("=== 工作流执行结束 ===")

if __name__ == "__main__":
    main()
