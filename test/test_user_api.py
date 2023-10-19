# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_atrocore.api.user_api import UserApi  # noqa: E501


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_relation_for_user(self) -> None:
        """Test case for add_relation_for_user

        Add relation for User  # noqa: E501
        """
        pass

    def test_create_user_item(self) -> None:
        """Test case for create_user_item

        Create a record of the User  # noqa: E501
        """
        pass

    def test_delete_user_item(self) -> None:
        """Test case for delete_user_item

        Delete a record of the User  # noqa: E501
        """
        pass

    def test_follow_user(self) -> None:
        """Test case for follow_user

        Follow the User stream  # noqa: E501
        """
        pass

    def test_get_linked_items_for_user_item(self) -> None:
        """Test case for get_linked_items_for_user_item

        Returns linked entities for the User  # noqa: E501
        """
        pass

    def test_get_list_of_user_items(self) -> None:
        """Test case for get_list_of_user_items

        Returns a collection of User records  # noqa: E501
        """
        pass

    def test_get_user_item(self) -> None:
        """Test case for get_user_item

        Returns a record of the User  # noqa: E501
        """
        pass

    def test_link_user(self) -> None:
        """Test case for link_user

        Link User to Entities  # noqa: E501
        """
        pass

    def test_mass_delete_user(self) -> None:
        """Test case for mass_delete_user

        Mass delete of User data  # noqa: E501
        """
        pass

    def test_mass_update_user(self) -> None:
        """Test case for mass_update_user

        Mass update of User data  # noqa: E501
        """
        pass

    def test_remove_relation_for_user(self) -> None:
        """Test case for remove_relation_for_user

        Remove relation for User  # noqa: E501
        """
        pass

    def test_unfollow_user(self) -> None:
        """Test case for unfollow_user

        Unfollow the User stream  # noqa: E501
        """
        pass

    def test_unlink_user(self) -> None:
        """Test case for unlink_user

        Unlink User from Entities  # noqa: E501
        """
        pass

    def test_update_user_item(self) -> None:
        """Test case for update_user_item

        Update a record of the User  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()