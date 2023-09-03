"""
Purpose: 

Practice writing functions using positional and keyword arguments.
Practice logging functions using the util_datafun_logger module
Log each time the function is called (along with its arguments)
Log the result of each function just before you return the result

 ----------------------------------------------------------
 UNIT TESTS BELOW - SPECIFY CORRECT BEHAVIOR
 ----------------------------------------------------------

>>> sum_two(1,2)
3

>>> sum_two("hello"," world")
'hello world'

>>> sum_rectangle_list( [1,1,3,3] )
8

>>> transform_using_keyword_args_with_default_values()
'bea'

>>> transform_using_keyword_args_with_default_values(reverse=True)
'aeb'

>>> transform_using_keyword_args_with_default_values(input="hello", reverse=True)
'leh'

>>> sum_any_using_args(1,1,1,2)
5

>>> sum_any_with_keyword_arguments_kwargs(a=1,b=2,c=3)
6

@uses doctest - to verify our functions are correct
"""

import doctest
import math
import statistics


from util_logger import setup_logger
logger, logname = setup_logger(__file__)

# TODO: Add functions to get the unit tests to pass 
# TODO: Log each time the function is called (along with its arguments)
# TODO: Log the result of each function just before you return the result




# TODO: Fix this function to get just the first 3 letters (possibly reversed)

def sum_two(value1,value2):
    logger.info(f"CAllING sum_two{value1,value2}")

    result = value1+value2

    logger.info(f"The result is {result}")

    return result



def transform_using_keyword_args_with_default_values(input="bearcat", reverse=False):
     
     logger.info(f"CALLING transform_using_keyword_args_with_default_values(input={input},reverse={reverse})")

     result = (input[0:3])
     if reverse:
         result = (input[2::-1])

     logger.info(f"the result is {result}")

     return result

def sum_any_using_args(*args):
    logger.info(f"CAllING sum_any_using_args {args}")

    result = sum(args)

    logger.info(f"The result is {result}")

    return result

def sum_any_with_keyword_arguments_kwargs(**kwargs):
    logger.info(f"CAllING sum_any_using_args {kwargs}")

    result = sum(kwargs.values())

    logger.info(f"The result is {result}")

    return result

def sum_rectangle_list(list):
    
    logger.info(f"CAllING sum_rectangle_list{list}" )

    result = sum(list)

    logger.info(f"The result is {result}")

    return result



   
'''Return a string with just the first 3 letters of input string. 
    If reverse is True, reverse the first 3 letters. 
    If reverse is omitted or False, return the first 3 letters reversed. 
    @kwargs:
        input: a string, default "bearcat"
        reverse: a boolean, default False'''
    
    
    





if __name__ == "__main__":

    # -------------------------------------------------------------
    # Call some functions and execute code!
    # Nothing below here needs to change
    # -------------------------------------------------------------

    transform_using_keyword_args_with_default_values()
    transform_using_keyword_args_with_default_values(reverse=True)
    transform_using_keyword_args_with_default_values(input="hello", reverse=True)

    logger.info("===========================================================")
    logger.info("Running doctest.testmod() function to unit test our code")
    logger.info("===========================================================")
    logger.info("Testing the function")
    transform_using_keyword_args_with_default_values()
    sum_two(1,2)
    sum_two("hello"," world")
    sum_any_using_args(1,1,1,2)
    sum_any_with_keyword_arguments_kwargs(a=1,b=2,c=3)
    sum_rectangle_list([1,1,3,3])


    # Run doctest and log the results

    doctest_result = doctest.testmod()
    if doctest_result.failed == 0:
        logger.info("All tests passed!")
    else:
        logger.error(f"{doctest_result.failed} tests failed!")

    logger.info("Script complete. More info in the log file.")
        
