import datetime
import time

class LogPupedu(object):
    '''简易 Logger'''
    def __init__(self):
        pass
    
    
    def log(self, message):
        when = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print('%s: %s' % (when, message))
        
        
    def echo(self, message):
        print(message)
    
    
Logger = LogPupedu()