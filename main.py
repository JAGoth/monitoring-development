"""Main Monitoring"""
from time import sleep
import monitoring
#import sendhook

def main():
    """Monitoring"""
    threshold = {
        "mem" : 1,
        "storage" : 10,
        "temp": 90
    }
    cpu = monitoring.GetCPU()
    mem = monitoring.GetMem()
    storage = monitoring.GetDisk()

    av_mem_raw = mem.get_available_mem(raw = True)
    av_disk_space = storage.get_free_space()
    cpu_temp = cpu.temprature()

    if av_mem_raw <= threshold["mem"]:
        print("Low Mem")

    if av_disk_space <= threshold["storage"]:
        print("Low Storage")

    if cpu_temp is int and cpu_temp >= threshold["temp"]:
        print("Warm")

    log_mem = f"Used-Memory: {mem.get_used_mem()}"
    log_storage = f"Used-Storage: {storage.get_used_space()} GB"
    log_cpu_temp = f"CPU-Temp: {cpu.temprature()} °C"
    log_cpu_load = f"CPU-Load: {cpu.cpu_load()} %"
    log_save = f"{log_cpu_temp} {log_cpu_load} {log_mem} {log_storage}"

    monitoring.write_log(log_entry=log_save)

while True:
    main()
    sleep(5)
