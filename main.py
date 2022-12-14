import base64
import tkinter as tk
from TopFrameClass import TopFrameClass
from RightFrameClass import RightFrameClass
from LeftFrameClass import LeftFrameClass
import paho.mqtt.client as mqtt
import socketio
from tkinter import messagebox

def on_message(cli, userdata, message):
    if message.topic == 'Value':
        print ('valor ', message.payload)
        topFrameClass.PutValue(message.payload)
    if message.topic == 'videoFrame':
        jpg_original = base64.b64decode(message.payload)
        leftFrameClass.SetFrame(jpg_original)
        print ('video frame received')


def ConnectButtonClicked():
    global connected
    global client
    global sio
    if not connected:
        ConnectButton['text'] ='Disconnect'
        ConnectButton['bg'] = 'green'
        connected = True
        MainFrame.pack(fill="both", expand="yes", padx=10, pady=10)
        client.publish('Connect')
        sio.emit('connectPlatform')




    else:
        ConnectButton['text'] = 'Connect'
        ConnectButton['bg'] = 'red'
        connected = False
        MainFrame.pack_forget()


connected = False
root = tk.Tk()
root.geometry ("1200x700")
root.title ('Dashboaq:rd')

broker_address = "broker.hivemq.com"
broker_port = 8000

client = mqtt.Client(transport="websockets")
client.on_message = on_message
client.connect(broker_address, broker_port)

client.loop_start()

ConnectButton = tk.Button(root, width= 150, text="Connect", bg='red', fg="white", command=ConnectButtonClicked)
ConnectButton.pack()
MainFrame = tk.Frame(root)

topFrameClass = TopFrameClass()
TopFrame= topFrameClass.buildFrame(MainFrame, client)
TopFrame.pack(fill="both", expand="yes", padx=10, pady=5)

MidFrame = tk.Frame(MainFrame)
MidFrame.pack(fill="both", expand="yes", padx=10, pady=5)

leftFrameClass = LeftFrameClass()
LeftFrame= leftFrameClass.buildFrame(MidFrame, client)
LeftFrame.pack(side = tk.LEFT,fill="both", expand="yes", padx=5, pady=5)

rightFrameClass = RightFrameClass()
RightFrame= rightFrameClass.buildFrame(MidFrame)
topFrameClass.setRightFrame (rightFrameClass)
RightFrame.pack(side = tk.RIGHT,fill="both", expand="yes", padx=5, pady=5)

BottomFrame = tk.LabelFrame(MainFrame, text = 'Bottom')
BottomFrame.pack(fill="both", expand="yes", padx=10, pady=5)

sio = socketio.Client()
sio.connect('http://localhost:5000')


@sio.on('connected')
def on_message(data):
    messagebox.showinfo('Wellcom message', data)







root.mainloop()