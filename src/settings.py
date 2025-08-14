import configparser, os

# TODO: FIX logging 

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
final_path = os.path.join(path, "config.ini")

#log = Logger()

#log.log_action('Initializing settings')

def read_config():
    config = configparser.ConfigParser()
    config.read(final_path)

    #log.log_action('Read config file')

    debug_mode = config.getboolean('General', 'debug')
    log_level = config.get('General', "log_level")
    hide_elements = config.getboolean("General", "hide_elements")
    
    config_data = {
        'debug_mode': debug_mode,
        'log_level': log_level,
        'hide_elements': hide_elements
    }
    return config_data

def write_config():
    config = configparser.ConfigParser()
    # TODO: Remake elements value assignement
    config['General'] = {'debug': 'True', 'log_level': 'All', 'hide_elements': 'True'}
    config['DataBase'] = {'db_name': 'example_db'}

    with open(final_path, 'w') as configfile:
        config.write(configfile)
    
    return True