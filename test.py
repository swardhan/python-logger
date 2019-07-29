from log_decorator import log

@log
def printer(arg):
	pass

@log
def add(*args):
	total = 0
	for arg in args:
		total = total + arg
	return total

printer('asd', 1)
add(1,2,3,4,5,6,7,8,9,10)
