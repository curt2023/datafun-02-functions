"""

Purpose: Illustrate the built-in statistics module.

VS Code Menu / View / Command Palette / Python Interpreter
Must be 3.10 or greater to get the correlation and linear regression.

Uses only Python Standard Library modules.

@ uses statistics module for descriptive stats
@ uses sys module for checking Python version

"""
# ----------------- INSTRUCTOR GENERATED CODE -----------------

# Use this handy logger to document your work automatically

# import setup_logger function from instructor-generated module
from util_logger import setup_logger

# setup the logger using the current file name (a built-in variable)
logger, logname = setup_logger(__file__)

# ----------------- END INSTRUCTOR GENERATED CODE -----------------


# Import from Python Standard Library

import statistics
import sys


xgames = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
yscores = [5,4,6,2,1,1,2,7,3,3,3,3,4,3,3,3,5,6,3,3]


total_score = sum(yscores)
number_games = max(xgames)

mean = statistics.mean(yscores)
mean = statistics.mean(yscores)
median = statistics.median(yscores)
mode = statistics.mode(yscores)

var = statistics.variance(yscores)
stdev = statistics.stdev(yscores)
lowest = min(yscores)
highest = max(yscores)



# if the lists are not the same size,
# log an error and quit the program
if len(xgames) != len(yscores):
    logger.error("ERROR: The related sets are not the same size.")
    logger.error(f"      {len(xgames)}!={len(yscores)}")
    quit()




logger.info("How'd we do? Does this make sense given the data?")

logger.info(f"Total points is {total_score}")
logger.info(f"Games played {number_games}")

logger.info(f"mean   = {mean:.1f}")
logger.info(f"median = {median:.1f}")
logger.info(f"mode   = {mode:.1f}")
logger.info(f"var    = {var:.2f}")
logger.info(f"stdev  = {stdev:.2f}")
logger.info(f"lowest = {lowest:.0f}")


