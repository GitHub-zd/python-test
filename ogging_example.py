import logging

log_file = 'log.txt'
logging.basicConfig(filename=log_file,level=logging.DEBUG,)
logging.debug('this messages should go to the log file')
with open(log_file,'rt') as f:
    prg = f.read()
print('file:')
print(prg)
