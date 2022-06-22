# 记录所有的名片字典
card_list = []


def menu_show():
    # 显示功能菜单
    print("*" * 50)
    print("欢迎使用【名片管理系统】 v1.0")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("0.退出程序")
    print("*" * 50)
    action = input("请输入您的操作: ")
    return action


def menu_show_again():
    # 当用户完成一次操作后，返回上一级别
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("0.退出程序")
    action = input("请输入您的操作: ")
    return action


def new_card():
    """新增名片

    """
    # 1. 用户输入信息
    name = input("请输入姓名: ")
    sex = input("请输入性别: ")
    phone = input("请输入电话: ")
    # 2. 建立名片字典
    card_dict = {"name": name,
                 "sex": sex,
                 "phone": phone}
    # 3. 将字典添加至列表
    card_list.append(card_dict)
    print("添加%s的名片成功！" % name)


def show_all():
    """显示全部名片

    :return:返回上级菜单
    """
    # 判断是否存在名片记录
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增功能添加名片")
        return
    # 1.打印表头
    for head in ["姓名", "性别", "电话"]:
        print(head, end='\t\t')
    print(" ")
    print("=" * 50)
    # 2.遍历名片列表并输出
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                      card_dict["sex"],
                                      card_dict["phone"]))


def search_card():
    """查找名片

    """
    find_name = input("请输入要搜索的姓名：")

    # 遍历名片列表，判断是否存在要查询的姓名，并输出
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t性别\t\t电话")
            print(" ")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                          card_dict["sex"],
                                          card_dict["phone"]))
            deal_card(card_dict)
            break
    else:
        print("未找到您所需的%s的名片" % find_name)


def deal_card(find_dict):
    """处理查找到的名片

    :param find_dict:查找到的名片
    :return:返回上一级菜单
    """
    action = input("请选择要执行的操作"
                   "[1]修改 [2]删除 [0]返回上级菜单")
    if action == "1":
        find_dict["name"] = input_card_info(find_dict["name"], "姓名：")
        find_dict["sex"] = input_card_info(find_dict["sex"], "性别：")
        find_dict["phone"] = input_card_info(find_dict["phone"], "电话：")
        print("名片修改成功")
    elif action == "2":
        card_list.remove(find_dict)
        print("名片删除成功 ")
    elif action == "0":
        return


def input_card_info(dict_value, tip_info):
    """修改名片信息工具类

    :param dict_value:字典原有值
    :param tip_info:输入的提示文字
    :return:如果用户输入了内容，则返回内容，否则返回原有值
    """
    # 提示用户输入内容
    result = input(tip_info)
    # 针对用户输入进行判断，若输入则返回结果
    if len(result) != 0:
        return result
    # 如果用户没有输入内容，则返回原有的值
    else:
        return dict_value
    pass
