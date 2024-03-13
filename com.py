from tkinter import *
from tkinter import messagebox
import base64
from turtle import Screen
from PIL import Image,ImageTk
def decrypt():
    password=code.get()
    if password=='1234':
        screen2=Toplevel(screen5)
        screen2.title('decryption')
        screen2.geometry('400x200')
        screen2.configure(bg='#00bd56')
        message=text1.get(1.0,END)
        decode1=message.encode('ascii')
        base64_bytes=base64.b64decode(decode1)
        decrypt1=base64_bytes.decode('ascii')
        Label(screen2,text='decrypt',font=('arial',20),fg='white',bg='#00bd56').place(x=10,y=0)
        text2=Text(screen2,font=('robote',10),bg='white',relief=RIDGE,wrap=WORD,bd=10)
        text2.place(x=10,y=50,width=380,height=150)
        text2.insert(END,decrypt1)
    elif password=='':
        messagebox.showerror('decryption','input password')
    elif password!='1234':
        messagebox.showerror('decryption','invalid password')
            
def encrypt():
    password=code.get()
    if password=='1234':
        screen1=Toplevel(screen5)
        screen1.geometry('400x200')
        screen1.configure(bg='#ed3833')
        message=text1.get(1.0,END)
        encode1=message.encode('ascii')
        base64_bytes=base64.b64encode(encode1)
        encrypt1=base64_bytes.decode('ascii')
        Label(screen1,text='Encrypt',font=('arial',20),fg='white',bg='#ed3833').place(x=10,y=10)
        text2=Text(screen1,font='robote 10',bg='white',relief=GROOVE,wrap=WORD,bd=10)
        text2.place(x=10,y=50,width=380,height=150)
        text2.insert(END,encrypt1)
    elif password=='':
        messagebox.showerror('encryption','input password')
    elif password!='1234':
        messagebox.showerror('encryption','invalid password')

    
    
def main_screen():
    global screen5
    global code
    global text1
    screen5=Tk()
    screen5.geometry('900x700')
    image_icon=ImageTk.PhotoImage(file=r"./demo.png")
    screen5.iconphoto(False,image_icon)
    screen5.title('pctapp')
    def reset():
        code.set('')
        text1.delete(1.0,END)
    
    
    r= Label(bd=10,relief=RIDGE,text='enter text for encryption and decryption',fg='yellow',bg='black',font=('calbri',40))
    r.place(x=250,y=80)
    text1=Text(font='Robete 20',bg='white',relief=GROOVE,wrap=WORD,bd=5)
    text1.place(x=450,y=200,width=355,height=100)
    Label(bd=5,text='enter secret key for encryption decryption',fg='pink',bg='black',font=('calibri',23)).place(x=350,y=340)
    code=StringVar()
    Entry(textvariable=code,width=19,bd=5,font=('arial',25),show='*').place(x=450,y=400)
    Button(text='ENCRYPT',height='4',width=23,bg='#ed3833',fg='white',bd=0,command=encrypt).place(x=450,y=500)
    r3=Button(text='DECRYPT',height='4',width=23,bg='#00bd56',fg='white',bd=0,command=decrypt)      
    r3.place(x=620,y=500)
    r2=Button(text='RESET',height='4',width=50,bg='plum',fg='white',bd=0,command=reset)
    r2.place(x=440,y=580)

    
    screen5.mainloop()

main_screen()


