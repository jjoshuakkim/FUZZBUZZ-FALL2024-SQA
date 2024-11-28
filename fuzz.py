'''
Author: Aidan Kiser
Version: 28 November 2024
'''

import logging
from hypothesis import given, strategies as st

# Configure logging
logging.basicConfig(filename="fuzz_log.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

# Method placeholders for fuzz testing (import actual methods in production)
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

# Fuzzing functions
@given(st.text())
def fuzz_getAllSLOC(code):
    try:
        result = getAllSLOC(code)
        logging.info(f"getAllSLOC('{code[:20]}...') = {result}")
    except Exception as e:
        logging.error(f"Error in getAllSLOC('{code[:20]}...'): {e}")

@given(st.text())
def fuzz_getFileLength(file_content):
    try:
        result = getFileLength(file_content)
        logging.info(f"getFileLength('{file_content[:20]}...') = {result}")
    except Exception as e:
        logging.error(f"Error in getFileLength('{file_content[:20]}...'): {e}")

@given(st.text())
def fuzz_checkLoggingPerData(data):
    try:
        result = checkLoggingPerData(data)
        logging.info(f"checkLoggingPerData('{data[:20]}...') = {result}")
    except Exception as e:
        logging.error(f"Error in checkLoggingPerData('{data[:20]}...'): {e}")

@given(st.text())
def fuzz_getModelLoadCount(data):
    try:
        result = getModelLoadCount(data)
        logging.info(f"getModelLoadCount('{data[:20]}...') = {result}")
    except Exception as e:
        logging.error(f"Error in getModelLoadCount('{data[:20]}...'): {e}")

@given(st.text())
def fuzz_runFameML(repo_url):
    try:
        result = runFameML(repo_url)
        logging.info(f"runFameML('{repo_url}') = {result}")
    except Exception as e:
        logging.error(f"Error in runFameML('{repo_url}'): {e}")

if __name__ == "__main__":
    fuzz_getAllSLOC()
    fuzz_getFileLength()
    fuzz_checkLoggingPerData()
    fuzz_getModelLoadCount()
    fuzz_runFameML()