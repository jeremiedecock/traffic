import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import time
import json
from matplotlib.dates import DateFormatter

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

def getduration(myurl):
    content = urlopen(myurl).read().decode('utf8')
    data = json.loads(content)
    duration=data['rows'][0]['elements'][0]['duration_in_traffic']['value']
    return  duration/60.



origin='Orsay'
destination='Paris'
APIkey=np.genfromtxt('api.key',dtype='unicode')

myurl='https://maps.googleapis.com/maps/api/distancematrix/json?origins=%s&destinations=%s&departure_time=now&traffic_model=best_guess&key=%s'%(origin,destination,APIkey)
plot=False


waittime=180 # in secs

now= datetime.now()
endhour=21
endmin=0
end=now.replace(hour=endhour, minute=endmin,second=0,microsecond=0)

times=[]
durations=[]



if plot == True:
    fig,ax = plt.subplots(1, 1, figsize=(15,7.5))  
    ax.plot(now,35)
    ax.plot(end,80)
    fig.autofmt_xdate()
    formatter = DateFormatter('%H:%M')
    ax.xaxis.set_major_formatter(formatter)
    plt.ion()
    ax.set_xlabel('Time (mn)')
    ax.set_ylabel('Trip duration in current traffic')
    plt.draw()


myfile='traffic-archive/traffic_'+now.strftime('%Y-%m-%d')+'.dat'
f = open(myfile, 'w')
f.close()

print('\n \n')
print('NOW=', now)
print('END time =', end)
while now < end:
    date=datetime.now()
    datestr=date.strftime('%Y-%m-%d %H:%M:%S')
    duration=getduration(myurl)

    print( 'Trafic time at %s =>  %.1f mn'%(datestr, duration) )
    data='%s %.1f \n'%(datestr, duration)
    f = open(myfile, 'a')
    f.write(data)
    f.close()
    
    durations.append( duration )
    times.append( date )
    
    if plot == True:
        ax.plot(date, duration, 'ro')
        fig.autofmt_xdate()


    plt.pause(waittime)
    now= datetime.now()


