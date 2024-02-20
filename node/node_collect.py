import psutil
from node.node_metrics import *


clear_metrics()
def get_cpu_info():
    cpu_num = psutil.cpu_count()
    node_cpu_num.labels(cpu_num=cpu_num).set(cpu_num)
    # print("cpu个数：",cpu_num)
    for i in range(cpu_num):
        cpu_percent = psutil.cpu_percent(i)
        # print(i,"cpu使用率：",cpu_percent)
        node_cpu_percent.labels(cpu_num=i).set(cpu_percent)
def get_mem_info():
    mem_total = psutil.virtual_memory().total
    mem_used = psutil.virtual_memory().used
    mem_available = psutil.virtual_memory().available
    mem_free = psutil.virtual_memory().free
    mem_percent = psutil.virtual_memory().percent
    # print("mem_total:",mem_total)
    # print("mem_used:",mem_used)
    # print("mem_available:",mem_available)
    # print("mem_free:",mem_free)
    # print("mem_percent:",mem_percent)
    node_memory_total.labels(memory="memory").set(mem_total)
    node_memory_used.labels(memory="memory").set(mem_used)
    node_memory_available.labels(memory="memory").set(mem_available)
    node_memory_free.labels(memory="memory").set(mem_free)
    node_memory_percent.labels(memory="memory").set(mem_percent)
def get_disk_info():
    disk_list = psutil.disk_partitions()
    for mountpoints in disk_list:
        disk_type = mountpoints.fstype
        mountpoint = mountpoints.mountpoint
        disk_total = psutil.disk_usage(mountpoint).total
        disk_used = psutil.disk_usage(mountpoint).used
        disk_free = psutil.disk_usage(mountpoint).free
        disk_percent = psutil.disk_usage(mountpoint).percent
        # print(disk_total)
        # print(disk_used)
        # print(disk_free)
        # print(disk_percent)
        node_disk_total.labels(mountpoint=mountpoint,fstype=disk_type).set(disk_total)
        node_disk_used.labels(mountpoint=mountpoint,fstype=disk_type).set(disk_used)
        node_disk_free.labels(mountpoint=mountpoint,fstype=disk_type).set(disk_free)
        node_disk_percent.labels(mountpoint=mountpoint,fstype=disk_type).set(disk_percent)

def get_network_info():
    pass
def get_custom_info():
    pass


# get_cpu_info()
# get_mem_info()
# get_disk_info()