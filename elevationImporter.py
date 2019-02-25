import json
import urllib
import csv


def elevation(lat, lng):
    apikey = "GET YOU OWN KEY FROM THE GOOGLE ELEVATION API WEBSITE"
    url = "https://maps.googleapis.com/maps/api/elevation/json"
    request = urllib.urlopen(url+"?locations="+str(lat)+","+str(lng)+"&key="+apikey)
    try:
        results = json.load(request).get('results')
        if 0 < len(results):
            elevation = results[0].get('elevation')
            # ELEVATION
            return elevation
        else:
            print 'HTTP GET Request failed.'
    except ValueError, e:
        print 'JSON decode failed: '+str(request)
        
with open("nodeCSViSentYou.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(" ".join(row))
        #Get the colum for Lat and Long.
        #Plug it into the function above. 
        #Write it into the column for Elevation that already exists. 
