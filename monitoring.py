"""Monitoring script"""
# Importing Libaries and local Files
import psutil
import os
import sendhook

class GetMem():
    """Gets ram information"""

    def __init__(self):
        self.mem = psutil.virtual_memory()
    
    def get_total_mem(self, raw:bool=False):
        """Function outputs the total ram"""
        total_mem = round(self.mem.total / 1024 ** 3, 2)
        if raw:
            return total_mem
        return str(total_mem) + " GB"
    
    def get_available_mem(self, raw:bool=False):
        """Function outputs the available ram"""
        av_mem = round(self.mem.available / 1024 ** 3, 2)
        if raw:
            return av_mem
        return str(av_mem) + " GB"
    
    def get_used_mem(self, raw:bool=False):
        """Function outputs the used ram"""
        used_mem = round(self.mem.used / 1024 ** 3, 2)
        if raw:
            return used_mem
        return str(used_mem) + " GB"

def write_log(path:str = f"{os.getcwd()}/log.log", log_entry:str = ""):
    """Function writes into a log"""
    with open(f'{path}', "a") as log:
        log.write(f"\n{log_entry}\n")

funny_number = 42
while True:
    write_log(log_entry=F"{funny_number}")
    funny_number += 27