import threading
from TcpServer import TcpServer
from KeyboardListener import KeyboardListener
from service import *
from ComputerMonitor import ComputerMonitor
from CommandMessage import CommandMessage;
import json
import pyautogui
from KeyboardManager import *
import time


def on_message_received(data):
	command_message = json.loads(data)
	script = command_message["script"]
	params = command_message["params"]
	exec(script)

def on_screen_locked():
	print("screen locked")
	data = json.dumps({"command":2,"message":""})
	print(data)
	tcpServer.send_text(data)

computerMonitor = ComputerMonitor(on_screen_locked)

def on_tcp_connected():
	if not computerMonitor.started:
		computerMonitor.start()


tcpServer = TcpServer()
tcpServer.set_receive_listener(on_message_received)
tcpServer.connected_listener = on_tcp_connected
tcpServer.start()

keyboardListener = KeyboardListener(tcpServer)

def onTrans():
	print("need trans")
	content = getClipContent()
	text = json.dumps({"command":1,"message":content})

	tcpServer.send_text(text)

keyboardListener.listen_keyboard(onTrans)