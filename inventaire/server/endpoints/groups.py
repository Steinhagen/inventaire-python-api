from .common import EndpointTemplate


class GroupsEndpoints(EndpointTemplate):
    """
    Api wrapper for Groups. Read and edit users groups data. See:
    - code: https://github.com/inventaire/inventaire/blob/master/server/controllers/groups/groups.js
    """

    def __init__(self, session):
        super().__init__(session)
        self.base_path = "groups"

    def get_groups(self, **params):
        """
        Get all the groups the authentified user is a member of.

        Returns:
            Response: The response object from the GET request.
        """
        return self.session.get(self._path())

    def get_group_by_id(self, id: str):
        """
        Get a group by its id.

        Args:
            id (str): A group id (e. g. '85d797f862e362335f3e6144cc12568a').

        Returns:
            Response: The response object from the GET request.
        """
        params = {"id": id}
        return self.session.get(self._path("by-id"), params=params)

    def get_group_by_slug(self, slug: str):
        """
        Get a group by its slug.

        Args:
            slug (str): A group slug (e. g. 'la-myne').

        Returns:
            Response: The response object from the GET request.
        """
        params = {"slug": slug}
        return self.session.get(self._path("by-slug"), params=params)

    def get_groups_by_username(self, **params):
        """
        Groups by usernames.
        """
        raise NotImplementedError

    def invite(self, **params):
        """
        Invite a user to join the group.
        """
        raise NotImplementedError

    def accept(self, **params):
        """
        Accept an invitation to join a group.
        """
        raise NotImplementedError

    def decline(self, **params):
        """
        Decline an invitation to join a group.
        """
        raise NotImplementedError

    def request(self, **params):
        """
        Request to join the group.
        """
        raise NotImplementedError

    def cancel_request(self, **params):
        """
        Cancel the authentified user request to join a group.
        """
        raise NotImplementedError

    def accept_request(self, **params):
        """
        Accept a user request to join the group.
        """
        raise NotImplementedError

    def refuse_request(self, **params):
        """
        Refuse a user request to join the group.
        """
        raise NotImplementedError

    def make_admin(self, **params):
        """
        Give admin right to a non-admin member.
        """
        raise NotImplementedError

    def kick(self, **params):
        """
        Remove a user from the group.
        """
        raise NotImplementedError

    def leave_group(self, **params):
        """
        Leave a group.
        """
        raise NotImplementedError

    def update_group_settings(self, **params):
        """
        Update the group settings.
        """
        raise NotImplementedError
