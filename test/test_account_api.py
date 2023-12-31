# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_atrocore.api.account_api import AccountApi  # noqa: E501


class TestAccountApi(unittest.TestCase):
    """AccountApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccountApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_relation_for_account(self) -> None:
        """Test case for add_relation_for_account

        Add relation for Account  # noqa: E501
        """
        pass

    def test_create_account_item(self) -> None:
        """Test case for create_account_item

        Create a record of the Account  # noqa: E501
        """
        pass

    def test_delete_account_item(self) -> None:
        """Test case for delete_account_item

        Delete a record of the Account  # noqa: E501
        """
        pass

    def test_follow_account(self) -> None:
        """Test case for follow_account

        Follow the Account stream  # noqa: E501
        """
        pass

    def test_get_account_item(self) -> None:
        """Test case for get_account_item

        Returns a record of the Account  # noqa: E501
        """
        pass

    def test_get_linked_items_for_account_item(self) -> None:
        """Test case for get_linked_items_for_account_item

        Returns linked entities for the Account  # noqa: E501
        """
        pass

    def test_get_list_of_account_items(self) -> None:
        """Test case for get_list_of_account_items

        Returns a collection of Account records  # noqa: E501
        """
        pass

    def test_link_account(self) -> None:
        """Test case for link_account

        Link Account to Entities  # noqa: E501
        """
        pass

    def test_mass_delete_account(self) -> None:
        """Test case for mass_delete_account

        Mass delete of Account data  # noqa: E501
        """
        pass

    def test_mass_update_account(self) -> None:
        """Test case for mass_update_account

        Mass update of Account data  # noqa: E501
        """
        pass

    def test_remove_relation_for_account(self) -> None:
        """Test case for remove_relation_for_account

        Remove relation for Account  # noqa: E501
        """
        pass

    def test_unfollow_account(self) -> None:
        """Test case for unfollow_account

        Unfollow the Account stream  # noqa: E501
        """
        pass

    def test_unlink_account(self) -> None:
        """Test case for unlink_account

        Unlink Account from Entities  # noqa: E501
        """
        pass

    def test_update_account_item(self) -> None:
        """Test case for update_account_item

        Update a record of the Account  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
