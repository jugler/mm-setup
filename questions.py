# questions.py
import wifi_utils

#wifiNetworks = [cell.ssid for cell in wifi_utils.Search()]

wifiNetworks = [ 'FortressOfSolitude', "Xfinity"]

questions = [
    {
        'type': 'list',
        'name': 'wifi_network',
        'message': 'Select the WiFi to connect to:',
        'choices': wifiNetworks
    },
    {
        'type': 'password',
        'name': 'wifi_password',
        'message': 'Type the password for the WiFi Network you want to use:',
    },
    {
        'type': 'list',
        'name': 'screen_rotate',
        'message': 'Do you want to rotate screen',
        'choices': ['0', '90', '180', '270']
    },
    {   
        'type': 'checkbox',
        'name': 'modules_to_install',
        'message': 'Select the modules/widgets to install',
        'choices': [
            {
                'name': 'Clock'
            },
            {
                'name': 'Calendar'
            },
            {
                'name': 'US holidays calendar'
            },
            {
                'name': 'Forecast'
            },
            {
                'name': 'Stocks'
            },
            {
                'name': "News Feed"
            },
            {
                'name': "Random Compliment"
            }
            #,
            # {
            #     'name': 'Uber Wait Time'
            # },
            # {
            #     'name': 'Lyft Wait Time'
            # }
            ]

    }
]
positions = {
        'type': 'list',
        'name': 'position',
        'message': 'Select the Position of the Module/Widget',
        'choices': ['top_bar', 'top_left', 'top_center', 'top_right', 'upper_third', 'middle_center', 'lower_third', 'bottom_left', 'bottom_center', 'bottom_right', 'bottom_bar', 'fullscreen_above', 'fullscreen_below']
    }

clock_questions = [
    positions,
    {
        'type': 'list',
        'name': 'time_format',
        'message': 'Time format',
        'choices': ['12 hour format (AM/PM)', '24 hour format']
    },
    {
        'type': 'confirm',
        'name': 'display_seconds',
        'message': 'Display Seconds',
        'default' : 'y'
    }
]

calendar_questions = [
    positions,
    {
        'type': 'input',
        'name': 'header',
        'message': 'Header for the Calendar'
    },
    {
        'type': 'input',
        'name': 'account',
        'message': 'Account to use in the calendar'
    },
    {
        'type': 'input',
        'name': 'max_entries',
        'message': 'Maximum entries to show'
    }
]
us_holiday_questions = [
    positions,
    {
        'type': 'input',
        'name': 'max_entries',
        'message': 'Maximum entries to show'
    }
]
latitude = {
    'type': 'input',
    'name': 'latitude',
    'message': 'Latitude location'
    }
longitude = {
    'type': 'input',
    'name': 'longitude',
    'message': 'Longitude location'
    }
forecast_questions = [
    positions,
    latitude,
    longitude,
    {
        'type': 'list',
        'name': 'units',
        'message': 'Units to show forecast info',
        'choices': ['metric','imperial']
    },

]
 
stocks_questions = [
    positions,
    {
        'type': 'input',
        'name': 'stocks',
        'message': 'Stock Symbols (comma sepparated)'
    }
]

uber_questions = [
    positions,
    latitude,
    longitude,
    {
        'type': 'checkbox',
        'name': 'ride_type',
        'message': 'Select the type of ride you want to know',
        'choices': [
            {'name':'UberX'},{'name': 'UberPool'},{'name': 'UberXL'},{'name':'Select'},{'name':'Black'},{'name':'Black SUV'}
        ]
    }
]

lyft_questions = [
    positions,
    latitude,
    longitude,
    {
        'type': 'checkbox',
        'name': 'ride_type',
        'message': 'Select the type of ride you want to know',
        'choices': [
            {'name':'Lyft'},{'name':'Lyft Plus'},{'name':'Lyft Line'},{'name':'Premier'},{'name':'Lyft Lux'},{'name':'Lyft Lux SUV'}
        ]
    }
]

news_feed_questions = [
    positions,
    {
        'type': 'checkbox',
        'name': 'selected_feeds',
        'message': 'Select the news feed you want to follow',
        'choices': [
            {'name':'New York Times'},{'name':'BBC'},{'name':'custom'}
        ]
    }
]
custom_feed_questions = [
    {
        'type':'input',
        'name':'custom_feed',
        'message': 'Title of the custom news feed'
    },
        {
        'type':'input',
        'name':'custom_feed_url',
        'message': 'Full URL of the feed to track (e.g. http://www.nytimes.com/services/xml/rss/nyt/HomePage.xml)'
    }
]

random_compliment_questions = [
    positions   
]

restart_question = [
    {
        'type': 'confirm',
        'name': 'restart',
        'message': 'Restart now?',
        'default' : True
    }
]
