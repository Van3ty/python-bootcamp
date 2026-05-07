import platform
import psutil
from datetime import datetime

def get_os_name():
    return platform.system()

def get_ram_size():
    return psutil.virtual_memory().total / (1024 ** 3)

def get_cpu_count():
    return psutil.cpu_count()

def get_python_version():
    return platform.python_version()

def get_date_time():
    return datetime.now()
