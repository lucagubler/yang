import sys, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'Accept': "application/yang-data+json",
    'Content-Type': "application/yang-data+json",
    'Authorization': "Basic aW5zOmluc0BsYWI=",
    }

def printApiResponse(response):
    # dirty workaround because I'm too dumb: for every code above 200 throw an error!
    if response.status_code > 299:
        print('ERROR while executing action on REST API:\nError Code: ' + str(response.status_code)  + '\nError Message: ' + response.text)
        sys.exit(7)
    else:
        print('API call status: OK!\n')
