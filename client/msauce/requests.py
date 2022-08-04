import http.client, urllib.request, urllib.parse, urllib.error
import json
import pandas as pd

def courbeBAM(dateCourbe):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'c82aab0841e44c40a50c21605a2983bf',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'dateCourbe': dateCourbe,
    })

    try:
        conn = http.client.HTTPSConnection('api.centralbankofmorocco.ma')
        conn.request("GET", "/mo/Version1/api/CourbeBDT?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read() 
        jsondata = json.loads(data)
        conn.close()
        df = pd.DataFrame(jsondata)
        return df

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


