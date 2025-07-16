from inventaire.utils.common import dict_merge

from .common import EndpointTemplate


class ItemsEndpoints(EndpointTemplate):
    """
    Api wrapper for Items. What users' inventories are made of. See:
    - code: https://github.com/inventaire/inventaire/blob/master/server/controllers/items/items.js
    """

    def __init__(self, session):
        super().__init__(session)
        self.base_path = "items"

    def create_item(
        self,
        entity: str,
        transaction: str = "inventorying",
        listing: str = "private",
        lang: str | None = None,
        details: str | None = None,
        notes: str | None = None,
        data: dict | None = None,
    ):
        """
        Create an item.

        Parameters:
            entity (str): The associated book entity (work or edition) uri (e.g. 'isbn:9782253138938').
            transaction (str): The item transaction: one of giving, lending, selling, or inventorying. Defaults to inventorying.
            listing (str): The item visibility listing: one of private, network, or public. Defaults to private.
            lang (str, optional): 2-letters language code.
            details (str, optional): Free text to be visible by anyone allowed to see the item.
            notes (str, optional): Free text that is visible only by the item owner.
            data (dict, optional): Additional parameters to include in the request.

        Returns:
            Response: The HTTP response object from the POST request.
        """
        if data is None:
            data = {}

        json = {
            "entity": entity,
            **{
                k: v
                for k, v in {
                    "transaction": transaction,
                    "listing": listing,
                    "lang": lang,
                    "details": details,
                    "notes": notes,
                }.items()
                if v is not None
            },
        }
        json = dict_merge(data, json)
        return self.session.post(self._path(), json=json)

    def update_item(self, **params):
        """
        Update an item.
        """
        raise NotImplementedError

    def get_items_by_ids(self, **params):
        """
        Items by ids.
        """
        raise NotImplementedError

    def get_items_by_users(self, **params):
        """
        Items by users ids.
        """
        raise NotImplementedError

    def get_items_by_entities(self, **params):
        """
        Items by entities URIs.
        """
        raise NotImplementedError

    def get_last_public_items(self, **params):
        """
        Last public items.
        """
        return self.session.get(self._path("last-public"), params=params)

    def get_nearby_items(self, **params):
        """
        Last nearby items.
        """
        raise NotImplementedError

    def delete_item(self, **params):
        """
        Delete an item.
        """
        raise NotImplementedError
