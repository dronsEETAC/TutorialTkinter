import tkinter as tk

def ConnectButtonClicked():
    global connected
    if not connected:
        ConnectButton['text'] ='Disconnect'
        ConnectButton['bg'] = 'green'
        connected = True
        MainFrame.pack(fill="both", expand="yes", padx=10, pady=10)
    else:
        ConnectButton['text'] = 'Connect'
        ConnectButton['bg'] = 'red'
        connected = False
        MainFrame.pack_forget()

def button1Clicked ():
    print ('button 1 clicked')

connected = False
root = tk.Tk()
root.geometry ("1200x700")
root.title ('Dashboard')
ConnectButton = tk.Button(root, width= 150, text="Connect", bg='red', fg="white", command=ConnectButtonClicked)
ConnectButton.pack()
MainFrame = tk.Frame(root)
TopFrame = tk.LabelFrame(MainFrame, text = 'Top')
TopFrame.pack(fill="both", expand="yes", padx=10, pady=5)
TopFrame.rowconfigure(0, weight=1)
TopFrame.rowconfigure(1, weight=4)
TopFrame.columnconfigure(0, weight=1)
TopFrame.columnconfigure(1, weight=1)
TopFrame.columnconfigure(2, weight=1)
TopFrame.columnconfigure(3, weight=1)

Button1 = tk.Button(TopFrame, text="Button 1", bg='red', fg="white", command=button1Clicked)
Button1.grid(row=0, column=0, padx=5, pady=5, sticky="nesw")
Button2 = tk.Button(TopFrame, text="Button 2", bg='blue', fg="white", command=button1Clicked)
Button2.grid(row=0, column=1, padx=5, pady=5, sticky="nesw")
Button3 = tk.Button(TopFrame,  text="Button 3", bg='yellow', fg="black", command=button1Clicked)
Button3.grid(row=0, column=2, padx=5, pady=5, sticky="nesw")
Button4 = tk.Button(TopFrame, text="Button 4", bg='green', fg="white", command=button1Clicked)
Button4.grid(row=0, column=3, padx=5, pady=5, sticky="nesw")
Button5 = tk.Button(TopFrame, text="Button 5", bg='pink', fg="black", command=button1Clicked)
Button5.grid(row=1, column=0, columnspan =4, padx=5, pady=5, sticky="nesw")



MidFrame = tk.Frame(MainFrame)
MidFrame.pack(fill="both", expand="yes", padx=10, pady=5)
LeftFrame = tk.LabelFrame(MidFrame, text = 'Left')
LeftFrame.pack(side = tk.LEFT,fill="both", expand="yes", padx=5, pady=5)
RightFrame = tk.LabelFrame(MidFrame, text = 'Right')
RightFrame.pack(side = tk.RIGHT,fill="both", expand="yes", padx=5, pady=5)
BottomFrame = tk.LabelFrame(MainFrame, text = 'Bottom')
BottomFrame.pack(fill="both", expand="yes", padx=10, pady=5)



root.mainloop()