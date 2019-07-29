import traceback
import sys
import datetime

def log(function):
# 	log_template = """
# ==================================================
# 	Date: %(date)s
# 	Time: %(time)s
# 	Function Name: %(func_name)s
# 	Arguments: %(args)s
# 	Keyword Arguments: %(kwargs)s
# 	Return Value: %(ret_val)s
# 	Traceback: %(traceback)s
# ==================================================
# 	"""
	log_template = """
%(date)s %(time)s %(func_name)s %(args)s %(kwargs)s %(ret_val)s %(traceback)s
	"""

	def wrapper(*args, **kwargs):

		ret_val = None
		tb = None
		dt = datetime.datetime.now()

		try:
			ret_val = function(*args, **kwargs)
		except Exception as e:
			trace = sys.exc_info()
			tb = '\n'.join(traceback.format_exception(*trace))
			if tb is not None:
				tb = '\n'+tb

		finally:
			log_data = log_template % {
					'date': dt.strftime("%b %d"),
					'time': dt.strftime("%H:%M:%S"),
					'func_name': function.__name__,
					'args': args,
					'kwargs': kwargs,
					'ret_val': ret_val,
					'traceback': tb
				}

			with open("logger.log", "a") as logfile:
				logfile.write(log_data)			

	return wrapper
