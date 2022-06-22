# Author : Raed Ahsan
# Date : 22.06.2022
# Time : 9:37 PM

#Queue ADT ( CIRCULAR )

# Initialization
frontpointer = -1 
rearpointer  = -1
Qsize = 0
Qfull = 10
ub = 9

queue = [None for x in range(9)]

def initializeQ():
	frontpointer = -1
	rearpointer = -1
	Qsize = 0
	Qfull = 10
	ub = 9

	for i in range(9):
		queue[i] = None

# Enqueue ( INSERTION ) - REARPOINTER : 

def enqueue(data):
	global Qsize, Qfull, rearpointer, ub
	if Qsize == Qfull:

		print("[!]--Overflow Error") 
	else:
		if rearpointer == ub:
			rearpointer = 0
		else:
			rearpointer = rearpointer + 1

		queue[rearpointer] = data
		Qsize = Qsize + 1


# Dequeue ( DELETION ) - FRONTPOINTER : 

def dequeue():
	global frontpointer, ub, Qsize

	if Qsize == 0:
		print("[!] Underflow error, no sufficient values.")
	else:
		if frontpointer == ub:
			frontpointer = 0
		else:
			frontpointer = frontpointer + 1

		print("Data Dequeued: ", queue[frontpointer])
		Qsize = Qsize - 1

# Printing live values for the queue ADT circular function..

def live_track():
	global rearpointer, frontpointer, Qsize
	print("RearPointer Location: ", rearpointer)
	print("FrontPointer Location: ", frontpointer)
	print("The Qsize filled: ", Qsize + 1)
	print(queue)
	queue[frontpointer] = None

# Final execution test:
#enqueue:

# enqueue('a')
# live_track()
# enqueue('b')
# live_track()
# enqueue('c')
# live_track()
# enqueue('d')
# live_track()

#dequeue:

# dequeue()
# live_track()
# dequeue()
# live_track()
# dequeue()
# live_track()
# dequeue()
# live_track()