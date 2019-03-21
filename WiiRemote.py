import cwiid, RobotMovement, time

class WiiRemote:

	control = 1
	button_delay = 0.1
	rightSpeed = 10
	leftSpeed = 10
	
	def __init__(self):
		wiiMoteConnected = False
		while(wiiMoteConnected == False):
			try:
				self.wii = cwiid.Wiimote()
				wiiMoteConnected = True
			except RuntimeError:
				time.sleep(0.25)
				print("Wii Remote NOT connected...")

		print("Wii remote connected!")				
		self.wii.rpt_mode = cwiid.RPT_BTN
		
	def getControl(self):
		return self.control
	
	def handleButtonPress(self, robotMovement):
		buttons = self.wii.state['buttons']
		if (buttons & cwiid.BTN_1):
			self.control = 1
		elif(buttons & cwiid.BTN_2):
			self.control = 2
		elif(buttons & cwiid.BTN_LEFT):
			robotMovement.Left(self.leftSpeed, self.rightSpeed)
		elif (buttons & cwiid.BTN_MINUS):
			robotMovement.RotateLeft(self.leftSpeed, self.rightSpeed)
		elif (buttons & cwiid.BTN_PLUS):
			robotMovement.RotateRight(self.leftSpeed, self.rightSpeed)
		elif(buttons & cwiid.BTN_RIGHT):
			robotMovement.Right(self.leftSpeed, self.rightSpeed)
		elif (buttons & cwiid.BTN_UP):
			robotMovement.Forward(self.leftSpeed, self.rightSpeed)
		elif (buttons & cwiid.BTN_DOWN):
			robotMovement.Backward(self.leftSpeed, self.rightSpeed)
		elif (buttons & cwiid.BTN_B):
			robotMovement.Stop()
		if (buttons):
			time.sleep(self.button_delay)
	

