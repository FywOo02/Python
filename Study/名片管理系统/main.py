from Study.名片管理系统 import tool

while True:
    # 显示功能菜单
    action = tool.menu_show()
    # 1,2,3 针对名片操作
    if action in ["1", "2", '3']:
        if action == "1":
            tool.new_card()
        elif action == "2":
            tool.show_all()
        else:
            tool.search_card()
    # 0 退出系统
    elif action == "0":
        print("欢迎再次使用名片系统")
        break
    else:
        print("您输入的操作有误，请重新输入")

