#for HC
def printf():
    print("num     name    scor\n")
    for i in range(n):
        print(num[i], "  ", name[i], " ", scor[i], "\n")
n=1
num=[1001]
name=['张元皓']
scor=[100]
while True:
    x = input("请输入操作\n")
    if x == "1":
        num.append(input("请输入编号\n"))
        name.append(input('请输入名字\n'))
        scor.append(input('请输入分数\n'))
        n=n+1
    elif x=="2":
        try:
            numb=num.index(input("请输入学生编号"))
        except BaseException :
            print("没有该同学的数据")
        else:
            num[numb]=input("请输入修改后的编号")
            name[numb]=input("请输入修改后的名字")
            scor[numb]=input("请输入修改后的分数")
    printf()