# Forecast.py
from Cheetah.Template import Template
import file_utils


class Forecast:
    def __init__(self, config):
        self.config = config
        self.position = config.get('position')
        self.latitude = config.get('latitude')
        self.longitude = config.get('longitude')
        self.units = config.get("units")


    def to_config(self) -> str:
        templateDef = file_utils.readFile("templates/forecast.template")
        template = Template(templateDef)
        template.position = self.position
        template.latitude = self.latitude
        template.longitude = self.longitude
        template.units = self.units
        return template
