import tkinter as tk
flag=0
root=tk.Tk()
root.title("Calculator")
CurrentShow=tk.StringVar()
CurrentShow.set('0')
def ground():
    
    root.minsize(400,465)
    w=tk.Label(root,width=26,textvariable=CurrentShow,bg='black',anchor='e',bd=16,fg='white',font=('楷体',20))
    w.place(x=20,y=0,width=100,height=100)
    w.pack()
    button1_1=tk.Button(text="+",bg='#666',command=lambda:push('+'),bd=5,font=('楷体',30))
    button1_1.place(x=0,y=65,width=100,height=100)
    button1_2=tk.Button(text="-",bg='#666',command=lambda:push('-'),bd=5,font=('楷体',30))
    button1_2.place(x=100,y=65,width=100,height=100)
    button1_3=tk.Button(text="X",bg='#666',command=lambda:push('X'),bd=5,font=('楷体',30))
    button1_3.place(x=200,y=65,width=100,height=100)
    button1_4=tk.Button(text="/",bg='#666',command=lambda:push('/'),bd=5,font=('楷体',30))
    button1_4.place(x=300,y=65,width=100,height=100)
    button2_1=tk.Button(text="9",bg='#666',command=lambda:push('9'),bd=5,font=('楷体',30))
    button2_1.place(x=0,y=165,width=100,height=100)
    button2_2=tk.Button(text="8",bg='#666',command=lambda:push('8'),bd=5,font=('楷体',30))
    button2_2.place(x=100,y=165,width=100,height=100)
    button2_3=tk.Button(text="7",bg='#666',command=lambda:push('7'),bd=5,font=('楷体',30))
    button2_3.place(x=200,y=165,width=100,height=100)
    button3_1=tk.Button(text="6",bg='#666',bd=5,command=lambda:push('6'),font=('楷体',30))
    button3_1.place(x=0,y=265,width=100,height=100)
    button3_2=tk.Button(text="5",bg='#666',bd=5,command=lambda:push('5'),font=('楷体',30))
    button3_2.place(x=100,y=265,width=100,height=100)
    button3_3=tk.Button(text="4",bg='#666',bd=5,command=lambda:push('4'),font=('楷体',30))
    button3_3.place(x=200,y=265,width=100,height=100)
    button4_1=tk.Button(text="3",bg='#666',bd=5,command=lambda:push('3'),font=('楷体',30))
    button4_1.place(x=0,y=365,width=100,height=100)
    button4_2=tk.Button(text="2",bg='#666',bd=5,command=lambda:push('2'),font=('楷体',30))
    button4_2.place(x=100,y=365,width=100,height=100)
    button4_3=tk.Button(text="1",bg='#666',bd=5,command=lambda:push('1'),font=('楷体',30))
    button4_3.place(x=200,y=365,width=100,height=100)
    button4_4=tk.Button(text="C",bg='#666',bd=5,command=lambda:push('C'),font=('楷体',30))
    button4_4.place(x=300,y=165,width=100,height=150)
    button4_4=tk.Button(text="=",bg='#666',bd=5,command=lambda:push('='),font=('楷体',30))
    button4_4.place(x=300,y=315,width=100,height=150)
    root.mainloop()
def push(m):
    global keydown
    if (CurrentShow.get()== '0'):
        CurrentShow.set(m)
    else:
        CurrentShow.set(CurrentShow.get()+m)
    if (m =='C'):
        CurrentShow.set('0')
    if(m=="="):
        s=str(CurrentShow.get())
        a=list(s)
        stack=[]
        sign='+'
        num=0
        while len(a)>0:
            b=a.pop(0)
            c=str(b)
            if c.isdigit():
                    num=10*num+int(c)  
            if(not c.isdigit() or len(a)==0):
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == 'X':
                    stack[-1]=stack[-1]*num
                elif sign == '/':
                    stack[-1]=int(stack[-1]/float(num))
                num =0
                sign=c
        top=str(sum(stack))
        CurrentShow.set(CurrentShow.get()+top)

if __name__ == "__main__":
    ground()
