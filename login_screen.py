from tkinter import *
import tkinter.messagebox as tm
import MySQLdb

conn = MySQLdb.connect(host= "localhost",user="root",passwd="P@ssw0rd",db="mysql")
#x = conn.cursor()
mycursor=conn.cursor()
mycursor.execute("select * from emp where ESal=901")
for i in mycursor:
    usercheck=i[0]
    passcheck=i[3]
class LoginFrame(Frame):
    def __init__(root, master):
        super().__init__(master)

        root.label_username = Label(root, text="Username")
        root.label_password = Label(root, text="Password")

        root.entry_username = Entry(root)
        root.entry_password = Entry(root, show="*")

        root.label_username.grid(row=0, sticky=E)
        root.label_password.grid(row=1, sticky=E)
        root.entry_username.grid(row=0, column=1)
        root.entry_password.grid(row=1, column=1)

        root.checkbox = Checkbutton(root, text="Keep me logged in")
        root.checkbox.grid(columnspan=3)

        root.logbtn = Button(root, text="Login", command=root._login_btn_clicked)
        root.logbtn.grid(columnspan=3)

        root.pack()

    def _login_btn_clicked(root):
        # print("Clicked")
        username = root.entry_username.get()
        password = root.entry_password.get()

        # print(username, password)

        if username == usercheck and password == passcheck:
            tm.showinfo("Login info", "Welcome praveen")
        else:
            tm.showerror("Login error", "Incorrect username")


root = Tk()
lf = LoginFrame(root)
root.mainloop()