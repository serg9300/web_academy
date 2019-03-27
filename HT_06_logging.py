import logging

# add filemode="w" to overwrite
logging.basicConfig(filename="sample.log", filemode='w', level=logging.DEBUG)

# logging.debug("This is a debug message")
# logging.info("Informational message")
# logging.error("An error has happened!")

def log(x,y):
    logging.basicConfig(filename="sample.log", level=logging.INFO)
    logging.info("create function %s" % 'log')
    logging.info("multiply %s and %s, result1 %s" % (x,y, x*y))
    result1 = x*y
    logging.info("multiply %s and %s, result2 %s" % (x,x, x*x))
    result2 = x*x
    logging.info("finished function %s" % 'log')
    return result1, result2

print(log(5,6))