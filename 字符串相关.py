xiaoxie = "hello world"
print(xiaoxie.title()) #首字母大写输出
print(xiaoxie.upper()) #字母全部大写输出
print(xiaoxie.lower()) #字母全部小写输出
#拼接字符串
first_name = ("桜")
last_name = ("火")
# 去掉空格
space = (" hello ")
print ("这是没有去空格的代码", space)
print("这是去了尾部空格的代码", space.rstrip())
print("这是去了头部空格的", space.lstrip())
print("这是同时去了去了头尾的空格的", space.strip())
# 制表符相关
# \t为表示器，表示要在字符串中添加制表符
# \n为换行指示器，放入后会在\n处提行
# 可以n+t
print("\t Python \n JAVA \n C# \t\n 都是啥")
