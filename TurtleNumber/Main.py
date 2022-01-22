import tkinter
import random


window = tkinter.Tk()

def Label_Funtion(Where, What_Text, Font_Size, Height):
    tkinter.Label(master=Where, text=What_Text, font=("Courier", Font_Size), height=Height).pack()
def Button_Funtion(Where, What_Text, Command):
    tkinter.Button(master=Where, text=What_Text, command=Command).pack()


def Count_Number_Window():
    newWindow = tkinter.Toplevel(window)
    newWindow.geometry("500x300")
    Label_Funtion(newWindow, "몇 개의 숫자로 진행하시겠습니까?", 10, 10)
    text1 = tkinter.Text(newWindow, height=1.45, width=40)
    text1.place(x=100, y=100)

    def Start():
        global result
        result = text1.get("1.0", "end")
        newWindow.destroy()
        window.destroy()
        Game_Window()  # 게임 하는 함수 window 만들어서 여기다가 추가 해줘
        return result

    Button_Funtion(newWindow, "Ok", Start)
    Button_Funtion(newWindow, "Cancel", newWindow.destroy)


def MainWindow():
    window.title("숫자 기억 게임")
    window.geometry("1000x700+100+100")  # ("너비*높이+x좌표+y좌표")
    window.resizable(1, 1)
    Label_Funtion(window, "숫자 기억하기 게임을 시작합니다.", 30, 10)
    Button_Funtion(window, "게임 시작", Count_Number_Window)
    window.mainloop()

class Tool():
    def __init__(self):
        self.window=tkinter.Tk()
        self.window.geometry("1000x700+100+100")
        self.label = tkinter.Label(text="", font=('Courier', 80), fg='black')
        self.label.pack()
        self.plzplz()
        self.window.mainloop()
    def plzplz(self):
        self.label.configure(text=random.randint(1, 99))
        self.window.after(1000,self.plzplz)





def Game_Window():
    app = Tool()

    # for i in range(int(result)):
    #
    #     gameWindow = tkinter.Tk()
    #     gameWindow.title("숫자 기억 게임")
    #     gameWindow.geometry("1000x700+100+100")
    #     gameWindow.resizable(1, 1)
    #     print("plz")
    #     a = tkinter.Label(gameWindow, random.randint(1,99), font=("Courier", 80), height=10)
    #     a.pack()
    #     a.pack_forget()
        # Label_Funtion(gameWindow,random.randint(1,99), 80, 10)
        # time.sleep(3)
        # gameWindow.destroy()
        # plztext = tkinter.Text(gameWindow, height=10)
        # plztext.pack()
        # plztext.delete("1.0", "end")
        # Label_Funtion(gameWindow,random.randint(1,99), 80, 10)
        # time.sleep(1)
        # gameWindow.configure(bg="white")
        # time.sleep(1)
        # plztext.insert("1.0",random.randint(1,99))







MainWindow()
