import json
import urllib.request
from swamp_hacks_GUI import *
url = 'https://data.ca.gov/api/3/action/datastore_search?resource_id=c6f760be-b94f-495e-aa91-2d8e6f426e11&limit=1400'  
fileobj = urllib.request.urlopen(url)
response_dict = json.loads(fileobj.read())

global data
data = response_dict["result"] # create new object data which holds the results from the response dict
data = data["records"]
