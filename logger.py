import logging

def logger():    
    logging.basicConfig(filename='logger.log', level=logging.DEBUG)


if __name__=="__main__":
    logger()    

