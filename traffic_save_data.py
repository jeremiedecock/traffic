#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import json
import os
import yaml
import time
import argparse

from datetime import datetime
from urllib.request import urlopen

# TODO
# - allow multiple paths per request (+ mention the path id in the csv file...) -> one configuration file per path ?
# - set way points
# - finish the plot script

def get_duration(request_url):
    content = urlopen(request_url).read().decode('utf8')
    data = json.loads(content)
    #print(data)
    duration = data['rows'][0]['elements'][0]['duration_in_traffic']['value']
    return duration / 60.


def record_traffic(config):

    # Get the Google Maps API private key
    api_key = np.genfromtxt(config['google_maps_api_key'], dtype='unicode')

    request_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&departure_time=now&traffic_model=best_guess&key=%s' % (config['origin'], config['destination'], api_key)

    now = datetime.now()
    end_hour, end_min = config['end_time']['hour'], config['end_time']['minute']
    end_time = now.replace(hour=end_hour, minute=end_min, second=0, microsecond=0)

    data_file = "{}_{}.csv".format(config['path_id'], now.strftime('%Y-%m-%d_%H-%M'))
    data_path = os.path.join(config['data_directory'], data_file)

    # TODO: improve the next 2 lines (create the data file)...
    fd = open(data_path, 'w')
    fd.write("datetime,duration\n")
    fd.close()

    print()
    print("PATH = https://www.google.com/maps/dir/'{}'/'{}'/".format(config['origin'], config['destination']))
    print('NOW =', now)
    print('END TIME =', end_time)

    while now < end_time:
        date_str = datetime.now().isoformat()
        duration = get_duration(request_url)

        print("{} -> trafic time at {}: {:0.1f} mn".format(config['path_id'], date_str, duration))
        data = "{},{:0.1f}\n".format(date_str, duration)

        fd = open(data_path, 'a')
        fd.write(data)
        fd.close()

        time.sleep(config['wait_time_sec'])

        now = datetime.now()


def main():
    parser = argparse.ArgumentParser(description='An argparse snippet.')

    parser.add_argument("--config", "-c", required=True, metavar="STRING",
            help="The path of the YAML configuration file.")

    args = parser.parse_args()

    with open(args.config) as stream:
        config_dict = yaml.load(stream)

    record_traffic(config_dict)

if __name__ == '__main__':
    main()

