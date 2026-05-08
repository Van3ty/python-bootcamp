import logging  

logging.basicConfig(
    filename="organizer_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


logger = logging.getLogger()