"""Main Monitoring"""
from time import sleep
import monitoring
import sendhook

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
    send_msg = sendhook.Webhook

    av_mem_raw = mem.get_available_mem(raw = True)
    av_disk_space = storage.get_free_space()
    cpu_temp = cpu.temprature()

    if av_mem_raw <= threshold["mem"]:
        msg = f"<| Ramkapazität ist zu niedrig [{mem.get_available_mem()}] |>"
        send_msg(msg=msg)

    if av_disk_space <= threshold["storage"]:
        msg = f"<| Speicherkapazität beträgt nur noch [{storage.get_free_space()} GB] |>"
        send_msg(msg=msg)

    if cpu.is_linux and cpu_temp >= threshold["temp"]:
        msg = f"<| CPU Temperatur ist zu hoch [{cpu.temprature()} °C] |>"
        send_msg(msg=msg)

    log_mem = f"Used-Memory: {mem.get_used_mem()}"
    log_storage = f"Used-Storage: {storage.get_used_space()} GB"
    log_cpu_temp = f"CPU-Temp: {cpu.temprature()} °C"
    log_cpu_load = f"CPU-Load: {cpu.cpu_load()} %"
    log_save = f"{log_cpu_temp} {log_cpu_load} {log_mem} {log_storage}"

    monitoring.write_log(log_entry=log_save)

while True:
    try:
        main()
        sleep(5)
    except:
        err = "Monitoring Tool Crashed"
        monitoring.write_log(log_entry=err)
        break
