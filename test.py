# from class1 import MyClass
# MyClass.func('self')
from web3 import Web3, HTTPProvider, IPCProvider
web3 = Web3(HTTPProvider('https://rinkeby.infura.io/Eu6qZvhMrNS0ap9G1Qty'))
# web3 = Web3(IPCProvider())
block = web3.eth.blockNumber
print(block)
# from tkinter import *
#
# class Window(Frame):
#
#
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master = master
#         self.init_window()
#
#     #Creation of init_window
#     def init_window(self):
#
#         # changing the title of our master widget
#         self.master.title("GUI")
#
#         # allowing the widget to take the full space of the root window
#         self.pack(fill=BOTH, expand=1)
#
#         # creating a menu instance
#         menu = Menu(self.master)
#         self.master.config(menu=menu)
#
#         # create the file object)
#         file = Menu(menu)
#
#          # adds a command to the menu option, calling it exit, and the
#         # command it runs on event is client_exit
#         file.add_command(label="Exit", command=self.client_exit)
#
#         # creating a button instance
#         quitButton = Button(self, text="Exit",command=self.client_exit)
#
#         # placing the button on my window
#         quitButton.place(x=0, y=0)
#
#         #added "file" to our menu
#         menu.add_cascade(label="File", menu=file)
#
#         # create the file object)
#         edit = Menu(menu)
#
#         # adds a command to the menu option, calling it exit, and the
#         # command it runs on event is client_exit
#         edit.add_command(label="Undo")
#
#         #added "file" to our menu
#         menu.add_cascade(label="Edit", menu=edit)
#
#     def client_exit(self):
#         exit()
#
# root = Tk()
#
# #size of the window
# root.geometry("1380x768")
#
# app = Window(root)
# root.mainloop()
