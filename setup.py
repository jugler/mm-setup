#!/usr/bin/env python


from __future__ import print_function, unicode_literals
from PyInquirer import prompt, Separator
from pprint import pprint

import questions, wifi_utils, raspberry_utils, config
from modules import Clock, Calendar, USHolidays, Forecast, Stocks, NewsFeed, RandomCompliment
import subprocess

from shutil import copyfile




def main():
    user_input = prompt(questions.questions)
    pprint(user_input)
    #wifi_utils.setup_wifi(user_input.get("wifi_network"), user_input.get("wifi_password"))
    #raspberry_utils.rotate_screen(user_input.get("screen_rotate"))
    configure_modules(user_input.get("modules_to_install"))

    print("Configuration saved!, a restart is needed to apply changes")
    print("Moving configuration to MagicMirror Directory")
    copyfile("tmp/config.js", "/home/pi/MagicMirror/config/config.js")
    
    # activate pm2 activate mm if it isnt
    # restart whole pi to apply changes (screen, wifi, magic mirror config)
    subprocess.call(['pm2','start','/home/pi/mm.sh'])
    subprocess.call(['pm2','save'])
    print("Restarting MagicMirror")
    #subprocess.call(['/usr/bin/pm2','restart','mm'])
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
        if module == 'News Feed':
            news_feed_config = prompt(questions.news_feed_questions)
            pprint(news_feed_config)
            news_feed_module = NewsFeed.NewsFeed(news_feed_config)
            if 'custom' in news_feed_config.get('selected_feeds'):
                custom_feed_config = prompt(questions.custom_feed_questions)
                pprint(custom_feed_config)
                news_feed_module.add_custom_feed(custom_feed_config)
            cfg.add_module(news_feed_module)
        if module == 'Random Compliment':
            random_compliment_config = prompt(questions.random_compliment_questions)
            pprint(random_compliment_config)
            random_compliment_module = RandomCompliment.RandomCompliment(random_compliment_config)
            cfg.add_module(random_compliment_module)
    cfg.build_config_str()



# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()