from datetime import datetime
import os, inspect

class Logger:
    def __init__(self, output_dir=None):
        self.file_name = f"{datetime.now()}.log.txt"
        self.directory_path = os.path.dirname(os.path.realpath(__file__))
        if output_dir is None:
            output_dir = self.directory_path
        self.output_dir = output_dir

    def log_action(self, action_text = None):
        if not os.path.exists(self.file_name):
            pass
        log_file_path = os.path.join(self.directory_path, self.file_name)
        log_text = f'{datetime.now()} | caller: {inspect.stack()[1].function} - {action_text}\n'

        log = open(log_file_path, "a")
        log.write(log_text)
        log.close()
        print(log_text)