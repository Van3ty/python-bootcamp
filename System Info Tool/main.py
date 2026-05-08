from src.system_info import (
    get_os_name,
    get_ram_size,
    get_cpu_count,
    get_python_version,
    get_date_time
)

from src.logger_config import logger
from src.utilities import print_separator, print_title


def display_system_info():
    print_title('System Information')

    print(f'OS: {get_os_name()}')
    print(f'CPU Cores: {get_cpu_count()}')
    print(f'RAM: {get_ram_size():.2f} GB')
    print(f'Python Version: {get_python_version()}')
    print(f'Current Date and Time: {get_date_time()}')

    print_separator()

try:

    logger.info('Application started')

    display_system_info()

    logger.info('System information displayed successfully')

except Exception as e:
    logger.error(f'An error occurred: {e}')