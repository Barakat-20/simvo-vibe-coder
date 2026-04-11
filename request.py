import asyncio
import aiohttp

async def get_species_images(session, species_key, image_limit=3):
    url = "https://api.gbif.org/v1/occurrence/search"
    params = {"taxonKey": species_key, "mediaType": "StillImage", "limit": image_limit}
    try:
        async with session.get(url, params=params) as response:
            if response.status != 200:
                return []
            data = await response.json()
            images = []
            for occ in data.get("results", []):
                for media in occ.get("media", []):
                    images.append(media.get("identifier"))
            return images
    except Exception as e:
        print(f"Error fetching images for {species_key}: {e}")
        return []

async def search_species(query, dataset_key="d7dddbf4-2cf0-4f39-9b2a-bb099caae36c"):
    url = "https://api.gbif.org/v1/species/search"
    params = {"datasetKey": dataset_key, "q": query}
    headers = {"accept": "application/json"}

    async with aiohttp.ClientSession() as session:
        # --- async species search ---
        async with session.get(url, params=params, headers=headers) as resp:
            if resp.status != 200:
                print("Species search failed:", resp.status)
                return []
            data = await resp.json()
            animals = data.get("results", [])

            # --- async image fetch ---
            species_keys = [a.get("key") for a in animals]
            # Limit concurrency to avoid hammering GBIF
            semaphore = asyncio.Semaphore(10)

            async def sem_get_images(key):
                async with semaphore:
                    return await get_species_images(session, key)

            tasks = [sem_get_images(key) for key in species_keys]
            image_results = await asyncio.gather(*tasks)

            # --- combine results ---
            results = []
            for animal, images in zip(animals, image_results):
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
                    "extinct": animal.get("extinct"),
                    "vernacularName": vernacular,
                    "image": images[0] if images else None
                }
                results.append(extracted)
            return results

# Example usage
# asyncio.run(search_species("Macaca"))