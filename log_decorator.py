import traceback
import sys
import datetime
import logging

logging.basicConfig(filename="logfile.log", format='%(asctime)s-%(message)s', datefmt="%b %d %Y-%H:%M:%S") 
logger = logging.getLogger()
logger.setLevel(logging.DEBUG) 

def log(mask_args=[], masked_kwargs=[]):
	def outer_wrapper(function):

		log_template = """
	%(func_name)s %(args)s %(kwargs)s %(ret_val)s %(traceback)s
		"""

		def wrapper(*args, **kwargs):

			ret_val = None
			tb = None
			dt = datetime.datetime.now()
			temp_args = list(args)
			temp_kwargs = kwargs

			for index in mask_args:
				if index > 0 or index < len(mask_args):
					temp_args[index] = 'xxxx'

			for key in masked_kwargs:
				temp_kwargs[key] = 'xxxx'

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
						'args': temp_args,
						'kwargs': temp_kwargs,
						'ret_val': ret_val,
						'traceback': tb
					}

				logger.info(log_data)

		return wrapper
	return outer_wrapper
