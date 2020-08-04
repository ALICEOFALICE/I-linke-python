def ccc(wendu):                                     #本行定义了一个叫ccc的函数，内置了温度转换
    if wendu[-1] in ("F","f"):                      #调用if如果函数ccc返回的数值最后一位为（F，f），则进入if分支的算法
        sheshidu =(eval(wendu[0:-1]) - 32) / 1.8    #eval将wendu的最后一位去掉后把其余部分转换为字符串，并且进行计算（wendu-32）/1.8
        print(sheshidu)                             #输出变量sheshidu
    elif wendu[-1] in ("C","c"):                    #如果返回数值为（C，c），则进入elif分支
        huashedu = (eval(wendu[0:-1]) * 1.8) + 32   #eval将wendu的最后一位去掉后把其余部分转换为字符串,并进行计算（wendu*1.8) + 32
        print (huashedu)                            #输出变量sheshidu
    else:print("输入的数值错误")                     #如果是其他输入，返回错误信息

wendu1 = input("请输入温度")                         #使用input函数把输入值赋予wendu1变量
ccc(wendu1)                                         #调用ccc函数并设置输入值为wendu2
#这代码抄的我一脸懵逼，这个文件暂时锁起来，不要去管
