#!/usr/bin/env python


from __future__ import print_function, unicode_literals
from PyInquirer import prompt, Separator
from pprint import pprint

import questions, wifi_utils, raspberry_utils, config
from modules import Clock, Calendar, USHolidays, Forecast, Stocks



def main():
    user_input = prompt(questions.questions)
    pprint(user_input)
    #wifi_utils.setup_wifi(user_input.get("wifi_network"), user_input.get("wifi_password"))
    #raspberry_utils.rotate_screen(user_input.get("screen_rotate"))
    configure_modules(user_input.get("modules_to_install"))

    print("Configuration saved!, a restart is needed to apply changes")

    restart_input = prompt(questions.restart_question)


    if restart_input.get("restart"):
        raspberry_utils.restart_raspberry()

    exit




def configure_modules(modules):
    pprint(modules)
    cfg = config.Config()

    for module in modules:
        print (f"Configuring module {module}")
        if module == 'Clock':
            clock_config = prompt(questions.clock_questions)
            pprint(clock_config)
            clock_module = Clock.Clock(clock_config)
            cfg.add_module(clock_module)
        if module == 'Calendar':
            calendar_config = prompt(questions.calendar_questions)
            pprint(calendar_config)
            calendar_module = Calendar.Calendar(calendar_config)
            cfg.add_module(calendar_module)
        if module == 'US holidays calendar':
            us_holiday_calendar_config = prompt(questions.us_holiday_questions)
            pprint(us_holiday_calendar_config)
            calendar_module = USHolidays.USHolidays(us_holiday_calendar_config)
            cfg.add_module(calendar_module)
        if module == 'Forecast':
            forecast_config = prompt(questions.forecast_questions)
            pprint(forecast_config)
            forecast_module = Forecast.Forecast(forecast_config)
            cfg.add_module(forecast_module)
        if module == 'Stocks':
            stocks_config = prompt(questions.stocks_questions)
            pprint(stocks_config)
            stocks_module = Stocks.Stocks(stocks_config)
            cfg.add_module(stocks_module)
        if module == 'Uber Wait Time':
            uber_config = prompt(questions.uber_questions)
            pprint(uber_config)
        if module == 'Lyft Wait Time':
            lyft_config = prompt(questions.lyft_questions)
            pprint(lyft_config)
    cfg.build_config_str()



# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()