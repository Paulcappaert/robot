import cwiid, RobotMovement, time

class WiiRemote:

	control = 1
	button_delay = 0.1
	rightSpeed = 40
	leftSpeed = 40
	
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
			print("Left")
			robotMovement.Left(self.leftSpeed, self.rightSpeed)
		elif (buttons & cwiid.BTN_MINUS):
			print("Rotate Left")
			robotMovement.RotateLeft(self.leftSpeed, self.rightSpeed)
		elif (buttons & cwiid.BTN_PLUS):
			print("Rotate Right")
			robotMovement.RotateRight(self.leftSpeed, self.rightSpeed)
		elif(buttons & cwiid.BTN_RIGHT):
			print("Right")
			robotMovement.Right(self.leftSpeed, self.rightSpeed)
		elif (buttons & cwiid.BTN_UP):
			print("Forward")
			robotMovement.Forward(self.leftSpeed, self.rightSpeed)
		elif (buttons & cwiid.BTN_DOWN):
			print("Backward")
			robotMovement.Backward(self.leftSpeed, self.rightSpeed)
		elif (buttons & cwiid.BTN_B):
			print("Stop")
			robotMovement.Stop()
		if (buttons):
			time.sleep(self.button_delay)
	

