"""
Author: Aidan Kiser
Version: 28 November 2024
"""

import logging
import random
import string

# Configure logging to both console and file
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(message)s",
    handlers=[
        logging.FileHandler("fuzz_log.txt"),
        logging.StreamHandler()
    ]
)

# Method placeholders for fuzz testing
# Testing github
def getAllSLOC(code):
    return len(code.split('\n'))

def getFileLength(file_content):
    return len(file_content)

def checkLoggingPerData(data):
    if "log" in data:
        return True
    return False

def getModelLoadCount(data):
    return data.count("model")

def runFameML(repo_url):
    if "http" in repo_url:
        return "Repository analyzed"
    return "Invalid URL"

# Helper function to generate random strings
def random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

if __name__ == "__main__":
    logging.info("Starting fuzz testing...")

    # Fuzz getAllSLOC
    for _ in range(5):
        code = random_string(50) + "\n" + random_string(50)
        try:
            result = getAllSLOC(code)
            logging.info(f"getAllSLOC('{code[:20]}...') = {result}")
        except Exception as e:
            logging.error(f"Error in getAllSLOC('{code[:20]}...'): {e}")

    # Fuzz getFileLength
    for _ in range(5):
        file_content = random_string(100)
        try:
            result = getFileLength(file_content)
            logging.info(f"getFileLength('{file_content[:20]}...') = {result}")
        except Exception as e:
            logging.error(f"Error in getFileLength('{file_content[:20]}...'): {e}")

    # Fuzz checkLoggingPerData
    for _ in range(5):
        data = random_string(50)
        try:
            result = checkLoggingPerData(data)
            logging.info(f"checkLoggingPerData('{data[:20]}...') = {result}")
        except Exception as e:
            logging.error(f"Error in checkLoggingPerData('{data[:20]}...'): {e}")

    # Fuzz getModelLoadCount
    for _ in range(5):
        data = "model " * random.randint(1, 10)
        try:
            result = getModelLoadCount(data)
            logging.info(f"getModelLoadCount('{data[:20]}...') = {result}")
        except Exception as e:
            logging.error(f"Error in getModelLoadCount('{data[:20]}...'): {e}")

    # Fuzz runFameML
    for _ in range(5):
        repo_url = random.choice(["http://github.com/repo", "invalid_url"])
        try:
            result = runFameML(repo_url)
            logging.info(f"runFameML('{repo_url}') = {result}")
        except Exception as e:
            logging.error(f"Error in runFameML('{repo_url}'): {e}")

    logging.info("Fuzz testing completed.")