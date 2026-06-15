import logging
from utils import safe_divide


logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
)

logging.info('Application started')
logging.info('Bootcamp day 3 in progress')


try:
    a, b = int(input("Enter the first number: ")), int(input("Enter the second number: "))
    logging.info('Age entered successfully')
    print(safe_divide(a, b))

except ValueError:
    logging.error('Invalid input provided by user')
    print("Invalid input. Please enter valid integers.")

finally:
    logging.info('Execution completed.')
    print("Execution completed.")