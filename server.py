from gpiozero import PWMLED, Motor
from flask import Flask
import time

app = Flask(__name__)

move = Motor(27, 17)
move.stop()


turn = Turn(5, 6)

class Turn():
	def __init__(self, left, right):
		this.left = PWMLED(left)
		this.right = PWMLED(right)

	def turn_left(self, value=0.2, for_time=0.2):
		self.left.value = value
		time.sleep(for_time)
		self.left.value = 0

	def turn_right(self, value=0.2, for_time=0.2):
		self.right.value = value
		time.sleep(for_time)
		self.right.value = 0

	def stop(self):
		self.right.off()
		self.left.off()

	def close(self):
		self.left.close()
		self.right.close()

@app.route('/forward')
def forward():
	move.forward()
	return "Success"

@app.route('/backward')
def backward():
	move.backward()
	return "Success"

@app.route('/stop')
def stop():
	move.stop()
	return "Success"

@app.route('/left')
def left():
	turn.turn_left()
	return "Success"

@app.route('/right')
def right():
	turn.turn_right()
	return "Success"
