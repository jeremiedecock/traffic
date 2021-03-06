# Traffic

Estimate commuting time with traffic conditions using Google Maps API.
Saving the travel time every XX minutes to create a Traffic vs Time curve. 
The idea is to find the optimum time to leave from work and look for day, month, weather conditions correlation with traffic.

Request are submitted through the Google maps API. A key is required (see [here](https://developers.google.com/maps/documentation/javascript/get-api-key)).
A free account allows you to submit 2500 requests/day.

Go [there](https://console.developers.google.com/apis/dashboard) to watch the Google API dashboard.

Go [there](https://console.developers.google.com/apis/credentials/key/) to manage your Google API keys.

Use cron to launch the script periodically on a Unix system ```crontab -e```:

```
# Everyday at 16:00
0 16 * * *       python3 ~/traffic_save_data.py -c config_1.yaml

# Every week days at 7:30
30 7 * * 1-5     python3 ~/traffic_save_data.py -c config_2.yaml
```


Use ```crontab -l``` to check.

## Example

The following example show the aggregated trip duration measured during 2 months (weekdays only between 4pm and 8pm) on a small portion of a local road (near Paris in France).

<img src="example.png">
