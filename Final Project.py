import tkinter as tk
from tkinter import *
from random import random
from tkinter import messagebox, END
import random
import mysql.connector



from PIL import ImageTk, Image

current_balance = 0.0


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.shared_data = {'Balance': tk.IntVar()}

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, Menu, Withdraw, Deposit, InfoPage, Balance):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#ffb6f9')
        self.controller = controller

        self.controller.title("Scam Banker")
        self.controller.state("zoomed")
        self.controller.iconphoto(False, tk.PhotoImage(file='abc.png'))
        heading_Label = tk.Label(self, text="Scam Banker ATM", foreground='#7e7efd',
                                 font=('comic two', 45, 'bold'), background='purple')
        heading_Label.pack(pady=25)

        Space_label = tk.Label(self, height=4, bg='#ffb6f9')
        Space_label.pack()
        pin_label = tk.Label(self, text=f'Welcome {user_display_name} to Scam Banker', font=('ariel', 20),
                             bg='#ffb6f9'
                             , fg='white')
        pin_label.pack(pady=10)

        def next_page():
            controller.show_frame('MenuPage')

        entry_button = tk.Button(self, text='Enter', font=('orbitron', 12), command=next_page, relief='raised',
                                 borderwidth=3, width=23, height=3)
        entry_button.pack(pady=10)

        def Quit():
            self.controller.destroy()

        def popup():
            response = messagebox.askyesno('Exit', 'Do you want to Quit?')

            if response == 1:
                return Quit()
            else:
                return

        quit1 = tk.Button(self, text='Quit', font=('orbitron', 12), command=popup, relief='raised', borderwidth=3,
                          width=23, height=3)
        quit1.pack(pady=10)

        dualtone_label = tk.Label(self, text='', font=('orbitron', 13), fg='white', bg='#33334d', anchor='n')
        dualtone_label.pack(fill='both', expand='True')

        def changescreen():
            self.controller.destroy()
            main_screen()

        def popup2():
            response = messagebox.askyesno('Exit', 'Do you want to use another account?')

            if response == 1:
                return changescreen()
            else:
                return

        register_login_screen = tk.Button(dualtone_label, text='Use another account', font=('orbitron', 12),
                                          command=popup2, relief='raised', borderwidth=3, width=23, height=3)
        register_login_screen.pack(pady=10, padx=10, side='bottom', anchor='e')


class Menu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffb6f9")
        self.controller = controller

        heading_Label = tk.Label(self, text="Scam Banker ATM", foreground='#7e7efd',
                                 font=('comic two', 45, 'bold'), background='#ffb6f9')
        heading_Label.pack(pady=25)

        main_menu_label = tk.Label(self, text='Main Menu', font=('ariel', 13), fg="white", bg='purple')
        main_menu_label.pack()
        selection_label = tk.Label(self, text='Please Choose a service below',
                                   font=('ariel', 13), fg='white', bg='#ffb6f9', anchor='c')
        selection_label.pack(fill='x')

        button_frame = tk.Frame(self, bg='black')
        button_frame.pack(fill='both', expand=True)

        def withdraw():
            controller.show_frame('Withdraw')

        withdraw_button = tk.Button(button_frame, text='Withdraw',
                                    command=withdraw,
                                    relief='raised',
                                    borderwidth=3,
                                    width=50,
                                    height=5)
        withdraw_button.grid(row=0, column=0, pady=5, padx=200)

        def deposit():
            controller.show_frame('Deposit')

        deposit_button = tk.Button(button_frame,
                                   text='Deposit',
                                   command=deposit,
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   height=5)
        deposit_button.grid(row=1, column=0, pady=10, padx=10)

        def balance():
            controller.show_frame('Balance')

        balance_button = tk.Button(button_frame,
                                   text='Balance',
                                   command=balance,
                                   relief='raised',
                                   borderwidth=3,
                                   width=50,
                                   height=5)
        balance_button.grid(row=0, column=1, pady=5)

        def info():
            controller.show_frame('InfoPage')

        info_button = tk.Button(button_frame, text='Personal Info', font=('orbitron', 13), command=info,
                                relief='raised', borderwidth=3, width=30, height=4)
        info_button.grid(row=2, column=0, pady=5)

        def exit():
            controller.show_frame('StartPage')

        exit_button = tk.Button(button_frame,
                                text='Exit',
                                command=exit,
                                relief='raised',
                                borderwidth=3,
                                width=50,
                                height=5)
        exit_button.grid(row=1, column=1, pady=5)


class Withdraw(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffb6f9")
        self.controller = controller

        heading_Label = tk.Label(self, text="Scam Banker ATM", foreground='#7e7efd',
                                 font=('comic two', 45, 'bold'), background='#ffb6f9')
        heading_Label.pack(pady=25)

        choose_amount_label = tk.Label(self,
                                       text='Choose the amount you want to withdraw',
                                       font=('orbitron', 13),
                                       fg='white',
                                       bg='#ffb6f9')
        choose_amount_label.pack()

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both', expand=True)

        def withdraw(amount):
            global current_balance
            if amount > current_balance:
                messagebox.showwarning(" Not Enough Funds")
                other_amount_entry.delete(0, END)
            else:
                current_balance -= amount
                messagebox.showinfo("Transaction Complete")
                other_amount_entry.delete(0, END)
                controller.shared_data['Balance'].set(current_balance)
                DataBase = mysql.connector.connect(host="localhost", user="root", password='Ilovetocode@123')
                curr = DataBase.cursor()
                curr.execute("use scambanker")
                curr.execute(f"update scambanker set balance ={current_balance} where accid ={username1}")
                DataBase.commit()
                controller.show_frame("Menu")

        twenty_button = tk.Button(button_frame, text='$20', font=('orbitron', 12), command=lambda: withdraw(20),
                                  relief='raised', borderwidth=3, width=30, height=4)
        twenty_button.grid(row=0, column=0, pady=5)

        fourty_button = tk.Button(button_frame, text='$40', font=('orbitron', 12), command=lambda: withdraw(40),
                                  relief='raised', borderwidth=3, width=30, height=4)
        fourty_button.grid(row=1, column=0, pady=5)

        sixty_button = tk.Button(button_frame, text='$60', font=('orbitron', 12), command=lambda: withdraw(60),
                                 relief='raised', borderwidth=3, width=30, height=4)
        sixty_button.grid(row=2, column=0, pady=5)

        eighty_button = tk.Button(button_frame, text='$80', font=('orbitron', 12), command=lambda: withdraw(80),
                                  relief='raised', borderwidth=3, width=30, height=4)
        eighty_button.grid(row=3, column=0, pady=5)

        one_hundred_button = tk.Button(button_frame, text='$100', font=('orbitron', 12), command=lambda: withdraw(100),
                                       relief='raised', borderwidth=3, width=30, height=4)
        one_hundred_button.grid(row=0, column=1, pady=5, padx=794)

        two_hundred_button = tk.Button(button_frame, text='$200', font=('orbitron', 12), command=lambda: withdraw(200),
                                       relief='raised', borderwidth=3, width=30, height=4)
        two_hundred_button.grid(row=1, column=1, pady=5)

        three_hundred_button = tk.Button(button_frame, text='$300', font=('orbitron', 12),
                                         command=lambda: withdraw(300), relief='raised', borderwidth=3, width=30,
                                         height=4)
        three_hundred_button.grid(row=2, column=1, pady=5)

        cash = tk.StringVar()
        other_amount_entry = tk.Entry(button_frame, font=('orbitron', 12), textvariable=cash, width=28, justify='right')
        other_amount_entry.grid(row=3, column=1, pady=4, ipady=30)

        other_amount_heading = tk.Button(button_frame, text='Other amount in dollars', font=('orbitron', 13),
                                         borderwidth=0, relief='sunken', activeforeground='white',
                                         activebackground='#33334d', bg='#33334d', fg='white')
        other_amount_heading.grid(row=4, column=1)

        def other_amount(_):
            global current_balance
            try:
                val = int(cash.get())

                if int(cash.get()) > current_balance:
                    messagebox.showwarning('WARNING', 'Not sufficient funds!')
                    other_amount_entry.delete(0, END)
                elif int(cash.get()) < 0:
                    messagebox.showwarning('WARNING', 'Invalid Input!')
                    other_amount_entry.delete(0, END)
                else:

                    current_balance -= int(cash.get())
                    controller.shared_data['Balance'].set(current_balance)
                    cash.set('')
                    messagebox.showinfo('TRANSACTION', 'Done Successfully!')
                    controller.show_frame('Menu')
                    DataBase = mysql.connector.connect(host="localhost", user="root", password='Ilovetocode@123')
                    curr = DataBase.cursor()
                    curr.execute("use scambanker")
                    curr.execute(f"update scambanker set balance ={current_balance} where accid ={username1}")
                    DataBase.commit()


            except ValueError:
                messagebox.showwarning('WARNING', 'Invadlid Input!')
                cash.set('')

        other_amount_entry.bind('<Return>', other_amount)


class Deposit(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffb6f9")
        self.controller = controller

        heading_Label = tk.Label(self, text="Scam Banker ATM", foreground='#7e7efd',
                                 font=('comic two', 45, 'bold'), background='#ffb6f9')
        heading_Label.pack(pady=25)

        enter_amount_label = tk.Label(self, text='Enter amount', font=('Ariel', 13),
                                      bg='#ffb6f9',
                                      fg='white')
        enter_amount_label.pack(pady=10)

        cash = tk.StringVar()
        deposit_entry = tk.Entry(self,
                                 textvariable=cash,
                                 font=('orbitron', 12),
                                 width=22)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            try:
                val = int(cash.get())
                if int(val) < 0:
                    messagebox.showwarning('WARNING', 'Improper Amount Entered!')
                    cash.set('')
                else:
                    current_balance += int(val)
                    messagebox.showinfo('DEPOSITION', 'Done Successfully!')
                    controller.shared_data['Balance'].set(current_balance)
                    controller.show_frame('Menu')
                    cash.set('')
                    DataBase = mysql.connector.connect(host="localhost", user="root", password='Ilovetocode@123')
                    curr = DataBase.cursor()
                    curr.execute("use scambanker")
                    curr.execute(f"update scambanker set balance ={current_balance} where accid ={username1}")
                    DataBase.commit()

            except ValueError:
                messagebox.showwarning('WARNING', 'Invadlid Input!')
                cash.set('')

        enter_button = tk.Button(self, text='Enter',
                                     command=deposit_cash,
                                     relief='raised',
                                     borderwidth=3,
                                     width=40,
                                     height=3)
        enter_button.pack(pady=10)

        two_tone_label = tk.Label(self, bg='black')
        two_tone_label.pack(fill='both', expand=True)


class Balance(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffb6f9")
        self.controller = controller
        heading_Label = tk.Label(self, text="Scam Banker ATM", foreground='#7e7efd',
                                 font=('comic two', 45, 'bold'), background='#ffb6f9')
        heading_Label.pack(pady=25)
        self.balance_var = tk.StringVar()
        controller.shared_data['Balance'].trace('w', self.on_balance_changed)
        controller.shared_data['Balance'].set(current_balance)

        balance_label = tk.Label(self, text='Balance', font=('orbitron', 13), fg='white', bg='#3d3d5c', anchor='w')
        balance_label.pack()

        upperframe = tk.Frame(self, bg='black')
        upperframe.pack(fill='both', expand='True')

        balance_label = tk.Label(upperframe, textvariable=self.balance_var, font=('orbitron', 16), fg='white',
                                 bg='#33334d', anchor='w')
        balance_label.pack(pady=7)

        button_frame = tk.Label(self, bg='#33334d')
        button_frame.pack(fill='both')

        def menu():
            controller.show_frame('Menu')

        menu_button = tk.Button(button_frame, command=menu, text='Menu', font=('orbitron', 13), relief='raised',
                                borderwidth=3, width=23, height=4)
        menu_button.pack(pady=10)

        def exit():
            controller.show_frame('Start')

        exit_button = tk.Button(button_frame, text='Exit', command=exit, font=('orbitron', 13), relief='raised',
                                borderwidth=3, width=23, height=4)
        exit_button.pack(pady=5)

    def on_balance_changed(self, *args):
        self.balance_var.set('Current Balance: $' + str(self.controller.shared_data['Balance'].get()))


class InfoPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#ffb6f9")
        self.controller = controller
        heading_Label = tk.Label(self, text="Scam Banker ATM", foreground='#7e7efd',
                                 font=('ariel', 45, 'bold'), background='#ffb6f9')
        heading_Label.pack(pady=25)

        main_menu_label = tk.Label(self, text='Personal Info', font=('Ariel', 13), fg='white', bg='black')
        main_menu_label.pack(pady=5)

        upperframe = tk.Frame(self, bg='#33334d')
        upperframe.pack(fill='both', expand='True')

        button_frame = tk.Frame(self, bg='#33334d')
        button_frame.pack(fill='both')
        DataBase = mysql.connector.connect(host="localhost", user="root", password='Ilovetocode@123')
        curr = DataBase.cursor()
        curr.execute("use scambanker")
        curr.execute("create database if not exist scambanker")
        curr.execute(f"select password from scambanker where accid = {username1} ")
        DataBase.commit()

        pin_code = curr.fetchone()
        pin_code_read = ''
        for i in pin_code:
            pin_code_read += i

        name_info = tk.Label(upperframe, text=f'Name : {user_display_name}', font=('orbitron', 16), fg='white',
                             bg='#33334d')
        name_info.pack(pady=5)

        accid_info = tk.Label(upperframe, text=f'Account No. : {username1}', font=('orbitron', 16), fg='white',
                              bg='#33334d')
        accid_info.pack(pady=5)

        pin_info = tk.Label(upperframe, text=f'Pin : {pin_code_read}', font=('orbitron', 16), fg='white', bg='#33334d')
        pin_info.pack(pady=5)

        def exit():
            controller.show_frame('MenuPage')

        exit_button = tk.Button(button_frame, text='Menu', command=exit, font=('orbitron', 13), relief='raised',
                                borderwidth=3, width=23, height=4)
        exit_button.pack(pady=20, padx=10)
def abcd():
    app = SampleApp()
    app.mainloop()


########## REGISTER/LOGIN #####


def password_not_recognised():
    messagebox.showwarning('WARNING', 'Invalid Password!')


##### WARNING_SCREEN ###
def user_not_found():
    messagebox.showwarning('WARNING', 'No AccountID Found !')


######REGISTER USER SCREEN #######
def register_user():
    global username_info
    username_info = str(rand)
    password_info = password.get()
    name_info = name.get()

    ################## MYSQL DATABASE ##################
    global curr
    DataBase = mysql.connector.connect(host="localhost", user="root", password='Ilovetocode@123')
    curr = DataBase.cursor()
    curr.execute("create database if not exists scambanker")
    curr.execute("use scambanker")
    curr.execute(
        "create table if not exists scambanker(accid int(10) primary key,name varchar(30),password char(20),"
        "balance char(30))")
    DataBase.commit()

    curr.execute('select accid from scambanker')
    values = curr.fetchall()

    b = []
    for i in values:
        b.append(i[0])
    if username_info in b:
        messagebox.showwarning('WARNING', 'AccountID already exists!')

        password_entry.delete(0, END)
        name_entry.delete(0, END)
    elif name_info == '':
        messagebox.showwarning('WARNING', 'No Name Given!')
        password_entry.delete(0, END)
    elif password_info == '':
        messagebox.showwarning('WARNING', 'No Password Given!')
    else:
        balance_inti = '0.00'
        password_entry.delete(0, END)
        name_entry.delete(0, END)
        screen1.destroy()
        curr.execute(
            "insert into scambanker values('" + username_info + "','" + name_info + "','" + password_info + "','" + balance_inti + "')")
        DataBase.commit()
        messagebox.showinfo('Registration', ('Done Successfully!'))


################## LOGIN VERIFY SCREEN #
def login_verify():
    global current_balance
    global username1
    global name_display
    global user_display_name
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    DataBase = mysql.connector.connect(host="localhost", user="root", password='Ilovetocode@123')
    curr = DataBase.cursor()

    curr.execute("use scambanker")

    curr.execute("select accid from scambanker ")
    values = curr.fetchall()
    user_acc = []
    for i in values:
        user_acc.append(i[0])

    if username1.isalpha():
        messagebox.showwarning('WARNING', ('Wrong Input!'))
        username_entry1.delete(0, END)
        password_entry1.delete(0, END)

    elif str(username1) == '':
        messagebox.showwarning('WARNING', 'No Accound ID Given!')
        password_entry1.delete(0, END)
    elif str(username1).isspace():
        messagebox.showwarning('WARNING', 'No Accound ID Given!')
        username_entry1.delete(0, END)
        password_entry1.delete(0, END)
    elif username1.isalnum():
        if username1.isdigit():

            if int(username1) in user_acc:

                curr.execute(f"select password from scambanker where accid = {username1} ")
                values = curr.fetchall()
                DataBase.commit()
                user_pass = []
                for i in values:
                    user_pass.append(i[0])

                user_pass_1 = str(user_pass[0])

                if password1 == '':
                    messagebox.showwarning('WARNING', 'No Password Given!')
                    username_entry1.delete(0, END)
                    password_entry1.delete(0, END)
                elif password1 == str(user_pass_1):
                    curr.execute(f"select name from scambanker where accid={username1}")
                    values = curr.fetchall()
                    user_name = []
                    for i in values:
                        user_name.append(i[0])
                    user_display_name = str(user_name[0])
                    # login_sucess()
                    DataBase = mysql.connector.connect(host="localhost", user="root", password='Ilovetocode@123')
                    curr = DataBase.cursor()
                    curr.execute("use scambanker")

                    curr.execute(f'select balance from scambanker where accid ={username1}')
                    values = curr.fetchall()
                    user_balance = []
                    for i in values:
                        user_balance.append(i[0])
                    user_balance_1 = float(user_balance[0])
                    current_balance = user_balance_1

                    screen2.destroy()
                    screen.destroy()
                    abcd()
                elif password1 != str(user_pass_1):
                    password_not_recognised()
            else:
                user_not_found()
        else:
            user_not_found()

    else:
        user_not_found()


################## REGISTER DISPLAY SCREEN #################################
def register():
    global screen1
    global password_entry
    global username_entry
    global rand
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("380x470+750+230")
    screen1.configure(bg='purple')
    screen1.iconphoto(False, tk.PhotoImage(file='abc.png'))

    photo = PhotoImage(file="login_person.png")
    label = Label(screen1, image=photo, bg='purple')
    label.image = photo
    label.pack(pady=5)

    global username
    global password
    global name

    global username_entry
    global password_entry
    global name_entry

    username = StringVar()
    password = StringVar()
    name = StringVar()

    Label(screen1, text="Please enter details below to register", bg='purple', font=("orbitron", 10)).pack()

    Label(screen1, text="", bg='purple').pack()
    Label(screen1, text="Name", font=("orbitron", 10), bg='purple').pack()
    name_entry = Entry(screen1, font=("orbitron", 10), textvariable=name)
    name_entry.pack()

    Label(screen1, text="Account No.", font=("orbitron", 10), bg='purple').pack()
    rand = random.randint(1, 100000)
    username = Label(screen1, text=rand, font=("orbitron", 11), bg='purple').pack()
    #username_entry = Entry(screen1, textvariable=username)
    #username_entry.pack()

    Label(screen1, text="Pin", font=("orbitron", 10), bg='purple').pack()
    password_entry = Entry(screen1, font=("orbitron", 10), textvariable=password)
    password_entry.config(fg='black', show='●')
    password_entry.pack()

    Label(screen1, text="", bg='purple').pack()

    img1 = PhotoImage(file="register_final.png")
    photoimage1 = img1.subsample(3, 3)
    img1Btn = Button(screen1, command=register_user, image=photoimage1, bg='purple', activebackground='purple',
                     relief='flat')
    img1Btn.image = photoimage1
    img1Btn.pack()


################## LOGIN DISPLAY SCREEN #################################
def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("380x470+750+230")
    screen2.configure(bg='purple')

    Label(screen2, text="Please enter details below to login", bg='purple', font=("orbitron", 10)).pack()
    Label(screen2, text="", bg='purple').pack()

    global username_verify
    global password_verify

    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Account No.", bg='purple', font=("orbitron", 10)).pack()
    username_entry1 = tk.Entry(screen2, font=("orbitron", 10), textvariable=username_verify)
    username_entry1.pack()

    Label(screen2, text="", bg='purple').pack()
    Label(screen2, text="Pin", bg='purple', font=("orbitron", 10)).pack()
    password_entry1 = tk.Entry(screen2, font=("orbitron", 10), textvariable=password_verify)
    password_entry1.config(fg='black')
    password_entry1.pack()
    Label(screen2, text="", bg='purple').pack()

    img1 = PhotoImage(file="login_final.png")
    photoimage1 = img1.subsample(3, 3)
    img1Btn = Button(screen2, command=login_verify, image=photoimage1, bg='purple', activebackground='purple',
                     relief=FLAT)
    img1Btn.image = photoimage1
    img1Btn.pack()


#### REGISTER/LOGIN SCREEN
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("530x530+450+120")
    screen.title("Scam Banker")
    screen.configure(bg='purple')
    screen.iconphoto(False, tk.PhotoImage(file='abc.png'))

    Label(text="Scam Banker", fg='white', bg="grey", width="300", height="2", font=("orbitron", 15, 'bold')).pack()
    Label(text="", bg='purple').pack()

    img = ImageTk.PhotoImage(Image.open("download.png"))
    panel = Label(screen, image=img, bg='purple')
    panel.pack()

    photo1 = PhotoImage(file="login_final.png")
    photoimage1 = photo1.subsample(2, 2)
    Button(command=login, bg='purple', activebackground='purple', relief=FLAT, image=photoimage1).pack(pady=5)

    Label(text="", bg='purple', ).pack()

    photo2 = PhotoImage(file="register_final.png")
    photoimage2 = photo2.subsample(2, 2)
    Button(command=register, bg='purple', activebackground='purple', relief=FLAT, image=photoimage2).pack(
        pady=5)

    Label(text="", bg='purple').pack()

    screen.mainloop()


main_screen()
