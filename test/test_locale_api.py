# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_atrocore.api.locale_api import LocaleApi  # noqa: E501


class TestLocaleApi(unittest.TestCase):
    """LocaleApi unit test stubs"""

    def setUp(self) -> None:
        self.api = LocaleApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_relation_for_locale(self) -> None:
        """Test case for add_relation_for_locale

        Add relation for Locale  # noqa: E501
        """
        pass

    def test_create_locale_item(self) -> None:
        """Test case for create_locale_item

        Create a record of the Locale  # noqa: E501
        """
        pass

    def test_delete_locale_item(self) -> None:
        """Test case for delete_locale_item

        Delete a record of the Locale  # noqa: E501
        """
        pass

    def test_follow_locale(self) -> None:
        """Test case for follow_locale

        Follow the Locale stream  # noqa: E501
        """
        pass

    def test_get_linked_items_for_locale_item(self) -> None:
        """Test case for get_linked_items_for_locale_item

        Returns linked entities for the Locale  # noqa: E501
        """
        pass

    def test_get_list_of_locale_items(self) -> None:
        """Test case for get_list_of_locale_items

        Returns a collection of Locale records  # noqa: E501
        """
        pass

    def test_get_locale_item(self) -> None:
        """Test case for get_locale_item

        Returns a record of the Locale  # noqa: E501
        """
        pass

    def test_link_locale(self) -> None:
        """Test case for link_locale

        Link Locale to Entities  # noqa: E501
        """
        pass

    def test_mass_delete_locale(self) -> None:
        """Test case for mass_delete_locale

        Mass delete of Locale data  # noqa: E501
        """
        pass

    def test_mass_update_locale(self) -> None:
        """Test case for mass_update_locale

        Mass update of Locale data  # noqa: E501
        """
        pass

    def test_remove_relation_for_locale(self) -> None:
        """Test case for remove_relation_for_locale

        Remove relation for Locale  # noqa: E501
        """
        pass

    def test_unfollow_locale(self) -> None:
        """Test case for unfollow_locale

        Unfollow the Locale stream  # noqa: E501
        """
        pass

    def test_unlink_locale(self) -> None:
        """Test case for unlink_locale

        Unlink Locale from Entities  # noqa: E501
        """
        pass

    def test_update_locale_item(self) -> None:
        """Test case for update_locale_item

        Update a record of the Locale  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
