# W.I.P
import argparse
import psutil
from time import sleep

def memory():
    """testing argparse"""
    while True:
        try:
            mem = psutil.virtual_memory().available / 1024 ** 3
            mem_str = str(round(mem, 2)) + " GB"
            print(mem_str)
            sleep(0.5)
        except:
            break

FUNCTION_MAP = {
    'mem' : memory
}

parser = argparse.ArgumentParser()
parser.add_argument('command', choices=FUNCTION_MAP.keys())

args = parser.parse_args()

print(args.command)

func = FUNCTION_MAP[args.command]
func()
