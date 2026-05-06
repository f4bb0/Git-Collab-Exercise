# -*- coding: utf-8 -*-
# Git 协作练习脚本

import datetime

def main():
    print("--- 团队协作演示开始 ---")
    
    # TODO: 请在下方添加代码
    # 例如加一句 print
    print("member hhp is here!")
    print("hhp use gitbash commit this time!")
    print("hhp use github desktop commit this time!")
    print("welcome the foreign member?")

    # Team member contributions all sample names
    team_members = [
        "Alice: Frontend developer",
        "Bob: Backend developer", 
        "Charlie: DevOps engineer",
        "Diana: UI/UX designer"
    ]
    
    print("\n👥 Current Team:")
    for member in team_members:
        print(f"  • {member}")
    
    # Current timestamp
    print(f"\n📅 Session time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # TODO: Add your feature here
    print("\n✨ Active tasks:")
    print("  - Implement login system (Bob)")
    print("  - Design landing page (Diana)")
    print("  - Setup CI/CD pipeline (Charlie)")
    print("  - Create API documentation (Alice)")
    
    print("\n--- 演示结束 ---")

if __name__ == "__main__":
    main()