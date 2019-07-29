import traceback
import sys
import datetime
import logging

logging.basicConfig(filename="newfile.log", format='%(asctime)s-%(message)s', datefmt="%b %d %Y-%H:%M:%S") 
logger = logging.getLogger()
logger.setLevel(logging.DEBUG) 

def log(function):

	log_template = """
%(func_name)s %(args)s %(kwargs)s %(ret_val)s %(traceback)s
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
					'func_name': function.__name__,
					'args': args,
					'kwargs': kwargs,
					'ret_val': ret_val,
					'traceback': tb
				}

			logger.info(log_data)

	return wrapper
