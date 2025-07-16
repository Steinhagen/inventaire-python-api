from inventaire.utils.common import str_bool

from .common import EndpointTemplate


class ImagesEndpoints(EndpointTemplate):
    """
    Undocumented Api wrapper for Images.
    """

    def __init__(self, session):
        super().__init__(session)
        self.base_path = "images"

    def get_data_url(self, url: str):
        """
        Returns the base64 data of an image.

        Args:
            url (str): Image URL.

        Returns:
            Response: The response object from the GET request.
        """
        params = {"url": url}
        return self.session.get(self._path("data-url"), params=params)

    def upload(
        self,
        image_path: str | None = None,
        image_data: bytes | None = None,
        container: str = "entities",
        hash: bool = True,
    ):
        """
        Upload an image cover to a entity.

        Args:
            image_path (str): Path to the cover image.
            image_data (str): Base64 of the desired image.
            container (str, optional): Location where the image gets uploaded. Default value: "entities"
            hash (bool, optional): Default value: "True"

        Returns:
            Response: The response object resulting from the POST request.
        """
        params = {"container": container, "hash": str_bool(hash)}
        return self.session.post_image(
            self._path("upload"),
            file_path=image_path,
            file_bytes=image_data,
            params=params,
        )
