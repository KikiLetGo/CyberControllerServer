import pyautogui
import time
from KeyboardManager import key_press
time.sleep(2)
with open('./TcpServer.py', encoding='UTF-8') as f:
	while True:
		line = f.readline()
		if not line:
			break
		print(line)
		#pyautogui.typewrite(line)
		#key_press("home")
		for c in line:
			out = open('out.py','a')
			out.write(c)
			out.close()
			time.sleep(0.001)

	# for line in content:
	# 	print(line)
	
	# print('\n')
	# pyautogui.typewrite('\n')
