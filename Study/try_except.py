class try_except_demo:
    try:
        num = int(input("请输入一个整数"))
        result = 8 / num
        print(result)

    except ZeroDivisionError:
        print("分母不能为零")

    except ValueError:
        print("请输入正确的整数")

    except Exception as result:
        print("未知错误 %s" % result)

    else:
        pass

    finally:
        print("无论有什么异常，最后都会执行这句话")
