import configparser, os
from .Logg import Logger

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
final_path = os.path.join(path, "config.ini")

log = Logger()

log.log_action('Initializing settings')

def read_config():
    config = configparser.ConfigParser()
    config.read(final_path)

    log.log_action('Read config file')

    debug_mode = config.getboolean('General', 'debug')
    log_level = config.get('General', "log_level")
    
    config_data = {
        'debug_mode': debug_mode,
        'log_level': log_level
    }
    return config_data