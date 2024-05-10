import customtkinter as ctk
from PIL import Image
from subprocess import call
import database

db = database.buat_koneksi()

base = ctk.CTk(fg_color='#142339')
base.geometry('400x500')
base.title('Login Page')
base.resizable(0,0)

loginframe = ctk.CTkFrame(
    base,
    fg_color='#446493',
)
loginframe.place(relx=0.5,rely=0.5,relwidth=0.8,relheight=0.8,anchor='center')
loginframe.columnconfigure((0,1),weight=1)
loginframe.rowconfigure((0,1,2,3,4,5),weight=1)

logintext=ctk.CTkLabel(
    loginframe,
    text='Welcome To SEA Demo App',
    font=(('Poppins Bold',16)),
    text_color='white'
)
logintext.grid(row=1,column=0,columnspan=2)

usernameicon = ctk.CTkLabel(
    loginframe,
    text='',
    image=ctk.CTkImage(Image.open('user-svgrepo-com.png'))
)
usernameicon.grid(row=2,column=0,sticky='e',padx=(0,10))

username = ctk.StringVar()
usernameform=ctk.CTkEntry(
    loginframe,
    text_color='black',
    placeholder_text='Username',
    fg_color='#F4F8FF',
    width=200,
    height=40,
    textvariable=username
)
usernameform.grid(row=2,column=1,sticky='w')

passwordicon = ctk.CTkLabel(
    loginframe,
    text='',
    image=ctk.CTkImage(Image.open('password-svgrepo-com.png'))
)
passwordicon.grid(row=3,column=0,sticky='e',padx=(0,10))

password=ctk.StringVar()
passwordform=ctk.CTkEntry(
    loginframe,
    text_color='black',
    placeholder_text='Password',
    fg_color='#F4F8FF',
    width=200,
    height=40,
    textvariable=password
)
passwordform.grid(row=3,column=1,sticky='w')

def submit():
    if any(username.get() == b for a,b,c,d in database.baca_data(db)) and any(password.get() == d for a,b,c,d in database.baca_data(db)):
        base.destroy()
        call(["python","mainapps.py"])

    else :
        passwordform.delete(0,len(password.get()))
        usernameform.delete(0,len(username.get()))
    

loginbutton = ctk.CTkButton(
    loginframe,
    text='Login',
    font=(('Poppins',12)),
    fg_color='#202E44',
    command=submit
)
loginbutton.grid(row=4,column=0,columnspan=2)

def daftar():
    base.destroy()
    call(['python','register.py'])

register = ctk.CTkButton(
    loginframe,
    text="Don't have account?",
    fg_color='transparent',
    command=daftar
)
register.grid(row=5,column=0,columnspan=2,sticky='n')
base.mainloop()