info_dic = {"user_name": "Cho",
            "password": "1321870261",
            }
print(info_dic.get("password"))
info_dic["sex"] = "Male"
info_dic.pop("password")
print(info_dic)
print(len(info_dic))

for k in info_dic:
    print("%s-%s" % (k, info_dic[k]))
