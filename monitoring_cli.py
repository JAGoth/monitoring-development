"""Monitoring commandline tool / W.I.P"""
# W.I.P
import argparse
import monitoring
import os
import time

def draw_graph(value, graph_name):
    """draws the graph"""
    percentage = value / 100
    progress = int(percentage * 50)
    remaining = 50 - progress
    graph = '[' + '|' * progress + ' ' * remaining + '] ' + str(int(percentage * 100)) + '%' + graph_name
    return graph

def update_graphs(values, graph_name):
    """updates graph"""
    os.system('clear')
    for i in range(len(values)):
        print(draw_graph(values[i], graph_name[i]))
    time.sleep(0.1)

# Initialisieren Sie die Werte und maximalen Werte für die Graphen
def create_graph():
    """creates graph"""
    values = [0, 0, 0]
    graph_name = [" Memory Used", " CPU Load", " Storage Used"]



    # Aktualisieren Sie die Graphen in einer Endlosschleife
    while True:
        mem = monitoring.GetMem()
        storage = monitoring.GetDisk()
        values[0] = mem.get_used_mem(raw=True) / mem.get_total_mem(raw=True) * 100
        values[1] = monitoring.GetCPU().load()
        values[2] = storage.get_used_space() / storage.get_total_space() * 100
        update_graphs(values, graph_name)



FUNCTION_MAP = {
    'monitor' : create_graph
}

parser = argparse.ArgumentParser()
parser.add_argument('command', choices=FUNCTION_MAP.keys())

args = parser.parse_args()

print(args.command)

func = FUNCTION_MAP[args.command]
func()
