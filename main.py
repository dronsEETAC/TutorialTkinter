import tkinter as tk

def ConnectButtonClicked():
    global connected
    if not connected:
        ConnectButton['text'] ='Disconnect'
        ConnectButton['bg'] = 'green'
        connected = True
    else:
        ConnectButton['text'] = 'Connect'
        ConnectButton['bg'] = 'red'
        connected = False


connected = False
root = tk.Tk()
root.geometry ("1200x700")
root.title ('Dashboard')
ConnectButton = tk.Button(root, width= 150, text="Connect", bg='red', fg="white", command=ConnectButtonClicked)
ConnectButton.pack()

root.mainloop()