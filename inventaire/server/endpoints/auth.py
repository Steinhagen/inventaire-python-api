from .common import EndpointTemplate


class AuthEndpoints(EndpointTemplate):
    """
    Api wrapper for Auth. Login and stuffs. See:
    - code: https://github.com/inventaire/inventaire/blob/master/server/controllers/auth/auth.js
    """

    def __init__(self, session):
        super().__init__(session)
        self.base_path = "auth"

    def login_user(self, username: str, password: str):
        """
        Authenticate a user with the provided credentials.

        Args:
            username (str): The user's username.
            password (str): The user's password.

        Returns:
            Response: The response object resulting from the POST request to the authentication endpoint.
        """
        json = {"username": username, "password": password}
        return self.session.post(self._path("login"), json=json)
