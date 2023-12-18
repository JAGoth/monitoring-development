# Importing Libaries and local Files
import sendhook
import psutil

class GetMem():

    def __init__(self):
        self.mem = psutil.virtual_memory()
    
    def getTotalMem(self, raw:bool=False):
        total_mem = round(self.mem.total / 1024 ** 3, 2)
        if raw:
            return str(total_mem) + " GB"
        else:
            return total_mem
    
    def getAvailableMem(self, raw:bool=False):
        av_mem = round(self.mem.available / 1024 ** 3, 2)
        if raw:
            return str(av_mem) + " GB"
        else:
            return av_mem
    
    def getUsedMem(self, raw:bool=False):
        used_mem = round(self.mem.used / 1024 ** 3, 2)
        if raw:
            return str(used_mem) + " GB"
        else:
            return used_mem