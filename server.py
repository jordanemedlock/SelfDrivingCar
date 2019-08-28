from gpiozero import PWMLED, Motor
from flask import Flask, request
import time

app = Flask(__name__)

move = Motor(27, 17)
move.stop()

class Turn():
	def __init__(self, left, right):
		self.left = PWMLED(left)
		self.right = PWMLED(right)

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

turn = Turn(5, 6)

moving = None

@app.route('/forward')
def forward():
	global moving
	speed = request.args.get('speed') or 0.8
	duration = request.args.get('duration') or 1
	move.forward()
	moving = 'forward'
	time.sleep(duration)
	if moving == 'forward':
		move.stop()
	return "Success"

@app.route('/backward')
def backward():
	global moving
	speed = request.args.get('speed') or 0.8
	duration = request.args.get('duration') or 1
	move.backward()
	moving = 'backward'
	time.sleep(duration)
	if moving == 'backward':
		move.stop()
	return "Success"

@app.route('/stop')
def stop():
	global moving
	move.stop()
	turn.stop()
	moving = False
	return "Success"

@app.route('/left')
def left():
	global turning
	turn.turn_left()
	return "Success"

@app.route('/right')
def right():
	turn.turn_right()
	return "Success"

if __name__ == '__main__':
    app.run('0.0.0.0', 3000, True)
