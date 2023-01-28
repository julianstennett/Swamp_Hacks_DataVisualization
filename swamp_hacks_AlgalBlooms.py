import json
import urllib.request
import swamp_hacks_Cl.cpp
url = 'https://data.ca.gov/api/3/action/datastore_search?resource_id=c6f760be-b94f-495e-aa91-2d8e6f426e11&limit=5'  
fileobj = urllib.request.urlopen(url)
response_dict = json.loads(fileobj.read())

data = response_dict["result"] # create new object data which holds the results from the response dict
data = data["records"]
print()

class AlgalBloom:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.lat = latitude
        self.lon = longitude


def DataClass():
    for i in range(len(data)):
        print(f"OfficialWaterBodyName: {data[i]['OfficialWaterBodyName']}")
        print(f"Latitude: {data[i]['Longitude']}")
        print(f"Longitude: {data[i]['Latitude']}")
        print()
