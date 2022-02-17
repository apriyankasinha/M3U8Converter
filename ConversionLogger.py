import logging

LOG_FORMATTER = logging.Formatter('{asctime} : {levelname:<8} : {message}', style='{')

def create_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(LOG_FORMATTER)
    stream_handler.setLevel(logging.INFO)
    return stream_handler

def create_log_handler():
    file_handler = logging.FileHandler('ConvertionLog.log',mode='w')
    file_handler.setFormatter(LOG_FORMATTER)
    file_handler.setLevel(logging.INFO)
    return file_handler

def create_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(create_stream_handler())
    logger.addHandler(create_log_handler())
    return logger
