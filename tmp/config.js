/* Magic Mirror Config Sample
 *
 * By Michael Teeuw http://michaelteeuw.nl
 * MIT Licensed.
 *
 * For more information how you can configurate this file
 * See https://github.com/MichMich/MagicMirror#configuration
 *
 */

var config = {
	address: "", 
	port: 8080,
	ipWhitelist: [], 
	language: "en",

	modules: [
		{
			module: "alert",
		},
		{
			module: "updatenotification",
			position: "top_bar"
		},
		{
			module: "clock",
			position: "top_bar",
			config: {
				displaySeconds: false
			}
		},
		{
			module: "calendar",
			header: "Jesus Valen",
			position: "top_center",
			config: {
				maximumEntries: 5,
				calendars: [
					{
						symbol: "calendar-check-o ",
						url: "https://calendar.google.com/calendar/ical/jugler@gmail.com/public/basic.ics"
					}
				]
			}
		},
		{
			module: 'MMM-forecast-io',
			position: 'upper_third',  // This can be any of the regions.
			config: {
			  // See 'Configuration options' for more information.
			  apiKey: 'a89a155a3b70be18e9f62242206e1637', // Dark Sky API key.
			  // Only required if geolocation doesn't work:
			  latitude:   123123,
			  longitude: 123123123,
			  units: 'metric',
			  enablePrecipitationGraph: true
			}
		},
		{
    		module: "MMM-Stock",
    		position: "top_left",
    		config: {
    			companies: ['MSFT' ,]
    		}
		},

	]

};

/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") {module.exports = config;}
