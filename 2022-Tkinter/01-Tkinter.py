import tkinter
from tkinter import messagebox

price = 0

"""----------------label, button 함수----------------"""


def Label_Funtion(Where, What_Text, Font_Size, Height):
    tkinter.Label(master=Where, text=What_Text, font=("Courier", Font_Size), height=Height).pack()


def Button_Funtion(Where, What_Text, Height, Font_Size, Command, Fill, Expand, Side, Anchor):
    tkinter.Button(master=Where, text=What_Text, height=Height, font=Font_Size, command=Command).pack(fill=Fill,
                                                                                                        expand=Expand,
                                                                                                        side=Side,
                                                                                                        anchor=Anchor)


"""----------------이미지 버튼 함수--------------------"""


def IceAmericano():
    global price
    price += 1500
    print("아이스 아메리카노", price)
    tkinter.Label(master=SecondWindow, text=price, font=("Courier", 10), width=5, height=5).place(x=50, y=565)
    return price

def DolceLatte():
    global price
    price += 3000
    print("스타벅스 돌체 라떼", price)
    tkinter.Label(master=SecondWindow, text=price, font=("Courier", 10), width=5, height=5).place(x=50, y=565)
    return price

def Espresso():
    global price
    price += 3500
    print("에스프레소", price)
    tkinter.Label(master=SecondWindow, text=price, font=("Courier", 10), width=5, height=5).place(x=50, y=565)
    return price

def JavaChipFrappuccino():
    global price
    price += 2000
    print("자바 칩 프라푸치노", price)
    tkinter.Label(master=SecondWindow, text=price, font=("Courier", 10), width=5, height=5).place(x=50, y=565)
    return price

def CaramelMacchiato():
    global price
    price += 5500
    print("카라멜 마끼아또", price)
    tkinter.Label(master=SecondWindow, text=price, font=("Courier", 10), width=5, height=5).place(x=50, y=565)
    return price

def IceCafeLatte():
    global price
    price += 4500
    print("아이스 카페 라떼", price)
    tkinter.Label(master=SecondWindow, text=price, font=("Courier", 10), width=5, height=5).place(x=50, y=565)
    return price

def CafeMocha():
    global price
    price += 4000
    print("카페 모카", price)
    tkinter.Label(master=SecondWindow, text=price, font=("Courier", 10), width=5, height=5).place(x=50, y=565)
    return price

def Cappuccino():
    global price
    price += 5000
    print("카푸치노", price)
    tkinter.Label(master=SecondWindow, text=price, font=("Courier", 10), width=5, height=5).place(x=50, y=565)
    return price

def ColdBrew():
    global price
    price += 5500
    print("콜드브루", price)
    tkinter.Label(master=SecondWindow, text=price, font=("Courier", 10), width=5, height=5).place(x=50, y=565)
    return price

def StrawberryYogurt():
    global price
    price += 7000
    print("딸기 딜라이트 요거트 블랜디드", price)
    tkinter.Label(master=SecondWindow, text=price, font=("Courier", 10), width=5, height=5).place(x=50, y=565)
    return price

def PeachLemonBlended():
    global price
    price += 6500
    print("피치 & 레몬 블렌디드", price)
    tkinter.Label(master=SecondWindow, text=price, font=("Courier", 10), width=5, height=5).place(x=50, y=565)
    return price

def WhiteTigerFrappuccino():
    global price
    price += 7000
    print("화이트 타이거 프라푸치노", price)
    tkinter.Label(master=SecondWindow, text=price, font=("Courier", 10), width=5, height=5).place(x=50, y=565)
    return price


"""----------------실행 함수--------------------------"""


def money():
    def plz():
        global result, price
        result = text1.get("1.0", "end-1c")
        change = int(result) - int(price)
        if change < 0:
            MsgBox = messagebox.askquestion("Ask Retry", "금액이 부족합니다.\n금액을 다시 입력하시겠습니까?")
            if MsgBox == "yes":
                text1.delete("1.0", "end")
            else:
                MsgBox1 = messagebox.askquestion("Ask Retry", "다시 주문하시겠습니까?")
                if MsgBox1 == "yes":
                    price = 0
                    ThirdWindow.destroy()
                    Order()
                else:
                    ThirdWindow.destroy()
        else:
            tkinter.Label(master=ThirdWindow, text="이용해주셔서 감사합니다\n주문하신 메뉴 곧 준비해드리겠습니다.\n거스름돈 " + str(change) + "원 입니다!",
                          height=100, font=("Courier", 15)).pack()
        return result, change, price

    SecondWindow.destroy()
    ThirdWindow = tkinter.Tk()
    ThirdWindow.title("2022-Tkinter")
    ThirdWindow.geometry("400x580+100+100")

    text1 = tkinter.Text(ThirdWindow, height=3, width=40)
    text1.pack()

    a = tkinter.Button(master=ThirdWindow, text="결제", font=30, command=plz)
    a.place(x=345,y=17)


def reset():
    global price
    price = 0
    SecondWindow.destroy()
    Order()
    return price


def Order():
    global SecondWindow
    """firstwindow를 꺼줘야 secondwindow에서 mainloop의 영향을 받지 않고 
       이미지를 가져올 수 있어서 firstwindow.destroy를 해주는데 메뉴 초기화를 시키면
       켜져있는 firstwindow가 없는데 destory를 시켜주라고 하니 오류가 발생하여
       try except를 사용해주었다."""
    try:
        FirstWindow.destroy()
    except tkinter.TclError:
        pass

    SecondWindow = tkinter.Tk()
    SecondWindow.geometry("410x700+100+100")

    frame = tkinter.Frame(SecondWindow)
    frame.grid(row=0, column=0)

    """----------------이미지 버튼----------------"""
    # 0행
    photo1 = tkinter.PhotoImage(file="sampleImage2.png")
    btn = tkinter.Button(frame, image=photo1, width=130, height=130, command=IceAmericano)
    btn.grid(row=0, column=0)

    photo2 = tkinter.PhotoImage(file="sampleImage1.png")
    btn = tkinter.Button(frame, image=photo2, width=130, height=130, command=DolceLatte)
    btn.grid(row=0, column=1)

    photo3 = tkinter.PhotoImage(file="sampleImage3.png")
    btn = tkinter.Button(frame, image=photo3, width=130, height=130, command=Espresso)
    btn.grid(row=0, column=2)

    # 1행
    photo4 = tkinter.PhotoImage(file="sampleImage4.png")
    btn = tkinter.Button(frame, image=photo4, width=130, height=130, command=JavaChipFrappuccino)
    btn.grid(row=1, column=0)

    photo5 = tkinter.PhotoImage(file="sampleImage5.png")
    btn = tkinter.Button(frame, image=photo5, width=130, height=130, command=CaramelMacchiato)
    btn.grid(row=1, column=1)

    photo6 = tkinter.PhotoImage(file="sampleImage6.png")
    btn = tkinter.Button(frame, image=photo6, width=130, height=130, command=IceCafeLatte)
    btn.grid(row=1, column=2)

    # 2행
    photo7 = tkinter.PhotoImage(file="sampleImage7.png")
    btn = tkinter.Button(frame, image=photo7, width=130, height=130, command=CafeMocha)
    btn.grid(row=2, column=0)

    photo8 = tkinter.PhotoImage(file="sampleImage8.png")
    btn = tkinter.Button(frame, image=photo8, width=130, height=130, command=Cappuccino)
    btn.grid(row=2, column=1)

    photo9 = tkinter.PhotoImage(file="sampleImage9.png")
    btn = tkinter.Button(frame, image=photo9, width=130, height=130, command=ColdBrew)
    btn.grid(row=2, column=2)

    # 3행
    photo10 = tkinter.PhotoImage(file="sampleImage10.png")
    btn = tkinter.Button(frame, image=photo10, width=130, height=130, command=StrawberryYogurt)
    btn.grid(row=3, column=0)

    photo11 = tkinter.PhotoImage(file="sampleImage11.png")
    btn = tkinter.Button(frame, image=photo11, width=130, height=130, command=PeachLemonBlended)
    btn.grid(row=3, column=1)

    photo12 = tkinter.PhotoImage(file="sampleImage12.png")
    btn = tkinter.Button(frame, image=photo12, width=130, height=130, command=WhiteTigerFrappuccino)
    btn.grid(row=3, column=2)

    # 추가 버튼
    payment = tkinter.Button(SecondWindow, text="계산", width=27, height=4, command=money)
    payment.place(x=210, y=550)

    Cancel = tkinter.Button(SecondWindow, text="취소", width=27, height=4, command=reset)
    Cancel.place(x=210, y=625)

    SecondWindow.mainloop()


"""----------------처음 화면 설정----------------------"""
FirstWindow = tkinter.Tk()
FirstWindow.title("2022-Tkinter")
FirstWindow.geometry("400x580+100+100")

# 이미지 추가
wall = tkinter.PhotoImage(file="starbucks.png")
wall_label = tkinter.Label(FirstWindow, image=wall)
wall_label.place(x=0, y=0)

# 처음 화면 버튼
Button_Funtion(FirstWindow, "매장", 7, 20, Order, "x", 1, "left", "sw")
Button_Funtion(FirstWindow, "포장", 7, 20, Order, "x", 1, "right", "se")

FirstWindow.mainloop()