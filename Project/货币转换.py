info = input("请输入货币数量（不要加货币单位）")
Currency_type = input("请输入货币单位（如￥$)")
if Currency_type in ["$"]:
    a1 = ["RMB"]
    info = int(info)
    RMB = (info * 6.977)
    EUR = (info * 0.849)
    print("可兑换为", round(RMB, 3), "RMB")
    print("可兑换为", round(EUR, 3), "EUR")
elif Currency_type in ["￥"]:
    a2 = ["USD"]
    info = int(info)
    round(info, 4)
    USD = (info / 6.977)
    EUR = (info / 8.211)
    print("可兑换为", round(USD, 3), "USD")
    print("可兑换为", round(EUR, 3), "EUR")
elif Currency_type in ["€"]:
    a3 = ["Euro"]
    info = int(info)
    round(info, 4)
    RMB = (info * 8.211)
    USD = (info * 1.177)
    print("可兑换为", round(USD, 3), "USD")
    print("可兑换为", round(RMB, 3), "RMB")
else:
    print("输入错误")
ready = input("运行完毕，按任意键退出")