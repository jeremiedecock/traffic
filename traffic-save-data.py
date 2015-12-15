import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import time
import urllib2
from matplotlib.dates import DateFormatter

def getduration(myurl):
    info = urllib2.urlopen(myurl)
    content = info.read()
    index=content.find('Dans les conditions actuelles de circulation')
    substring=content[index+47:index+61]
#    substring='1 heure 9 min'
    print substring
    index_min=substring.find('min') ; print index_min
    index_hour=substring.find('heure') ; print index_hour
    hours=0
    minutes=0
    if index_hour > 0:
        hours=substring[index_hour-2:index_hour-1]
        print 'hours = ', hours
    if index_min > 0:
        minutes=substring[index_min-3:index_min-1]
        print 'minutes = ', minutes
    duration = float(hours)*60 + float(minutes)    
    return  duration

myurl='https://www.google.fr/maps/dir/Orsay/Paris/'



waittime=180 # in secs

now= datetime.now()
endhour=20
endmin=00
end=now.replace(hour=endhour, minute=endmin,second=0,microsecond=0)

times=[]
durations=[]

# plt.plot(now,35)
# plt.plot(end,70)
# plt.gcf().autofmt_xdate()
# formatter = DateFormatter('%H:%M')
# plt.gcf().axes[0].xaxis.set_major_formatter(formatter)
# plt.ion()
# plt.xlabel('Time')
# plt.ylabel('Trip duration in current traffic')
# plt.show()


myfile='traffic-archive/traffic_'+now.strftime('%Y-%m-%d')+'.dat'
f = open(myfile, 'w')
f.close()

print 'NOW=', now
print 'END time =', end
while now < end:
    date=datetime.now()
    datestr=date.strftime('%Y-%m-%d %H:%M:%S')
    duration=getduration(myurl)

    print 'Trafic time at %s =>  %s min' %(datestr, duration)
    data='%s %s \n'%(datestr, duration)
    f = open(myfile, 'a')
    f.write(data)
    f.close()
    
    durations.append( duration )
    times.append( date )
#     plt.plot(date, duration, 'ro')
#     plt.gcf().autofmt_xdate()
#     plt.draw()

    
    time.sleep(waittime)
    now= datetime.now()


