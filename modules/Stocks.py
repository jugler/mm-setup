# Stocks.py
from Cheetah.Template import Template
import file_utils


class Stocks:
    def __init__(self, config):
        self.config = config
        self.position = config.get('position')
        self.stocks = config.get('stocks')


    def to_config(self) -> str:
        templateDef = file_utils.readFile("templates/stocks.template")
        template = Template(templateDef)
        template.position = self.position
        template.stocks = self.stocks_format()
        return template

    def stocks_format(self) -> str:
        stock_list = self.stocks.split(",")
        stocks_str = ''
        for stock in stock_list:
            stocks_str = stocks_str + "'" + stock + "' ,"
        return stocks_str
