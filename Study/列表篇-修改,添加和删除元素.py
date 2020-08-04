print("这是一个实验整合项目，主要整合数列这个章节")
# 本源码由桜火编写
List = ["xie", "li", "yang", "liu", "rong", "rui"]
print("列表默认状态", List)
print("实验编码参考 \n 输出列表：1 \n 向列表末尾数值：2 \n 向列表指定位置添加数值:3 \n 向列表删除数值：4 \n 向列表弹出数值：5 \n 通过内容\
向列表删除：6 ")
ID = input("请选择实验编码")
if ID in "1":
    print("您选择了实验编码：1 \t 正在为您输入列表")
    print(List)
elif ID in "2":
    print("您选择了实验编码：2 \t 请及时输入您要添加的数值")
    LastAdd = input("请输入要添加到末尾的数值")
    List.append(LastAdd)
    print("正在为您添加列表并输出")
    print(List)
elif ID in "3":
    print("您选择了实验编码：3 \t 请及时输入您要添加的位置与数值")
    postion = input("请输入你需要的位置（从0开始）（-1代表倒数第二个）")
    Add = input("请输入你要添加的数值")
    List.insert(int(postion), Add)
    print("正在为您添加列表并输出")
    print(List)
elif ID in "4":
    print("您选择了实验编码：4 \t 请及时输入您要删除的位置")
    Delpostion = input("您要删除的数值所在位置")
    del List[int(Delpostion)]
    print("正在为您删除列表并输出")
    print(List)
elif ID in "5":
    print("您选择了实验编码：5 \t 请及时输入您要弹出的位置")
    print("本次弹出将从列表中删除数值，并将被删除的数值赋予一个变量")
    pop_up = input("请输入要弹出的数值")
    pop_up_List = List.pop(int(pop_up))
    print("正在为您弹出列表并输出")
    print("弹出的数值", pop_up_List)
    print("剩余列表", List)
elif ID in "6":
    connect = input("请输入列表中的内容")
    List.remove(connect)
    print("正在为您删除列表并输出（注意：Remove不会输出内容，和上面insert那些不一样）")
    print(List)
    print("不知道我那本书干啥，非要搞一个变量来存一下被删除的数值，那就输出出来吧", connect)
else:
    print("没其他的了，列表那张第二节讲完了")
ready = input("运行完毕，按任意键退出")
