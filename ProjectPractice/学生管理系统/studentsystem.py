#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：TestProject 
@File ：studentsystem.py
@Author ：xiangzhi
@Date ：2021/5/7 10:44 
'''
import os
import re


def menu():
    """
    输出菜单
    :return:
    """
    print('''
    ---------------学生信息管理系统---------------
         ==========功能菜单==========
         
         1 录入学生信息
         2 查找学生信息
         3 删除学生信息
         4 修改学生信息
         5 排序
         6 统计学生总人数
         7 退出系统
         =======================================
         说明：通过数字或者上下键选择菜单
    --------------------------------------------
    ''')


def insert():
    """
    录入学生信息
    :return:
    """
    studentlist = []
    mark = True
    while mark:
        id = input("请输入ID（如 1001）：")
        if not id: # ID为空，跳出循环
            break
        name = input("请输入名字： ")
        if not name: # 名字为空， 跳出循环
            break
        try:
            english = input("请输入英语成绩： ")
            python = input("请输入Python成绩： ")
            c = input("请输入c语言成绩：")
        except:
            print("输入无效，不是整型数值...请重新输入")
            continue
        student = {"id": id, "name": name, "english": english, "python": python, "c": c}
        studentlist.append(student)
        inputMark = input("是否继续添加？ （y/n）:")
        if inputMark == "y":
            mark = True
        else:
            mark = False
        save(studentlist)
        print("学生信息录入完毕！！！")


def save(student):
    """
    将学生信息保存到文件
    :param student: 学生列表
    :return:
    """
    try:
        student_txt = open(filename, "a") # 以追加模式打开
    except Exception as e:
        student_txt = open(filename, "w") # 文件不存在，创建文件并打开
    for info in student:
        student_txt.write(str(info) + "\n") # 按行存储， 添加换行符
    student_txt.close()  # 关闭文件


def search():
    """
    2 查找学生成绩信息
    :return:
    """
    mark = True
    student_query = []
    while mark:
        id = ""
        name = ""
        if os.path.exists(filename): # 判断文件是否存在
            mode = input("按id查找输入1；按姓名查找输入2：")
            if mode == "1":
                id = input("请输入学生id： ")
            elif mode == "2":
                name = input("请输入学生姓名： ")
            else:
                print("你输入有误，请重新输入！")
                search()  # 重新查找
            with open(filename, "r") as file: # 打开文件
                student = file.readlines() # 读取全部内容
                for list in student:
                    d = dict(eval(list))
                    if id is not "":
                        if d["id"] == id:
                            student_query.append(d)
                    elif name is not "":
                        if d["name"] == name:
                            student_query.append(d)
                show_student(student_query)
                student_query.clear()
                inputMark = input("是否集训查询？ （y/n）:")
                if inputMark == "y":
                    mark = True
                else:
                    mark = False
        else:
            print("暂为保存信息。。。")
            return



def delete():
    """
    删除学生成绩信息
    :return:
    """
    mark = True
    while mark:
        studentId = input("请要输入要删除的学生id:")
        if studentId is not "": # 判断要删除的学生是否存在
            if os.path.exists(filename):
                with open(filename, "r") as rfile:
                    studentoid = rfile.readlines()
            else:
                studentoid = []
            ifdel = False # 标记是否删除
            if studentoid: # 如果存在学生信息
                with open(filename, "w") as wfile:
                    d = {} # 定义空字典
                    for list in studentoid:
                        d = dict(eval(list))
                        if d["id"] != studentId:
                            wfile.write(str(d) + "\n") # 将一条学生信息写入文件
                        else:
                            ifdel = True
                    if ifdel:
                        print("id为 %s 的学生已经被删除。。。" % studentId)
                    else:
                        print("没有找到id为 %s 的学生信息。。。" % studentId)
            else:
                print("无学生信息")
                break
            show()
            inputMark = input("是否继续删除？ y/n:")
            if inputMark == "y":
                mark = True
            else:
                mark = False


def modify():
    """
    修改学生成绩信息
    :return:
    """
    show()
    if os.path.exists(filename):
        with open(filename, "r") as rfilse:
            studentoid = rfilse.readlines()
    else:
        return
    studentid = input("请输入要修改的学生id：")
    with open(filename, "w") as wfilse:
        for student in studentoid:
            d = dict(eval(student))
            if d["id"] == studentid:
                print("找到了这名学生的id，可以修改他的信息！")
                while True:
                    try:
                        d["name"] = input("请输入姓名：")
                        d["english"] = int(input("请输入英语成绩："))
                        d["python"] = int(input("请输入python成绩"))
                        d["c"] = int(input("请输入c的成绩"))
                    except:
                        print("你输入的信息有误")
                    else:
                        break
                student = str(d)
                wfilse.write(student + "\n")
                print("修改成功")
            else:
                wfilse.write(student)
    mark = input("是否继续修改其他学生信息？ （y/n）:")
    if mark == "y":
        modify()

def sort():
    show()
    if os.path.exists(filename):
        with open(filename, "r") as file:
            studentoid = file.readlines()
            student_new = []
            for list in studentoid:
                d = dict(eval(list))
                student_new.append(d)
    else:
        return
    ascORdesc = input("请选择（0 升序：1 降序）:")
    if ascORdesc == "0":
        ascORdescBool = False
    elif ascORdesc == "1":
        ascORdescBool = True
    else:
        print("你输入的有误，请重新输入")
        sort()
    mode = input("请选择排序方式（1：按英语；2按Python；3按c语言）")
    if mode == "1":
        student_new.sort(key=lambda x: x["english"], reverse=ascORdescBool)
    elif mode == "2":
        student_new.sort(key=lambda x: x["python"], reverse=ascORdescBool)
    elif mode == "3":
        student_new.sort(key=lambda x:x["c"], reverse=ascORdescBool)
    elif mode == "0":
        student_new.sort(key=lambda x:x["english"] + x["python"] + x["c"], reverse=ascORdescBool)
    else:
        print("你的输入有误，重新输入")
        sort()
    show_student(student_new)


def total():
    """
    统计学生总数
    :return:
    """
    if os.path.exists(filename):
        with open(filename, "r") as rfile:
            studentold = rfile.readlines()
            if studentold:
                print("一共有 %d 名学生！" % len(studentold))
            else:
                print("还没有录入学生信息")
    else:
        print("暂未保存数据信息。。。")


def show():
    """
    显示所有学生信息
    :return:
    """
    student_new = []
    if os.path.lexists(filename):
        with open(filename, "r") as rfile:
            student_old = rfile.readlines()
        for list in student_old:
            student_new.append(eval(list))
        if student_new:
            show_student(student_new)
    else:
        print("暂未保存数据信息")


def show_student(studentList):
    if not studentList:
        print("无数据信息")
        return
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID", "名字", "英语成绩", "python成绩", "c语言成绩", "总成绩"))
    format_data = "{:^6}{:^12}\t{:^8}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:
        print(format_data.format(info.get("id"), info.get("name"), str(info.get("english"))
                                 , str(info.get("python")), str(info.get("c")),
        str(info.get("english")) + str(info.get("python")) + str(info.get("c"))))



def main():
    ctrl = True
    while ctrl:
        menu() # 显示菜单
        option = input("请选择：") # 选择菜单项
        option_str = re.sub("\D", "", option) # 提取数字
        if option_str in ["0", "1", "2", "3", "4", "5", "6", "7"]:
            option_int = int(option_str)
            if option_int == 0:
                print("您已经退出成绩管理系统")
                ctrl = False
            elif option_int == 1:
                insert()
            elif option_int == 2:
                search()
            elif option_int == 3:
                delete()
            elif option_int == 4:
                modify()
            elif option_int == 5:
                sort()
            elif option_int == 6:
                total()
            elif option_int == 7:
                show()

if __name__ == '__main__':
    filename = "student.text"
    main()