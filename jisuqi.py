import tkinter
import tkinter.messagebox


def main():
    flag = True
    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, world!')\
            if flag else ('blue', 'Goodbye, world!')
        label.config(text=msg, fg=color)
    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('240x160')
    # 设置窗口标题
    top.title('计算器')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    tos= tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    sumBtn= tkinter.Button(tos,text='+')
    sumBtn.pack(side='left')
    lBtn= tkinter.Button(tos,text='-')
    lBtn.pack(side='left')
    xBtn = tkinter.Button(tos, text='*')
    xBtn.pack(side='left')
    cBtn= tkinter.Button(tos,text='/')
    cBtn.pack(side='left')
    oneBtn= tkinter.Button(tos,text='1')
    oneBtn.pack(side='left')
    twoBtn= tkinter.Button(tos,text='2')
    twoBtn.pack(side='left')
    threeBtn= tkinter.Button(tos,text='3')
    threeBtn.pack(side='left')
    fourBtn= tkinter.Button(tos, text='4')
    fourBtn.pack(side='left')
    fiveBtn = tkinter.Button(tos, text='5')
    fiveBtn.pack(side='left')
    sixBtn= tkinter.Button(tos, text='6')
    sixBtn.pack(side='left')
    sevBtn= tkinter.Button(tos, text='7')
    sevBtn.pack(side='left')
    eightBtn = tkinter.Button(tos, text='8')
    eightBtn.pack(side='left')
    nineBtn = tkinter.Button(tos, text='9')
    nineBtn.pack(side='left')
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')
    tos.pack(side='top')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()
