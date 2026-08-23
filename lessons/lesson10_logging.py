'''##Logging gives you levels, timestamps, filtering, and configurable output.
Python categorizes log events into five standardized severity levels. 
By default, the system filters out lower-severity messages and only records WARNING and above:
DEBUG (Numeric value: 10): Detailed diagnostic insights used mainly by developers during troubleshooting.
INFO (Numeric value: 20): Confirms that application milestones and general operations are running normally.
WARNING (Numeric value: 30): Alerts developers to unexpected events or potential issues that do not break the program.
ERROR (Numeric value: 40): Highlights major program faults, exceptions, or failures preventing a specific function from running.
CRITICAL (Numeric value: 50): Reports fatal errors that may crash or completely stop the application
There are five commonly used Logging levels:
DEBUG
INFO
WARNING
ERROR
CRITICAL

'''
import logging

'''logging.basicConfig(level=logging.INFO)
logging.info("calling LLM")
logging.warning("This is a warning")
logging.error("something went wrong")
logging.debug("Detailed debuging information")
logging.critical("Application cannot continue")'''

## Note DEBUG log won't result in the output when INFO level present because the minimum level is INFO.
## Hence INFO logs to be commented for DEBUG logs

'''logging.basicConfig(level=logging.DEBUG)
logging.debug("Now debug information logs")'''

### Above DEBUG logging have to comment to reflect the below INFO log with Timestamps
#Add Timestamps
'''logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s | %(levelname)s |%(message)s ")

logging.info("Test the Timestamp display log")'''

## ⭐⭐ Create Your Own Logger ⭐⭐

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s | %(levelname)s | %(name)s |%(message)s ")
logger = logging.getLogger(__name__)
logger.info("Application is starting")
logger.warning("Slow response")
logger.error("Request failed")

## 7. Logging Exceptions ⭐⭐⭐⭐⭐

try :
    result=40/0

except: logger.exception("calucation error")    

print("Hello")
model="llama3.2"
logger.info(f"Using Modle:{model}")