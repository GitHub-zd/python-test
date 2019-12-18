import logging
import warnings

logging.basicConfig(level=logging.INFO,)
warnings.warn('this warn is not send to the logs')
logging.captureWarnings(True)
warnings.warn('this warning is send to the log')

