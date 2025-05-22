"""
Usage examples of Inventaire API wrappers.
"""

import logging

from inventaire import Inventaire

# Enable logging with level Debug for more verbosity
logging.basicConfig(level=logging.DEBUG)

# The type of login authorization
auth = {"username": "demo-user", "password": "abcde1-fghij2-klmno3"}

# Create an instance of Inventaire
inv = Inventaire.server_api(**auth)

# Get information about the authenticated user
auth_data = inv.api.user.get_authentified_user()
print(auth_data)

# Get the last public items modified
last_items = inv.api.items.get_last_public_items()
print(last_items)

# Get shelves information based on their ids
shelves_ids = inv.api.shelves.get_shelves_by_ids(
    ["b30491238f4a79a466c27418a2280c12", "0c490f3bc5ea9ab450bc24ff55151814"]
)
print(shelves_ids)

shelves_owners = inv.api.shelves.get_shelves_by_owners(
    ["9f030dba8b09fc500b220cff6a0df1ea"]
)
print(shelves_owners)

# Create a new shelf
new_shelf = inv.api.shelves.create_shelf(
    name="demo", listing="private", description="something"
)
print(new_shelf)

wiki_extract = inv.api.data.request_extract_wikipedia(lang="en", title="The Moonstone")
print(wiki_extract)

search_data = inv.api.search.search(search="moon", types="works", limit=2)
print(search_data)

# Get entity details and if it doesn't exist, try to create it
uri_details = inv.api.entities.get_entities_by_uris(
    uris="isbn:9789735087180",
    autocreate=True,
    refresh=True,
)
print(uri_details)

# Create a new inventaire collection, titled "Râsul lumii", with the romanian language and the "Humanitas" publisher
collection_name = "Râsul lumii"
claims = {
    "wdt:P31": ["wd:Q20655472"],
    "wdt:P1476": [collection_name],
    "wdt:P407": ["wd:Q7913"],
    "wdt:P123": ["wd:Q680566"],
    "wdt:P856": [],
    "wdt:P268": [],
    "wdt:P921": [],
    "wdt:P1581": [],
    "wdt:P1680": [],
    "wdt:P1889": [],
}
data = {"prefix": "inv"}
collection_data = inv.api.entities.create_entity(labels={}, claims=claims, data=data)
print(collection_data)

# Add a new title to an entity (if it doesn't already exist)
update_claim = inv.api.entities.update_claim(
    uri="inv:b61d78a24bd6d4a55eaade78d548366a",
    property="wdt:P856",
    new_value="https://humanitas.ro/humanitas-fiction/colectii/cocktail",
)
print(update_claim)
