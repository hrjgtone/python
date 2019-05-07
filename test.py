# tkinter复选框操作

import tkinter as tk

root = tk.Tk()
root.title('问卷调查')
root.geometry('220x80')  # 设置窗口大小

flag_1 = False
flag_2 = False
flag_3 = False
list_content = ['你的爱好是：']
hobby_list = ['游泳', '唱歌', '旅游']


def click_1():
    global flag_1
    flag_1 = not flag_1
    if flag_1:
        list_content.append(hobby_list[0])
    else:
        list_content.remove(hobby_list[0])
    # print('你的爱好是：', list_content)
    lab_msg['text'] = list_content


def click_2():
    global flag_2
    flag_2 = not flag_2
    if flag_2:
        list_content.append(hobby_list[1])
    else:
        list_content.remove(hobby_list[1])
    # print('你的爱好是：', list_content)
    lab_msg['text'] = list_content


def click_3():
    global flag_3
    flag_3 = not flag_3
    if flag_3:
        list_content.append(hobby_list[2])
    else:
        list_content.remove(hobby_list[2])
    # print('你的爱好是：', list_content)
    lab_msg['text'] = list_content


'''窗体控件'''
# 标题显示
lab = tk.Label(root, text='请选择你的爱好：')
lab.grid(row=0, columnspan=3, sticky=tk.W)

# 多选框
frm = tk.Frame(root)
ck1 = tk.Checkbutton(frm, text='游泳', command=click_1)
ck2 = tk.Checkbutton(frm, text='唱歌', command=click_2)
ck3 = tk.Checkbutton(frm, text='旅游', command=click_3)
ck1.grid(row=0)
ck2.grid(row=0, column=1)
ck3.grid(row=0, column=2)
frm.grid(row=1)

lab_msg = tk.Label(root, text='')
lab_msg.grid(row=2, columnspan=3, sticky=tk.W)

root.mainloop()
