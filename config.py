# config.py
from modules import Clock, Calendar
import file_utils

from Cheetah.Template import Template

class Config:


    def __init__(self):
        self.modules = []

    def add_module(self, module):
        self.modules.append(module)
    
    def build_config_str(self) :
        templateDef = file_utils.readFile("templates/config.js.template")
        template = Template(templateDef)
        template.modules = self.build_modules()
        file_utils.writeFile("tmp/config.js", str(template))

    def build_modules(self) -> str:
        module_list: str = ''
        for module in self.modules:
            module_list = module_list + str(module.to_config()) + '\n'
        return module_list



