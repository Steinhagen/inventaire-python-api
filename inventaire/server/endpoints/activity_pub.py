from .common import EndpointTemplate


class ActivityPubEndpoints(EndpointTemplate):
    """
    API wrapper for ActivityPubEndpoints.
    """

    def get_activity(self, id: str):
        """
        Authenticate a user with the provided credentials.

        Args:
            id (str): An activity id. Example : 9f25f75dba901ddb9817c3e4bf001d85

        Returns:
            Response: The response object resulting from the GET request.
        """
        raise NotImplementedError
