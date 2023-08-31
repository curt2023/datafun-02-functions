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

        logger.info(f"CALLING get_total_points_scored({score_list})")

        try:
            total = sum(score_list)
            logger.info(f"Total points scored is {total}")
            return total
        except Exception as ex:
            logger.error(f"Error: {ex}")
            return None
        
def get_total_sale_cost(tickets_bought):
     logger.info(f"CAllING get_total_sale_cost({tickets_bought})")

     price = 120.56
     tax = .07

     try:
        sale_total = tickets_bought * price *tax *100
        logger.info(f"Total sale cost is {sale_total:.2f}")
        return sale_total
     except Exception as ex:
            logger.error(f"Error: {ex}")
            return None
     

def get_average_points_per_game(games_played):
     logger.info(f"CALLING: get_average_points_per_game({games_played})")

     try:
          average_points = sum(score_list) / games_played
          logger.info(f"Average points scored per game is {average_points:.2f}")
          return average_points
     except Exception as ex:
            logger.error(f"Error: {ex}")
            return None
     








# -------------------------------------------------------------
# Call some functions and execute code!


if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(2,1) = {math.comb(2,1)}")
    logger.info(f"math.perm(2,1) = {math.perm(2,1)}")


    logger.info("TRY: Call get_area_of_field() function with different values.")
    get_area_of_field(2,3)
    get_area_of_field(345,137)


    logger.info("TRY: get_total_point.")
    score_list = [5,3]
    get_total_points_scored(score_list)

    logger.info("TRY: get_total_sales_cost")
    get_total_sale_cost(10)

    logger.info("TRY: get_average_points_per_game")
    get_average_points_per_game(2)


    print("Done. Please check the log file for more details.")


