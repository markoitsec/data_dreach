from intelxapi import intelx
import json
import datetime
from config import API,domain,time_delta

end_date = str(datetime.datetime.now())
start_date = str(datetime.datetime.now()-datetime.timedelta(time_delta))

#print(end_date,start_date)

intelx = intelx(API)
search_latest = intelx.search(domain,
                       maxresults = 10000,
                       dateto = end_date,
                       datefrom = start_date)
stats_latest = intelx.stats(search_latest)

search_history = intelx.search(domain,
                       maxresults = 10000)
stats_history = intelx.stats(search_history)
stats_history = json.loads(stats_history)
stats_latest = json.loads(stats_latest)

with open("data_breach_results.txt","w") as f:
    f.write ( "The investigated domain is "+str(domain)+("\r\n") )
    f.write ( "Number of leaked data in the last period: "+str(sum ( stats_latest.values () )) +("\r\n"))
    f.write ( "Total number of leaked data: " +str(sum ( stats_history.values () ) )+("\r\n"))
    f.write ( "Data to start investigation: "+str( search_latest.values () )+("\r\n"))
f.close()

