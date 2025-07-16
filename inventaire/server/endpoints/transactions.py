from .common import EndpointTemplate


class TransactionsEndpoints(EndpointTemplate):
    """
    Api wrapper for Transactions. When users request each others items. See:
    - code: https://github.com/inventaire/inventaire/blob/master/server/controllers/transactions/transactions.js
    """

    def __init__(self, session):
        super().__init__(session)
        self.base_path = "transactions"

    def get_transactions(self):
        """
        Get the authentified user transactions data.

        Returns:
            Response: The response object resulting from the GET request to the shelves endpoint.
        """
        return self.session.get(self._path())

    def get_transaction_messages(self, transaction: str):
        """
        Get messages associated to a transaction.

        Args:
            transaction (str): A transaction id (e. g., '85d797f862e362335f3e6144cc12568a').

        Returns:
            Response: The response object from the GET request.
        """
        params = {"transaction": transaction}
        return self.session.get(self._path("get-messages"), params=params)
