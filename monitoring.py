"""Monitoring script"""
# Importing Libaries and local Files
from time import sleep
import datetime
import os
import platform
import psutil
#import sendhook

class GetCPU():
    """Gets CPU information"""
    def __init__(self):
        self.system = platform.system().lower()
        if self.system == "linux":
            self.cpu_temp = psutil.sensors_temperatures()['coretemp'][0].current
        self.cpu_load = psutil.cpu_percent
        self.cpu_core_count = psutil.cpu_count
        self.cpu_freq = psutil.cpu_freq

    def temprature(self):
        """Function outputs current cpu temp"""
        if self.system == "linux":
            return self.cpu_temp
        err_msg = f"Sorry the {self.system} os isn't supported. :("
        return err_msg

    def frequency(self, per_core:bool = False):
        """Function outputs current frequenzy"""
        cpu_freq = self.cpu_freq(percpu=per_core)
        return cpu_freq

    def load(self, per_thread:bool = False):
        """Function outputs current load"""
        loop_var = 0
        while loop_var != 2:
            cpu_load_avg = psutil.cpu_percent(percpu = per_thread)
            loop_var += 1
            sleep(0.5)
        return cpu_load_avg

    def show_core_count(self, per_thread:bool = False):
        """Function outputs core count"""
        core_count = self.cpu_core_count(logical = per_thread)
        return core_count

class GetDisk():
    """Gets storage information"""
    def __init__(self):
        self.disks_data = {}
        for disk in psutil.disk_partitions():
            if disk.fstype.lower() in ("ext4", "ntfs", "xfs", "hfs+", "fat32"):
                total_space_kb = psutil.disk_usage(disk.mountpoint).total
                free_space_kb = psutil.disk_usage(disk.mountpoint).free
                used_space_kb = psutil.disk_usage(disk.mountpoint).used

                self.disks_data[disk.mountpoint] = [used_space_kb, free_space_kb, total_space_kb]

    def get_total_space(self, disk:str = ""):
        """Function outputs the total space"""
        total_space_gib = round(self.disks_data[f"{disk}" if disk != "" else f"{next(iter(self.disks_data))}"][2] / 1024 ** 3, 2)
        return total_space_gib

    def get_free_space(self, disk:str):
        """Function outputs the free space"""
        free_space_gib = round(self.disks_data[f"{disk}" if disk != "" else f"{next(iter(self.disks_data))}"][1] / 1024 ** 3, 2)
        return free_space_gib

    def get_used_space(self, disk:str = ""):
        """Function outputs space that is used"""
        free_space_gib = round(self.disks_data[f"{disk}" if disk != "" else f"{next(iter(self.disks_data))}"][0] / 1024 ** 3, 2)
        return free_space_gib

class GetMem():
    """Gets ram information"""

    def __init__(self):
        self.mem = psutil.virtual_memory()

    def get_total_mem(self, raw:bool = False):
        """Function outputs the total ram"""
        total_mem = round(self.mem.total / 1024 ** 3, 2)
        if raw:
            return total_mem
        return str(total_mem) + " GB"

    def get_available_mem(self, raw:bool = False):
        """Function outputs the available ram"""
        av_mem = round(self.mem.available / 1024 ** 3, 2)
        if raw:
            return av_mem
        return str(av_mem) + " GB"

    def get_used_mem(self, raw:bool = False):
        """Function outputs the used ram"""
        used_mem = round(self.mem.used / 1024 ** 3, 2)
        if raw:
            return used_mem
        return str(used_mem) + " GB"

def write_log(path:str = f"{os.getcwd()}", log_entry:str = "", log_user:str = ""):
    """Function writes into a log"""
    with open(f"{path}/{f'{log_user}-' if log_user != '' else ''}log-{datetime.date.today()}.log", "a", encoding="utf-8") as log:
        log.write(f"{log_entry}")
