import logging

def api_error_handler(func):
    """
    API error handler. 
    Decorator object for simplifying code
    """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            logging.info(f"Error connecting to API: \n\n {err} \n\n")
            return None
    return wrapper