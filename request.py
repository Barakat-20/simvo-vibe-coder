import requests

# API endpoint
url = "https://api.gbif.org/v1/species/search"

# Query parameters
params = {
    "datasetKey": "d7dddbf4-2cf0-4f39-9b2a-bb099caae36c",
    "q": "parrot"
}

# Headers
headers = {
    "accept": "application/json"
}

# Send GET request
response = requests.get(url, params=params, headers=headers)

# Check if request succeeded
if response.status_code == 200:
  data = response.json()

  for animal in data["results"]:

    vernacular = None
    names = animal.get("vernacularNames")

    if names:
      vernacular = names[0].get("vernacularName")

    extracted = {
      "scientificName": animal.get("scientificName"),
      "authorship": animal.get("authorship"),
      "kingdom": animal.get("kingdom"),
      "habitats": animal.get("habitats"),
      "threatStatuses": animal.get("threatStatuses"),
      "vernacularName": vernacular
    }

    print(extracted)

else:
  print("Request failed:", response.status_code)