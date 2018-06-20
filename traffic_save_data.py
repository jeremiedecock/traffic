#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import json

from datetime import datetime
from urllib.request import urlopen

# TODO: put the 4 next variables in an external configuration file
origin = 'Orsay'
destination = 'Paris'
request_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&departure_time=now&traffic_model=best_guess&key=%s' % (origin, destination, api_key)
wait_time_sec = 180  # in secs

def get_duration(request_url):
    content = urlopen(request_url).read().decode('utf8')
    data = json.loads(content)
    duration = data['rows'][0]['elements'][0]['duration_in_traffic']['value']
    return duration / 60.

# Get the Google Maps API private key
api_key = np.genfromtxt('api.key', dtype='unicode')

# TODO: improve the next 3 lines: set a duration instead a end time and make it configurable to be able to launch the script several times per day with different durations...
now = datetime.now()
end_hour, end_min = 13, 0
end = now.replace(hour=end_hour, minute=end_min, second=0, microsecond=0)

times = []
durations = []

# TODO: improve the next 3 lines (create the data file)...
data_file = 'traffic-archive/traffic_' + now.strftime('%Y-%m-%d') + '.csv'
fd = open(data_file, 'w')
fd.close()

print('\n\n')
print('NOW =', now)
print('END TIME =', end)

while now < end:
    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d %H:%M:%S")
    duration = get_duration(request_url)

    print("Trafic time at {}: {:0.1f} mn".format(date_str, duration))
    data = "{}: {:0.1f}\n".format(date_str, duration)

    fd = open(data_file, 'a')
    fd.write(data)
    fd.close()

    durations.append(duration)
    times.append(date)

    now = datetime.now()
