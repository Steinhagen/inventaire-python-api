from inventaire.session import InventaireSession


class EndpointTemplate:
    """Class with basic constructor for endpoint classes"""

    def __init__(self, session: InventaireSession):
        self.session = session
        self.base_path = None

    def _path(self, action: str | None = None, base: str | None = None) -> str:
        """
        Return the API endpoint for a specific function.

        Args:
            action (str, optional): The action for the API endpoint. If None, the return will be only the base API endpoint. Example: "create"
            base (str, optional): Force a different base API endpoint than the one the class uses. Normally, you wouldn't need to do this. Example: "data-experimental"

        Returns:
            Response: The response object resulting from the GET request.
        """
        if not base:
            base = self.base_path

        if not base:
            raise ValueError("The base path for this endpoint was not set!")

        if action:
            return f"{base}?action={action}"
        return base
