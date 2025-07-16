from .common import EndpointTemplate


class UsersEndpoints(EndpointTemplate):
    """
    Api wrapper for Users. Read and edit authentified user data. See:
    - code: https://github.com/inventaire/inventaire/blob/master/server/controllers/users/users.js
    """

    def __init__(self, session):
        super().__init__(session)
        self.base_path = "users"

    def get_users_by_ids(self, ids: str | list[str]):
        """
        Users by ids.

        Args:
            ids (str or list[str]): Ids separated by pipes as a string or a list ids.

        Returns:
            Response: The response object resulting from the GET request.
        """
        ids_str = "|".join(ids) if isinstance(ids, list) else ids
        return self.session.get(self._path("by-ids"), params={"ids": ids_str})

    def get_users_by_usernames(self, usernames: str | list[str]):
        """
        Users by usernames.

        Args:
            usernames (str or list[str]): Usernames separated by pipes as a string or a list usernames.

        Returns:
            Response: The response object resulting from the GET request.
        """
        users_str = "|".join(usernames) if isinstance(usernames, list) else usernames
        return self.session.get(
            self._path("by-usernames"), params={"usernames": users_str}
        )

    def search(self, search):
        """
        Search users.

        Args:
            search (str): Text matching users username or bio.

        Returns:
            Response: The response object from the GET request.
        """
        params = {"search": search}
        return self.session.get(self._path("search"), params=params)
