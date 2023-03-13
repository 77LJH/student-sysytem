
import os

filename = 'student.txt'


def main():
    while True:
        menu()
        try:
            choice = int(input('请选择：'))
            if choice in range(8):
                if choice == 0:
                    answer = input('您确定要退出吗？y/n：')
                    if answer == 'y' or answer == 'Y':
                        print('谢谢你的使用')
                        break
                    else:
                        continue
                elif choice == 1:
                    insert()  # 录入学生信息
                elif choice == 2:
                    search()  # 查找学生信息
                elif choice == 3:
                    delete()  # 删除学生信息
                elif choice == 4:
                    modify()  # 修改学生信息
                elif choice == 5:
                    sort()  # 对学生成绩排序
                elif choice == 6:
                    total()  # 统计学生总人数
                elif choice == 7:
                    show()  # 显示所有的学生信息
            else:
                print('输入值非法lll')
        except BaseException as e:
            print('输入值非法hhh', e)


def menu():
    print('======================================学生管理系统==========================================')
    print('---------------------------------------功能菜单--------------------------------------------')
    print('\t\t\t\t\t\tl.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5,排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出')
    print('-----------------------------------------------------------------------------------------')


def insert():
    student_lst = []
    while True:
        stu_id = input('请输入学生ID：')
        if not stu_id:
            break
        name = input('请输入学生姓名：')
        if not name:
            break
        try:
            eng_score = int(input('请输入学生英语成绩：'))
            python_score = int(input('请输入学生Python成绩：'))
            java_score = int(input('请输入学生Java成绩：'))
        except BaseException as e:
            print('输入的分数不是整数类型，请重新输入', e)
        else:
            # 将录入的学生信息保存到字典中
            student = {'stu_id': stu_id, 'name': name, 'eng_score': eng_score, 'python_score': python_score,
                       'java_score': java_score}
            # 将学生信息添加到列表中
            student_lst.append(student)
            answer = input('是否继续添加？y/n：')
            if answer in ['y', 'Y']:
                continue
            else:
                break
    # 调用save函数保存
    save(student_lst)
    print('学生信息录入完毕')


def save(lst):
    # noinspection PyBroadException
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except BaseException as e:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query = []
    while True:
        stu_id = ''
        name = ''
        if os.path.exists(filename):
            mode = int(input('按ID查找按1，按姓名查找按2：'))
            if mode == 1:
                stu_id = input('请输入学生ID：')
            elif mode == 2:
                name = input('请输入学生名字：')
            else:
                print('非法输入')
                continue
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if stu_id and d['stu_id'] == stu_id:
                        student_query.append(d)
                    elif name and d['name'] == name:
                        student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer = input('是否继续查询？y/n：')
            if answer in ['y', 'Y']:
                continue
            else:
                break
        else:
            print('未保存学生信息')
            return


def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无法显示')
        return
    # 定义标题显示格式
    format_title = '{:^16}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    # 定义内容的显示格式
    format_data = '{:^16}\t{:^12}\t{:^8}\t{:^10}\t{:^8}\t{:^8}'
    for item in lst:
        print(format_data.format(item.get('stu_id'),
                                 item.get('name'),
                                 item.get('eng_score'),
                                 item.get('python_score'),
                                 item.get('java_score'),
                                 int(item.get('eng_score')) + int(item.get('python_score')) + int(item.get('java_score')
                                                                                                  )))


def delete():
    while True:
        stu_id = input('请输入要删除的学生ID：')
        if stu_id:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转成字典
                        if d['stu_id'] != stu_id:

                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print('ID为{0}的学生信息已删除'.format(stu_id))
                    else:
                        print('没有找到ID为{0}的学生信息'.format(stu_id))
            else:
                print('无学生信息')
                break
            show()
            answer = input('是否继续删除？y/n：')
            if answer in ['y', 'Y']:
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    stu_id = input('请输入要修改的学生ID：')
    with open(filename, 'w', encoding='utf-8') as wfile:
        flag = False
        for item in student_old:
            d = dict(eval(item))
            if d['stu_id'] == stu_id:
                print('找到学生信息，可以修改了')
                while True:
                    try:
                        d['stu_id'] = input('请输入学生ID：')
                        d['name'] = input("请输入学生姓名：")
                        d['eng_score'] = input("请输入学生英语成绩：")
                        d['python_score'] = input("请输入学生Python成绩：")
                        d['java_score'] = input("请输入学生Java成绩：")
                    except BaseException as e:
                        print('输入的分数不是整数类型，请重新输入', e)
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功')
                flag = True
            else:
                wfile.write(str(d) + '\n')
        if not flag:
            print('没有找到该学号的学生信息，无法进行修改')
        answer = input('是否继续修改其他学生的信息？y/n：')
        if answer in ['y', 'Y']:
            modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_lst = rfile.readlines()
        student_new = []
        for item in student_lst:
            d = dict(eval(item))
            student_new.append(d)
    else:
        return
    while True:
        asc_or_desc = int(input('请选择升序0，还是降序1：'))
        if not asc_or_desc:
            asc_or_desc_bool = False
            break
        elif asc_or_desc:
            asc_or_desc_bool = True
            break
        else:
            print('输入错误，请重新输入')
    while True:
        mode = int(input('请选择排序方式(1,按英语成绩排序 2.按python成绩排序 3.java成绩排序 0.按总成绩排序：'))
        if mode == 1:
            student_new.sort(key=lambda x: int(x['eng_score']), reverse=asc_or_desc_bool)
            break
        elif mode == 2:
            student_new.sort(key=lambda x: int(x['python_score']), reverse=asc_or_desc_bool)
            break
        elif mode == 3:
            student_new.sort(key=lambda x: int(x['java_score']), reverse=asc_or_desc_bool)
            break
        elif mode == 0:
            student_new.sort(key=lambda x: int(x['eng_score'])+int(x['python_score'])+int(x['java_score']), reverse=asc_or_desc_bool)
            break
        else:
            print('输入错误，请重新输入')
    show_student(student_new)


def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student = rfile.readlines()
            if student:
                print(f'一共有{len(student)}学生', type(student))
            else:
                print('没有学生信息')
    else:
        print('没有学生信息')
        return


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('没有存过学生信息')
        return


if __name__ == '__main__':
    main()
