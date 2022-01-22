""""

# 새로운 윈도우 창 만들기
window = tkinter.Tk()

# 창 이름, 사이즈, 늘렸다줄이기 여부
window.title("jeong gang hyeon")
window.geometry("1000x700+100+100")  # ("너비*높이+x좌표+y좌표")
window.resizable(1,1)

# 글씨 추가
label=tkinter.Label(window, text="문장",font=("글씨체",30),height=10)

# 숫자 버튼으로 높이고 줄이기
tkinter.Spinbox(window, from_=0, to=30)  # Spinbox(원하는 화면,최저,최대)

def getTextInput():
    result=text1.get("1.0","end")
    print(list(map(int,result.split())))
"""


import tkinter
import random
from time import sleep


# window = tkinter.Tk()
# window.title("숫자 기억 게임")
# window.geometry("1000x700+100+100")  # ("너비*높이+x좌표+y좌표")
# window.resizable(1,1)

class Tool():
    def __init__(self):
        self.window=tkinter.Tk()
        self.label = tkinter.Label(text="", font=('Helvetica', 48), fg='red')
        self.label.pack()
        self.plzplz()
        self.window.mainloop()
    def plzplz(self):
        self.label.configure(text=random.randint(1, 99))
        self.window.after(1000,self.plzplz)

app=Tool()

# num=3
#
# def ad(self):
#     self.window = tkinter.Tk()
#     self.label = tkinter.Label(text="", font=('Helvetica', 48), fg='red')
#     self.label.pack()
#     for i in range(num):
#         self.plzplz()
#     self.window.mainloop()
#
# def plzplz(self):
#     self.label.configure(text=random.randint(1, 99))
#     self.window.after(1000, self.plzplz)
#
# ad(self)
















# import tkinter as tk
#
# import time
#
#
# class Clock():
#     def __init__(self):
#         self.root = tk.Tk()
#         self.label = tk.Label(text="", font=('Helvetica', 48), fg='red')
#         self.label.pack()
#         self.update_clock()
#         self.root.mainloop()
#
#     def update_clock(self):
#         now = time.strftime("%H:%M:%S")
#         self.label.configure(text=now)
#         self.root.after(1000, self.update_clock)
#
#
# app = Clock()



# window.mainloop()




"""# def showLabel():
#     label = tkinter.Label(window, text=random.randint(1, 99), font=("Courier", 80), height=10)
#     label.pack()
# 
# 
# window.after(2000,showLabel())"""


#
#
# for i in range(3):
#     label = tkinter.Label(window, text=random.randint(1, 99), font=("Courier", 80), height=10)
#     # label.pack()
#     window.after(2000,showLabel(label))
# label을 띄워주고 2초 후에 지워줘 그리고 다시 띄워주고 2초후에 지워주는 것을 반복해야하는게 아닌가?

# def plz(a):
#     a.pack_forget
#     a.pack()
#     return
#     window.after(1000, plz())
#
# for i in range(3):
#     a = tkinter.Label(window, text=random.randint(1, 99), font=("Courier", 80), height=10)
#     plz(a)


# def Text_Funtion(masterss,Text1):
#     tkinter.Label(master=masterss,text=Text1).pack()
#
# def Label_Funtion(Where,What_Text,Font_Size,Height):
#     tkinter.Label(master=Where, text=What_Text, font=Font_Size, height=Height).pack
#
# Label_Funtion(window,"안녕",10,10)
#
# window.mainloop()
# def clearTextInput():
#     plztext.delete("1.0","end")
#
# plztext = tkinter.Text(window)
# plztext.pack()
# plztext.insert("1.0",random.randint(1,99))
#
# btnRead=tkinter.Button(window, height=1, width=10, text="Clear",
#                     command=clearTextInput)
# btnRead.pack()





# for i in range(3):
#     print(random.randint(1, 99))


