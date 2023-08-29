class Rectangle:
	width = 0
	height = 0
	def __init__(self, width1, height1):
		self.width = width1
		self.height = height1
	def __str__(self):
		return "Rectangle"+"(width="+str(self.width)+", height="+str(self.height)+")"
	def set_width(self, width1):
		self.width = width1
	def set_height(self, height1):
		self.height = height1
	def get_area(self):
		return self.width*self.height
	def get_perimeter(self):
		return self.width*2 + self.height*2
	def get_diagonal(self):
		return ((self.width ** 2 + self.height ** 2) ** .5)
	def get_picture(self):
		if self.width > 50 or self.height > 50:
			return "Too big for picture"
		else:
			for i in range(self.height):
				print("*"*self.width)
			return ""
	def get_amount_inside(self, shape):
		return max(int(self.width/shape.width)*int(self.height/shape.height), int(self.width/shape.height)*int(self.height/shape.width))

class Square(Rectangle):
	def __init__(self, side):
		self.width = side 
		self.height = side
	def __str__(self):
		return "Square"+"(side="+str(self.width)+")"
	def set_side(self, side1):
		self.width = side1
		self.height = side1

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(4)
rect.set_width(7)
rect1 = Rectangle(3, 2)
print(rect.get_amount_inside(rect1))