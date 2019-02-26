
class Robot:

	imageProcessing = None
	Sensors = None
	wiiRemote = None
	running = False
	control = -1

	def __init__(self):
		self.imageProcessing = ImageProcessing()
		self.Sensors = Sensors()
		self.wiiRemote = WiiRemote()
		self.running = True
		self.control()

	def control(self):
		while self.running:
			buttons = wiiRemote.getButtons()
			if (buttons):
				control = changeControl()
			if (control == 1):
				self.manual(buttons)
			elif (control == 2):
				self.autonomous(buttons)
				
	def changeControl(self):
		if (wiiRemote.getButtonPressed() == 1):
			control = 1
		elif(wiiRemote.getButtonPressed() == 2):
			control = 2
			
	def manual(self, buttons):


	def autonomous(self, buttons):
