import logging
import time
from app import app

logger = logging.getLogger(__name__)

@app.task(queue="priority")
def notify_hello_work():
    logger.info("notifying hello world")

@app.task
def say_hello_world():
    time.sleep(5)
    logger.info("just saying hello world")