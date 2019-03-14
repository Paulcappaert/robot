import cwiid, RobotMovement, time

class WiiRemote:

	control = 1
	
	def __init__(self):
		wiiMoteConnected = false
		while(wiiMoteConnected == false):
			try:
				self.wii = cwiid.Wiimote()
				wiiMoteConnected = true
			except RunTimeError:
				time.sleep(1)
				print("remote not connected")
				
		self.wii.rpt_mode = cwiid.RPT_BTN

	def getButtons(self):
		print("Getting buttons")
		
	def getControl(self):
		
	
	def manual(self, buttons, robotMovement):
		if(buttons & cwiid.BTN_LEFT):
			robotMovement.Left(leftSpeed, rightSpeed)
		elif (buttons & cwiid.BTN_MINUS):
			robotMovement.RotateLeft(leftSpeed, rightSpeed)
		elif (buttons & cwiid.BTN_PLUS):
			robotMovement.RotateRight(leftSpeed, rightSpeed)
		elif(buttons & cwiid.BTN_RIGHT):
			robotMovement.Right(leftSpeed, rightSpeed)
		elif (buttons & cwiid.BTN_UP):
			robotMovement.Forward(leftSpeed, rightSpeed)
		elif (buttons & cwiid.BTN_DOWN):
			robotMovement.Backward(leftSpeed, rightSpeed)
		elif (buttons & cwiid.BTN_B):
			robotMovement.Stop()
		if (buttons):
			time.sleep(button_delay)
			
	def handleButtons(self):
		buttons = self.wii.state['buttons']
		if (buttons):
			self.control = self.changeControl(buttons, False)
		if (self.control == 1):
			self.manual(buttons,self.robotMovement)
		elif (self.control == 2):
			self.autonomous(buttons)
			
	def changeControl(self, buttons, emergencyStop):
		if (buttons & cwiid.BTN_1):
			self.control = 1
		elif(buttons & cwiid.BTN_2):
			self.control = 2
		elif (emergencyStop):
			self.control = 1
		
	

