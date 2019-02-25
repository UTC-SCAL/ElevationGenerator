import json
import urllib

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
