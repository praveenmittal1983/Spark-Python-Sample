import logging, logging.config
import json

def setLoggerContext():
    with open('.\\common\\log.json', 'r') as f:
        log_Configuration = json.load(f)

    logging.config.dictConfig(log_Configuration)
    return logging.getLogger('MyApp')

## Testing
# logger = setLoggerContext()
# logger.info("Starting application {}".format(__name__))

# logger.info('This is an info message')
# logger.error('This is an error message')