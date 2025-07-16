from .common import EndpointTemplate


class InvitationsEndpoints(EndpointTemplate):
    """
    API wrapper for InvitationsEndpoints.
    """

    def __init__(self, session):
        super().__init__(session)
        self.base_path = "invitations"

    def get_by_emails(self, emails: str | list[str], message, group):
        """
        Get invitations by email or email list.

        Args:
            emails (str or list[str]): Example: List [ "alice@example.org", "bob@example.org" ]

        Returns:
            Response: The response object resulting from the GET request.
        """
        raise NotImplementedError
