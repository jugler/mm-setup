# Clock.py
from Cheetah.Template import Template
import file_utils


class Clock:
    def __init__(self, config):
        if config.get('display_seconds'):
            self.display_seconds  = "true" 
        else:
            self.display_seconds  = "false"
        self.config = config
        self.position = config.get('position')
        if '12' in config.get('time_format'):
            self.time_format = 12
        else:
            self.time_format = 24

    def to_config(self) -> str:
        templateDef = file_utils.readFile("templates/clock.template")
        t2 = Template(templateDef)
        t2.position = self.position
        t2.display_seconds = self.display_seconds
        return t2
