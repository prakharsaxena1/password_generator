
from tkinter import *
loginWindow = Tk()
loginWindow.geometry('300x240')
loginWindow.title("LOG-IN")
loginWindow.iconbitmap('icon/lock.ico')
#loginWindow.resizable(0, 0)

textLabel = Label(loginWindow, text='---- Login to continue ----',
                  font=("Comic Sans", 15))
textLabel.grid(column=0, row=0, padx=(50, 50), pady=(5, 5))


# Username
usernameLabel = Label(loginWindow, text="Username ", font=("Comic Sans", 15))
usernameLabel.grid(column=0, row=1, padx=(20, 20),
                   pady=(20, 20), ipadx=(5), ipady=(2), sticky='W')
usernameEntry = Entry(loginWindow, width=20)
usernameEntry.grid(column=0, row=1, padx=(10, 10),
                   pady=(20, 10), ipadx=(5), ipady=(2), sticky='E')

# password
passwordLabel = Label(loginWindow, text="Password ", font=("Comic Sans", 15))
passwordLabel.grid(column=0, row=2, padx=(10, 10),
                   pady=(20, 10), ipadx=(5), ipady=(2), sticky='W')
passwordEntry = Entry(loginWindow, width=20)
passwordEntry.grid(column=0, row=2, padx=(10, 10),
                   pady=(20, 10), ipadx=(5), ipady=(2), sticky='E')

# loginButton
loginButton = Button(loginWindow, text=' Login ')
loginButton.grid(column=0, row=3, padx=(10, 10),
                 pady=(20, 20), ipadx=(15), ipady=(2))


loginWindow.mainloop()
