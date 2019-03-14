import time, socket, sys, serial, struct, cv2, math, os, _thread

class RobotMovement:

	serialConnection = None

	def __init__(self):
	
		#Set up connection to Arduino Mega
		self.serialConnection = serial.Serial('/dev/ttyACM0',9600)
		time.sleep(2)
	
	def Stop(self):
	
		self.serialConnection.write(str("A").encode())
		checksum = 127 & (130 + 0 + 0)
		packet = struct.pack('BBBB', 130, 0, 0, checksum)
		self.serialConnection.write(packet)

		self.serialConnection.write(str("B").encode())
		checksum = 127 & (130 + 4 + 0)
		packet = struct.pack('BBBB', 130, 4, 0, checksum)
		self.serialConnection.write(packet)

		self.serialConnection.write(str("B").encode())
		checksum = 127 & (130 + 1 + 0)
		packet = struct.pack('BBBB', 130, 1, 0, checksum)
		self.serialConnection.write(packet)

		self.serialConnection.write(str("A").encode())
		checksum = 127 & (130 + 5 + 0)
		packet = struct.pack('BBBB', 130, 5, 0, checksum)
		self.serialConnection.write(packet)
		
	def Left(self, leftSpeed, rightSpeed):
	
		#Front Left
		self.serialConnection.write(str("A").encode())
		checksum = 127 & (130 + 1 + leftSpeed)
		packet = struct.pack('BBBB',130,1,leftSpeed,checksum)
		self.serialConnection.write(packet)
		
		#Front Right
		self.serialConnection.write(str("A").encode())
		checksum = 127 & (130 + 5 + rightSpeed)
		packet = struct.pack('BBBB',130,5,rightSpeed,checksum)
		self.serialConnection.write(packet)
		
		#Back Left
		self.serialConnection.write(str("B").encode())
		checksum = 127 & (130 + 4 + leftSpeed)
		packet = struct.pack('BBBB',130,4,leftSpeed,checksum)
		self.serialConnection.write(packet)
		
		#Back Right
		self.serialConnection.write(str("B").encode())
		checksum = 127 & (130 + 0 + rightSpeed)
		packet = struct.pack('BBBB',130,0,rightSpeed,checksum)
		self.serialConnection.write(packet)
	
	def RotateRight(self, leftSpeed, rightSpeed):

		#Front Left
		self.serialConnection.write(str("A").encode())
		checksum = 127 & (130 + 0 + leftSpeed)
		packet = struct.pack('BBBB', 130, 0, leftSpeed, checksum)
		self.serialConnection.write(packet)
		
		#Back Left
		self.serialConnection.write(str("B").encode())
		checksum = 127 & (130 + 4 + leftSpeed)
		packet = struct.pack('BBBB', 130, 4, leftSpeed, checksum)
		self.serialConnection.write(packet)
		
		#Front Right
		self.serialConnection.write(str("A").encode())
		checksum = 127 & (130 + 4 + rightSpeed)
		packet = struct.pack('BBBB',130,4,rightSpeed,checksum)
		self.serialConnection.write(packet)
		
		#Back Right
		self.serialConnection.write(str("B").encode())
		checksum = 127 & (130 + 0 + rightSpeed)
		packet = struct.pack('BBBB',130,0,rightSpeed,checksum)
		self.serialConnection.write(packet)
	
	def RotateLeft(self, leftSpeed, rightSpeed):

		#Front Left
		self.serialConnection.write(str("A").encode())
		checksum = 127 & (130 + 1 + leftSpeed)
		packet = struct.pack('BBBB',130,1,leftSpeed,checksum)
		self.serialConnection.write(packet)
		
		#Back Left
		self.serialConnection.write(str("B").encode())
		checksum = 127 & (130 + 5 + leftSpeed)
		packet = struct.pack('BBBB',130,5,leftSpeed,checksum)
		self.serialConnection.write(packet)
		
		#Front Right
		self.serialConnection.write(str("A").encode())
		checksum = 127 & (130 + 5 + rightSpeed)
		packet = struct.pack('BBBB', 130, 5, rightSpeed, checksum)
		self.serialConnection.write(packet)
		
		#Back Right
		self.serialConnection.write(str("B").encode())
		checksum = 127 & (130 + 1 + rightSpeed)
		packet = struct.pack('BBBB', 130, 1, rightSpeed, checksum)
		self.serialConnection.write(packet)
		
	def Right(self, leftSpeed, rightSpeed):

		#Front Left
		self.serialConnection.write(str("A").encode())
		checksum = 127 & (130 + 0 + leftSpeed)
		packet = struct.pack('BBBB',130,0,leftSpeed,checksum)
		self.serialConnection.write(packet)
		
		#Front Right
		self.serialConnection.write(str("A").encode())
		checksum = 127 & (130 + 4 + rightSpeed)
		packet = struct.pack('BBBB',130,4,rightSpeed,checksum)
		self.serialConnection.write(packet)
		
		#Back Left
		self.serialConnection.write(str("B").encode())
		checksum = 127 & (130 + 5 + leftSpeed)
		packet = struct.pack('BBBB',130,5,leftSpeed,checksum)
		self.serialConnection.write(packet)
		
		#Back Right
		self.serialConnection.write(str("B").encode())
		checksum = 127 & (130 + 1 + rightSpeed)
		packet = struct.pack('BBBB',130,1,rightSpeed,checksum)
		self.serialConnection.write(packet)
	
	def Forward(self, leftSpeed, rightSpeed):
	
		#Front Left
		self.serialConnection.write(str("A").encode())
		checksum = 127 & (130 + 0 + leftSpeed)
		packet = struct.pack('BBBB', 130, 0, leftSpeed, checksum)
		self.serialConnection.write(packet)
		
		#Back Left
		self.serialConnection.write(str("B").encode())
		checksum = 127 & (130 + 4 + leftSpeed)
		packet = struct.pack('BBBB', 130, 4, leftSpeed, checksum)
		self.serialConnection.write(packet)
		
		#Front Right
		self.serialConnection.write(str("A").encode())
		checksum = 127 & (130 + 5 + rightSpeed)
		packet = struct.pack('BBBB', 130, 5, rightSpeed, checksum)
		self.serialConnection.write(packet)
		
		#Back Right
		self.serialConnection.write(str("B").encode())
		checksum = 127 & (130 + 1 + rightSpeed)
		packet = struct.pack('BBBB', 130, 1, rightSpeed, checksum)
		self.serialConnection.write(packet)
		
	def Backward(self, leftSpeed, rightSpeed):
	
		#Front Left
		self.serialConnection.write(str("A").encode())
		checksum = 127 & (130 + 1 + leftSpeed)
		packet = struct.pack('BBBB',130,1,leftSpeed,checksum)
		self.serialConnection.write(packet)
		
		#Back Left
		self.serialConnection.write(str("B").encode())
		checksum = 127 & (130 + 5 + leftSpeed)
		packet = struct.pack('BBBB',130,5,leftSpeed,checksum)
		self.serialConnection.write(packet)
		
		#Front Right
		self.serialConnection.write(str("A").encode())
		checksum = 127 & (130 + 4 + rightSpeed)
		packet = struct.pack('BBBB',130,4,rightSpeed,checksum)
		self.serialConnection.write(packet)
		
		#Back Right
		self.serialConnection.write(str("B").encode())
		checksum = 127 & (130 + 0 + rightSpeed)
		packet = struct.pack('BBBB',130,0,rightSpeed,checksum)
		self.serialConnection.write(packet)