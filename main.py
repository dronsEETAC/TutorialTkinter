import tkinter as tk
from TopFrameClass import TopFrameClass
from RightFrameClass import RightFrameClass

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

connected = False
root = tk.Tk()
root.geometry ("1200x700")
root.title ('Dashboard')
ConnectButton = tk.Button(root, width= 150, text="Connect", bg='red', fg="white", command=ConnectButtonClicked)
ConnectButton.pack()
MainFrame = tk.Frame(root)

topFrameClass = TopFrameClass()
TopFrame= topFrameClass.buildFrame(MainFrame)
TopFrame.pack(fill="both", expand="yes", padx=10, pady=5)

MidFrame = tk.Frame(MainFrame)
MidFrame.pack(fill="both", expand="yes", padx=10, pady=5)
LeftFrame = tk.LabelFrame(MidFrame, text = 'Left')
LeftFrame.pack(side = tk.LEFT,fill="both", expand="yes", padx=5, pady=5)

rightFrameClass = RightFrameClass()
RightFrame= rightFrameClass.buildFrame(MidFrame)
topFrameClass.setRightFrame (rightFrameClass)
RightFrame.pack(side = tk.RIGHT,fill="both", expand="yes", padx=5, pady=5)

BottomFrame = tk.LabelFrame(MainFrame, text = 'Bottom')
BottomFrame.pack(fill="both", expand="yes", padx=10, pady=5)



root.mainloop()