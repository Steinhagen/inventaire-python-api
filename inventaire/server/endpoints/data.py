from .common import EndpointTemplate


class DataEndpoints(EndpointTemplate):
    """
    Api wrapper for Data.
    """

    def __init__(self, session):
        super().__init__(session)
        self.base_path = "data"

    def request_extract_wikipedia(self, title: str, lang: str | None = None):
        """
        Request a summary extract from Wikipedia for a given article title and language.

        Args:
            title (str): The title of the Wikipedia article.
            lang (str, optional): The language code (e.g., 'en', 'fr') for the Wikipedia edition.

        Returns:
            Response: The response object from the GET request to retrieve the extract.
        """
        params = {"title": title}
        if lang:
            params["lang"] = lang
        return self.session.get(self._path("wp-extract"), params=params)

    def get_isbn_basic_facts(self, isbn: str):
        """
        An endpoint to get basic facts from an ISBN.

        Args:
            isbn (str): 10 or 13, with or without hyphen.

        Returns:
            Response: The response object from the GET request.
        """
        params = {"isbn": isbn}
        return self.session.get(self._path("isbn"), params=params)

    def get_property_values(self, property: str, type: str):
        """
        Return the allowed values per type for a given property.

        Args:
            property (str): A property (e. g., 'wdt:P31').
            type (str): A type from lib/wikidata/aliases (e. g., 'series').

        Returns:
            Response: The response object from the GET request.
        """
        params = {"property": property, "type": type}
        return self.session.get(self._path("property-values"), params=params)
