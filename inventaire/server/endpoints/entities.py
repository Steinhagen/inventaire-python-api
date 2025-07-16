from inventaire.utils.common import dict_merge, str_bool

from .common import EndpointTemplate


class EntitiesEndpoints(EndpointTemplate):
    """
    Api wrapper for Entities. Think books, authors, series data. See:
    - entities map: https://inventaire.github.io/entities-map/
    - code: https://github.com/inventaire/inventaire/blob/master/server/controllers/entities/entities.js
    """

    def __init__(self, session):
        super().__init__(session)
        self.base_path = "entities"

    def create_entity(
        self,
        labels: dict,
        claims: dict,
        data: dict | None = None,
    ):
        """
        Create an entity.

        Parameters:
            labels (dict): An object with lang as key, and the associated label as value. e.g.:
                {
                  "en": "that entity's label in English",
                  "fr": "le label de cette entité en français"
                }
            claims (dict): An object with properties URIs as keys, and, as value, the associated array of claim values. e.g.:
                { "wdt:P31": [ "wd:Q571" ] }
            data (dict, optional): Additional parameters to include in the request.

        Returns:
            Response: The HTTP response object from the POST request.
        """
        if data is None:
            data = {}

        json = {"labels": labels, "claims": claims}
        json = dict_merge(data, json)
        return self.session.post(self._path("create"), json=json)

    def resolve_entity(
        self,
        entries: list,
        create: bool = True,
        update: bool = True,
        enrich: bool = True,
        data: dict | None = None,
    ):
        """
        Find if some entries match existing entities, and optionnaly update and/or enrich the existing entities, and/or create the missing ones.

        Parameters:
            entries (list): An object with a key "entries" and an array of objects as value. Each object can contain keys "edition", "works" and/or "authors". "edition" must be an object. "works" and "authors" must be arrays of one or several objects.
            create (bool, optional): If True, non-resolved entities will be created.
            update (bool, optional): If True, resolved entities will be updated.
            enrich (bool, optional): If True, resolved entities might be enriched with corresponding data found from other data sources. For instance an edition cover might be added, based on the provided ISBN.
            data (dict, optional): Additional parameters to include in the request.

        Returns:
            Response: The HTTP response object from the POST request.
        """
        if data is None:
            data = {}

        params = {
            "entries": entries,
            **{
                k: v
                for k, v in {
                    "create": str_bool(create),
                    "update": str_bool(update),
                    "enrich": str_bool(enrich),
                }.items()
                if v is not None
            },
        }
        params = dict_merge(data, params)
        return self.session.post(self._path("resolve"), json=params)

    def update_label(self, **params):
        """
        Update an entity's label.
        """
        raise NotImplementedError

    def update_claim(
        self,
        uri: str,
        property: str,
        old_value: str | None = None,
        new_value: str | None = None,
    ):
        """
        Update an entity's claim.

        Parameters:
            uri (str): An entity URI (e.g. 'wd:Q2196')
            property (str): The claim's property URI (e.g. 'wdt:P50')
            old_value (str, optional): The old value to be replaced. Can be omitted when intenting to create a new claim (e.g. 'wd:Q571')
            new_value (str, optional): The new value to be replaced. Can be omitted when intenting to delete a claim. (e.g. 'wd:Q2831984')

        Returns:
            Response: The response object to the PUT request.
        """
        params = {
            "uri": uri,
            "property": property,
            **{
                k: v
                for k, v in {
                    "old-value": old_value,
                    "new-value": new_value,
                }.items()
                if v is not None
            },
        }
        return self.session.put(self._path("update_claim"), json=params)

    def merge(self, from_entity: str, to_entity: str):
        """
        [authentified] Merge two entities.

        Parameters:
            from_entity (str): The uri from the local entity to be merged. Example: inv:9f25f75dba901ddb9817c3e4bf001d85
            to_entity (str): The uri from the local or remote entity in which the local "from" entity should be merged. Example: wd:Q191949

        Returns:
            Response: The response object to the PUT request.
        """
        params = {
            "from": from_entity,
            "to": to_entity,
        }
        return self.session.put(self._path("merge"), json=params)

    def revert_merge(self, **params):
        """
        Revert a merge. Requires to have dataadmin rights.
        """
        raise NotImplementedError

    def get_entities_by_uris(
        self,
        uris: str,
        refresh: bool | None = None,
        autocreate: bool | None = None,
        data: dict | None = None,
    ):
        """
        Get entities by URIs.

        Parameters:
            uris (str): A title, author, or ISBN (e.g. 'wd:Q3203603|isbn:9782290349229')
            refresh (bool, optional): Request non-cached data.
            autocreate (bool, optional): If True, create an item if it doesn't exist.
            data (dict, optional): Additional parameters to include in the request.

        Returns:
            Response: The response object from the GET request.
        """
        if data is None:
            data = {}

        params = {
            "uris": uris,
            **{
                k: v
                for k, v in {
                    "refresh": str_bool(refresh),
                    "autocreate": str_bool(autocreate),
                }.items()
                if v is not None
            },
        }
        params = dict_merge(data, params)
        return self.session.get(self._path("by-uris"), params=params)

    def get_entities_by_claims(self, **params):
        """
        Get entities URIs by their claims.
        """
        raise NotImplementedError

    def get_popularity(self, uris: str | list[str], refresh: bool = False):
        """
        Get popularity score of an entity.

        Args:
            uris (str or list[str]): A title, author, or ISBN separated by pipes or a list of elements (e.g., 'wd:Q3203603|isbn:9782290349229|inv:d59e3e64f92c6340fbb10c5dcf437d86').
            refresh (bool, optional): Request non-cached data. Defaults to 'False'.

        Returns:
            Response: The response object from the GET request.
        """
        params = {"uris": "|".join(uris) if isinstance(uris, list) else uris}
        if refresh:
            params["refresh"] = str_bool(refresh)
        return self.session.get(self._path("popularity"), params=params)

    def get_history(self, id: str):
        """
        Get entities history as snapshots and diffs.

        Args:
            id (str): An (internal) entity id (e. g., 'd59e3e64f92c6340fbb10c5dcf437d86').

        Returns:
            Response: The response object from the GET request.
        """
        params = {"id": id}
        return self.session.get(self._path("history"), params=params)

    def get_author_works(self, uri: str, refresh: bool = False):
        """
        Pass an author URI, get uris of all works, series and articles of the entity that match this claim

        Args:
            uri (str): An author URI (e. g. 'wd:Q2196').
            refresh (bool, optional): Request non-cached data. Defaults to 'False'.

        Returns:
            Response: The response object from the GET request.
        """
        params = {"uri": uri}
        if refresh:
            params["refresh"] = str_bool(refresh)
        return self.session.get(self._path("author-works"), params=params)

    def get_serie_parts(self, uri: str, refresh: bool = False):
        """
        Get a serie's parts.

        Args:
            uri (str): A serie URI (e. g. 'wd:Q718449').
            refresh (bool, optional): Request non-cached data. Defaults to 'False'.

        Returns:
            Response: The response object from the GET request.
        """
        params = {"uri": uri}
        if refresh:
            params["refresh"] = str_bool(refresh)
        return self.session.get(self._path("serie-parts"), params=params)

    def get_publisher_publications(self, **params):
        """
        Get the publications of a publisher.
        """
        raise NotImplementedError

    def revert_edit(self, **params):
        """
        Revert an entity edit.
        """
        raise NotImplementedError

    def restore_version(self, **params):
        """
        Restores an entity to a past version.
        """
        raise NotImplementedError

    def move_to_wikidata(self, uri: str):
        """
        Move an inventaire entity to Wikidata.

        Args:
            uri (str): Entity URI (e.g., 'inv:60044095fc153704829f47af07a1517e').

        Returns:
            Response: The response object resulting from the GET request to the shelves endpoint.
        """
        json = {"uri": uri}
        return self.session.put(self._path("move-to-wikidata"), json=json)
