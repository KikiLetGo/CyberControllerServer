import keyboard
import time
from screen_shot import ScreenCapture
import io

class KeyboardListener:
	def __init__(self, tcpServer):
		self.tcpServer = tcpServer
		self.t = 0
		self.c = 0
		self.key_state_map={}
		self.screen_capture = None
		
	def listen_keyboard(self,callback):
		self.callback = callback
		keyboard.hook(self.onKeyEvent)
		keyboard.wait()

	def onImgCapture(self,pic):	
		imgByteArr = io.BytesIO()
		pic.save(imgByteArr, format='JPEG')
		bytes_data = imgByteArr.getvalue()
		self.tcpServer.send_img(bytes_data)

	def isCtrlHolding(self):
		return ('ctrl' in self.key_state_map and self.key_state_map['ctrl']=='down')\
			or ('left ctrl' in self.key_state_map and self.key_state_map['left ctrl']=='down')\
			or ('right ctrl' in self.key_state_map and self.key_state_map['right ctrl']=='down')

	def isAltHolding(self):
		return ('alt' in self.key_state_map and self.key_state_map['alt']=='down')\
			or ('left alt' in self.key_state_map and self.key_state_map['left alt']=='down')\
			or ('right alt' in self.key_state_map and self.key_state_map['right alt']=='down')

	def isKeyHolding(self,key):
		return (key in self.key_state_map and self.key_state_map[key]=='down')


	def onKeyEvent(self,key):
		#update key_state_map
		self.key_state_map[key.name.lower()]=key.event_type

		#is screenshoot?

		if  self.isKeyHolding("caps lock")\
			and key.event_type=="down"\
			and key.name.lower()=="a":
			self.screen_capture = ScreenCapture()
			self.screen_capture.are_capture(self.onImgCapture)

		print(self.key_state_map)
		#is triple c?
		if  key.event_type=="down" \
			and key.name.lower()=="c" \
			and self.isCtrlHolding():

			if self.t == 0:
				self.t=time.time()
				self.c += 1
				print("wait for nex c",self.c)
				return

			if (time.time()-self.t<0.5):
				self.t=time.time()
				self.c += 1
				print("wait for nex c:",self.c)

			else:
				self.c = 0
				self.t=0
				print("wait for nex c",self.c)

			if self.c>=2:
				self.c=0
				print("need trans")
				if self.callback:
					self.callback()

