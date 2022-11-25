from tkinter import*


window=Tk()
#상단 라벨 생성
l1= Label(window,text="이름")
l2= Label(window,text="직업")
l3= Label(window,text="국적")


#격자배열을 통해 1행에 배치
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)


#입력부분 생성
e1=Entry(window)
e2=Entry(window)
e3=Entry(window)


#격자배열을 통해 2행에 배치
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)


#하단 버튼 생성
b1=Button(window,text="Show")
b2=Button(window,text="Quit")


#격자배열을 통해 3열에 배치
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)


window.mainloop()
