from inventaire.utils.common import dict_merge, str_bool

from .common import EndpointTemplate


class SearchEndpoints(EndpointTemplate):
    """
    Api wrapper for Search. The generalist search endpoint. See:
    - code: https://github.com/inventaire/inventaire/blob/master/server/controllers/search/search.js
    """

    def __init__(self, session):
        super().__init__(session)
        self.base_path = "search"

    def search(
        self,
        search: str,
        types: str = "works|series|humans",
        limit: int | None = None,
        lang: str | None = None,
        exact: bool | None = None,
        min_score: int | None = None,
        data: dict | None = None,
    ):
        """
        Search for entities (works, humans, genres, publishers, series, collections), users, or groups.

        Parameters:
            search (str): The search term or query string.
            types (str): A pipe-separated string of entity types to search for
                         (possible values: works, humans, genres, publishers, series, collections, genres, movements, languages, users, groups, shelves, lists). Defaults to "works|series|humans".
            limit (int, optional): Maximum number of results to return.
            lang (str, optional): Language code to filter results by language.
            exact (bool, optional): If True, perform an exact match search.
            min_score (int, optional): Minimum relevance score for filtering results.
            data (dict, optional): Additional parameters to include in the request.

        Returns:
            Response: The HTTP response object from the POST request.
        """
        if data is None:
            data = {}

        params = {
            "search": search,
            "types": types,
            **{
                k: v
                for k, v in {
                    "limit": limit,
                    "lang": lang,
                    "exact": str_bool(exact),
                    "min_score": min_score,
                }.items()
                if v is not None
            },
        }
        params = dict_merge(data, params)
        return self.session.get(self._path(), params=params)
