import requests

def get_species_images(species_key, image_limit=3):
  print("Getting ... " + str(species_key))
  url = "https://api.gbif.org/v1/occurrence/search"
  params = {
    "taxonKey": species_key,
    "mediaType": "StillImage",
    "limit": image_limit
  }
  response = requests.get(url, params=params)
  if response.status_code != 200:
    return []
  images = []
  for occurrence in response.json().get("results", []):
    for media in occurrence.get("media", []):
      images.append(media.get("identifier"))
  return images


def search_species(query, dataset_key="d7dddbf4-2cf0-4f39-9b2a-bb099caae36c"):
  """Search species in GBIF based on query and return extracted info."""
  url = "https://api.gbif.org/v1/species/search"
  params = {"datasetKey": dataset_key, "q": query}
  headers = {"accept": "application/json"}

  # Send GET request
  response = requests.get(url, params=params, headers=headers)
  results = []

  # Check if request succeeded
  if response.status_code == 200:
    data = response.json()
    for animal in data["results"]:
      vernacular = None
      names = animal.get("vernacularNames")
      if names:
        vernacular = names[0].get("vernacularName")

        species_key = animal.get("key")
        image_urls = get_species_images(species_key)  # call your function here
        image_url = image_urls[0] if image_urls else None
        
        extracted = {
          "scientificName": animal.get("scientificName"),
          "authorship": animal.get("authorship"),
          "kingdom": animal.get("kingdom"),
          "habitats": animal.get("habitats"),
          "threatStatuses": animal.get("threatStatuses"),
          "extinct": animal.get("extinct"),
          "vernacularName": vernacular,
          "image": image_url
        }
        results.append(extracted)

  else:
    print("Request failed:", response.status_code)
  return results
  