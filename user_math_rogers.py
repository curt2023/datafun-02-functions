"""

Name: Curtis Rogers
Date: 8/31/2023

Purpose: Is to use the examples provided in Module 2 to create defensive functions
and if they do not work to provide a custom message



"""
import math

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

def get_area_of_field(height,width):
    logger.info(f"CALLING get_field_area{height,width}")

    try:
        area = height * width
        logger.info(f"The field area is {area}ft")
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None


def get_total_points_scored(score_list):

        logger.info(f"CALLING get_circle_area({score_list})")

        try:
            total = sum(score_list)
            logger.info(f"Total points scored is {total}")
            return total
        except Exception as ex:
            logger.error(f"Error: {ex}")
            return None


def get_circle_area_given_radius(radius):

    # Use a try / except / finally block when something 
    # could go wrong
    logger.info(f"CALLING get_circle_area({radius})")

    try: 
        area = 4 * math.pi * radius
        logger.info(f"The circle area is {area}")
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None



# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# Literally: "if this module name == the name of the main running module"
# (as opposed to being imported by another module like we do the logger),
# then, follow these instructions.
if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(2,1) = {math.comb(2,1)}")
    logger.info(f"math.perm(2,1) = {math.perm(2,1)}")


    logger.info("TRY: Call get_area_of_field() function with different values.")
    get_area_of_field(2,3)
    get_area_of_field(345,137)


    logger.info("TRY: get_total.")
    season_score_list = [5,3]
    get_total_points_scored(season_score_list)


    print("Done. Please check the log file for more details.")


