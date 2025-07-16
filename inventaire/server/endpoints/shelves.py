from inventaire.utils.common import dict_merge

from .common import EndpointTemplate


class ShelvesEndpoints(EndpointTemplate):
    """
    Api wrapper for Shelves. List of items.
    Items must belong to the shelf' owner.
    An owner can add or remove items from their own shelf.
    An owner must be a user.
    """

    def __init__(self, session):
        super().__init__(session)
        self.base_path = "shelves"

    def get_shelves_by_ids(self, ids: str | list[str]):
        """
        Retrieve shelf data for the given shelf IDs.

        Args:
            ids (str or list[str]): A shelf ID separated by pipes as a string or a list of shelf IDs.

        Returns:
            Response: The response object resulting from the GET request to the shelves endpoint.
        """
        ids_str = "|".join(ids) if isinstance(ids, list) else ids
        return self.session.get(self._path("by-ids"), params={"ids": ids_str})

    def get_shelves_by_owners(self, owners: str | list[str]):
        """
        Retrieve shelf data for the given owners ID.

        Args:
            ids (str or list[str]): A owner ID separated by pipes as a string or a list of owner IDs.

        Returns:
            Response: The response object resulting from the GET request to the shelves endpoint.
        """
        owners_str = "|".join(owners) if isinstance(owners, list) else owners
        return self.session.get(self._path("by-owners"), params={"owners": owners_str})

    def create_shelf(
        self, name: str, listing: str, description: str, data: dict | None = None
    ):
        """
        Create a new shelf with the given details.

        Args:
            name (str): The name of the shelf.
            listing (str): The shelf visibility listing: one of private, network, or public.
            description (str): A description of the shelf.
            data (dict, optional): Additional data to merge into the request payload.

        Returns:
            Response: The response object resulting from the POST request to create the shelf.
        """
        if data is None:
            data = {}

        json = {"name": name, "listing": listing, "description": description}
        merged_json = dict_merge(data, json)
        return self.session.post(self._path("create"), json=merged_json)

    def update_shelf(
        self,
        id: str,
        name: str,
        listing: str,
        description: str | None = None,
        data: dict | None = None,
    ):
        """
        Update an existing shelf with the given details.

        Args:
            id (str): The shelf ID.
            name (str): The name of the shelf.
            listing (str): The shelf visibility listing: one of private, network, or public.
            description (str, optional): A description of the shelf.
            data (dict, optional): Additional data to merge into the request payload.

        Returns:
            Response: The response object resulting from the POST request to create the shelf.
        """
        if data is None:
            data = {}

        json = {"id": id, "name": name, "listing": listing}
        if description:
            json["description"] = description
        merged_json = dict_merge(data, json)
        return self.session.post(self._path("update"), json=merged_json)

    def delete_shelf(self, id: str, data: dict | None = None):
        """
        Delete an existing shelf.

        Args:
            id (str): The shelf ID.
            data (dict, optional): Additional data to merge into the request payload.

        Returns:
            Response: The response object resulting from the POST request to create the shelf.
        """
        if data is None:
            data = {}

        json = {"id": id}
        merged_json = dict_merge(data, json)
        return self.session.post(self._path("delete"), json=merged_json)

    def add_items(self, **params):
        """
        Add items to a shelf.
        """
        raise NotImplementedError

    def remove_items(self, **params):
        """
        Remove items from a shelf.
        """
        raise NotImplementedError
