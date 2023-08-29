import random

class Hat:
	contents = []
	contents_original = []
	balls_drawn = []
	def __init__(self, **color_balls):
		for i in color_balls:
			for j in range(color_balls[i]):
				self.contents.append(i)
				self.contents_original.append(i)
	def draw(self, amount):
		if amount <= len(self.contents):
			for i in range(amount):
				temp = random.choice(self.contents)
				self.balls_drawn.append(temp)
				self.contents.remove(temp)
			return self.balls_drawn

#function: probability to get the least, not exactly equal to
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	M = 0 #amount of experiments is success
	for i in range(num_experiments):#experiments
		count = len(expected_balls)
		hat.draw(num_balls_drawn)#drawn
		for j in expected_balls:
			if hat.balls_drawn.count(j) >= expected_balls[j]:
				count = count - 1
		if count == 0:
			M = M + 1
		#reset to original
		hat.balls_drawn = []
		hat.contents = []
		for k in hat.contents_original:
			hat.contents.append(k)
	return (M/num_experiments)


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat, expected_balls={"red":2,"green":1}, num_balls_drawn=5, num_experiments=2000)
print(probability)
