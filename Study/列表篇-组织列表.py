print("这是一个实验整合项目，主要整合组织列表这个章节")
List = ["car", "foot", "coffe", "aplle", "sorcker"]  # 这里是定义一个列表
ID = input("请输入实验编号")
if ID in "1":
    List.sort()  # 正向输出代码
    print("将按照正向输出列表")
    print(List)
elif ID in "2":
    List.sort(reverse=True)  # 反向输出代码
    print("将按照反向输出")
    print(List)
elif ID in "3":
    print("将按照正向输出，但是并非永久")
    print(sorted(List, reverse=True))  # 非永久性正向输出代码
    print("这时输出原始列表就发现列表其实并没有变化")
    print(List)
elif ID in "4":
    print("将按照反向输出但是并非永久")
    print(sorted(List, reverse=True))  # 非永久性反向输出代码
    print("这时输出原始列表就发现列表其实并没有变化")
    print(List)
else:
    print("代码错误")
