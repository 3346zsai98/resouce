# create database heima charset="utf8";
# use heima;
# create table user (
#     -> id int unsigned primary key auto_increment,
#     -> name varchar(32) unique not null,
#     -> password varchar(32)
#     -> );

import pymysql
class User(object):
    def __init__(self):
        self.conn = pymysql.connect(host="localhost",port=3306,user="root",password="mysql",db="heima",charset="utf8")
    def __del__(self):
        self.conn.close()
    def show_menu(self):
        print("-------欢迎来到黑马程序猿-------")
        print("1：注册")
        print("2：登录")
        print("3：退出")

    def zuce(self):
        cur = self.conn.cursor()
        name = input("请输入您的用户名：")
        sql = "select name from user where name=%s;"
        cur.execute(sql,[name])
        if cur.fetchall():
            print("该用户名已经存在，请重新注册！")
            cur.close()
        pwd = input("请输入您的密码：")
        repwd = input("请确认您的密码：")
        if pwd != repwd:
            print("两次密码输入不一致，请重新输入！")
            cur.close()
        else:
            sql = "insert into user(name,password) values(%s,%s)"
            cur.execute(sql,[name,pwd])
        #     self.conn.commit()
            cur.close()
    def denglu(self):
        cur = self.conn.cursor()
        name = input("请输入您的用户名：")
        pwd = input("请输入您的密码：")
        sql = "select name from user where name=%s and password=%s;"
        cur.execute(sql,[name,pwd])
        if cur.fetchall():
            print("登陆成功")
        else:
            print("你输入的密码或用户名有错，请重新输入！")
        cur.close()

    def start(self):
        self.show_menu()
        while True:
            op = input("请输入功能对应的序号：")
            if op == "1":
                self.zuce()
            elif op == "2":
                self.denglu()
            elif op == "3":
                print("关闭连接，欢迎下次登录！")
                break
heima = User()
heima.start()