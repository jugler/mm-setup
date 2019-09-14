# USHolidays.py
from Cheetah.Template import Template
import file_utils


class USHolidays:
    def __init__(self, config):
        self.config = config
        self.position = config.get('position')
        self.header = "US Holidays"
        self.calendar_url = "https://www.calendarlabs.com/templates/ical/US-Holidays.ics"
        self.max_entries = config.get("max_entries")


    def to_config(self) -> str:
        templateDef = file_utils.readFile("templates/calendar.template")
        t2 = Template(templateDef)
        t2.position = self.position
        t2.header = self.header
        t2.calendar_url = self.calendar_url
        t2.max_entries = self.max_entries
        return t2
