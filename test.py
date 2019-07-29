from log_decorator import log

@log()
def printer(arg):
	pass

@log()
def add(*args, **kwargs):
	total = 0
	for arg in args:
		total = total + arg
	return total

printer('Saumya')

add(1,2,3, abc="abc", test=11)

