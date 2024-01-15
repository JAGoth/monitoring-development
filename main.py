"""Main Monitoring"""
from time import sleep
import monitoring
import sendhook

def main():
    """Monitoring"""
    # Values ar in GB and °C
    threshold = {
    "mem": {"hard": 1, "soft": 2},
    "storage": {"hard": 15, "soft": 30},
    "temp": {"hard": 95, "soft": 85}
    }

    cpu = monitoring.GetCPU()
    mem = monitoring.GetMem()
    storage = monitoring.GetDisk()

    av_mem_raw = mem.get_available_mem(raw = True)
    av_disk_space = storage.get_free_space()
    cpu_temp = cpu.temprature()

    compare("Ramkapazität", threshold["mem"], av_mem_raw, " GB", False)

    compare("Speicherkapazität", threshold["storage"], av_disk_space, " GB", False)

    if cpu.is_linux:
        compare("CPU Temprature", threshold["temp"], cpu_temp, " °C", True)

    log_mem = f"Used-Memory: {mem.get_used_mem()}"
    log_storage = f"Used-Storage: {storage.get_used_space()} GB"
    log_cpu_temp = f"CPU-Temp: {cpu.temprature()} °C"
    log_cpu_load = f"CPU-Load: {cpu.cpu_load()} %"
    log_save = f"{log_cpu_temp} {log_cpu_load} {log_mem} {log_storage}"

    monitoring.write_log(log_entry=log_save)

def compare(resource, threshold, get_value, get_unit="",is_high=True):
    "Compares resource with threshold"
    send_msg = sendhook.Webhook
    value = get_value()

    if is_high:
        if value >= threshold["hard"]:
            msg = f"<| Warnung {resource} ist zu hoch [{value}{get_unit}] |>"
            send_msg(msg = msg)
        elif value >= threshold["soft"]:
            msg = f"<| {resource} ist zu hoch [{value}{get_unit}] |>"
            send_msg(msg = msg)
    else:
        if value <= threshold["hard"]:
            msg = f"<| Warnung {resource} ist zu niedrig [{value}{get_unit}] |>"
            send_msg(msg=msg)
        elif value <= threshold["soft"]:
            msg = f"<| {resource} ist zu niedrig [{value}{get_unit}] |>"
            send_msg(msg=msg)

while True:
    try:
        main()
        sleep(5)
    except RuntimeError:
        VAR_ERROR = "Monitoring Tool Crashed"
        monitoring.write_log(log_entry=VAR_ERROR)
        break
