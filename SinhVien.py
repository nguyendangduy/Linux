class sinhvien:
	def __init__(self,TEN,NAMSINH,KHOA):
		self.TEN = TEN
		self.NAMSINH = NAMSINH
		self.KHOA = KHOA
	def getTEN(self):
		return self.TEN
	def setTEN(self,TEN):
		self.TEN = TEN
	def getNAMSINH(self):
		return self.NAMSINH
	def setNAMSINH(self,NAMSINH):
		self.NAMSINH = NAMSINH
	def getKHOA(self):
		return self.KHOA
	def setKHOA(self,KHOA):
		self.KHOA = KHOA
	def toString(self):
		print self.TEN,"-",self.NAMSINH,"-",self.KHOA
	

