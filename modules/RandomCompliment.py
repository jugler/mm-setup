# RandomCompliment.py
from Cheetah.Template import Template
import file_utils




class RandomCompliment:
    def __init__(self, config):
        self.config = config
        self.position = config.get('position')
        


    def to_config(self) -> str:
        templateDef = file_utils.readFile("templates/randomcompliment.template")
        template = Template(templateDef)
        template.position = self.position
        return template
