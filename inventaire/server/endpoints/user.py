from .common import EndpointTemplate


class UserEndpoints(EndpointTemplate):
    """
    Api wrapper for Users. Read and edit authentified user data. See:
    - code: https://github.com/inventaire/inventaire/blob/master/server/controllers/user/user.js
    """

    def __init__(self, session):
        super().__init__(session)
        self.base_path = "user"

    def get_authentified_user(self):
        """
        Get the authentified user data.

        Returns:
            Response: The response object from the GET request.
        """
        return self.session.get(self._path())

    def update_authentified_user(self, attribute: str, value: str):
        """
        Update the authentified user.

        Args:
            attribute (str): The attribute to update (username, email, language, bio, settings, position).
            value (str): The new value to give to this attribute.

        Returns:
            Response: The response object from the PUT request.
        """
        json = {"attribute": attribute, "value": value}
        return self.session.put(self._path(), json=json)
