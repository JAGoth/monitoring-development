# Importing Libaries and local Files
import psutil
import sendhook

class GetMem():

    def __init__(self):
        self.mem = psutil.virtual_memory()
    
    def get_total_mem(self, raw:bool=False):
        total_mem = round(self.mem.total / 1024 ** 3, 2)
        if raw:
            return total_mem
        return str(total_mem) + " GB"
    
    def get_available_mem(self, raw:bool=False):
        av_mem = round(self.mem.available / 1024 ** 3, 2)
        if raw:
            return av_mem
        return str(av_mem) + " GB"
    
    def get_used_mem(self, raw:bool=False):
        used_mem = round(self.mem.used / 1024 ** 3, 2)
        if raw:
            return used_mem
        return str(used_mem) + " GB"
