import pytest

from inventaire.inventaire import DEFAULT_BASE_URL, Inventaire

ISESSION_PATH = "inventaire.inventaire.InventaireSession"
INVENTAIRE_API_WRAP_PATH = "inventaire.inventaire.InventaireApiWrapper"


@pytest.mark.unit
class TestInventaire:
    @pytest.mark.parametrize(
        "creation_kwargs, exp_url",
        [
            ({}, DEFAULT_BASE_URL),
            ({"base_url": DEFAULT_BASE_URL}, DEFAULT_BASE_URL),
            ({"base_url": "test.com"}, "test.com"),
        ],
    )
    def test_inventaire_session_creation(self, creation_kwargs, exp_url, mocker):
        session_mock = mocker.patch(ISESSION_PATH)
        mocker.patch(INVENTAIRE_API_WRAP_PATH)

        Inventaire(**creation_kwargs)

        session_mock.assert_called_once_with(base_url=exp_url)
