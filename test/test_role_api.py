# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_atrocore.api.role_api import RoleApi  # noqa: E501


class TestRoleApi(unittest.TestCase):
    """RoleApi unit test stubs"""

    def setUp(self) -> None:
        self.api = RoleApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_relation_for_role(self) -> None:
        """Test case for add_relation_for_role

        Add relation for Role  # noqa: E501
        """
        pass

    def test_create_role_item(self) -> None:
        """Test case for create_role_item

        Create a record of the Role  # noqa: E501
        """
        pass

    def test_delete_role_item(self) -> None:
        """Test case for delete_role_item

        Delete a record of the Role  # noqa: E501
        """
        pass

    def test_follow_role(self) -> None:
        """Test case for follow_role

        Follow the Role stream  # noqa: E501
        """
        pass

    def test_get_linked_items_for_role_item(self) -> None:
        """Test case for get_linked_items_for_role_item

        Returns linked entities for the Role  # noqa: E501
        """
        pass

    def test_get_list_of_role_items(self) -> None:
        """Test case for get_list_of_role_items

        Returns a collection of Role records  # noqa: E501
        """
        pass

    def test_get_role_item(self) -> None:
        """Test case for get_role_item

        Returns a record of the Role  # noqa: E501
        """
        pass

    def test_link_role(self) -> None:
        """Test case for link_role

        Link Role to Entities  # noqa: E501
        """
        pass

    def test_mass_delete_role(self) -> None:
        """Test case for mass_delete_role

        Mass delete of Role data  # noqa: E501
        """
        pass

    def test_mass_update_role(self) -> None:
        """Test case for mass_update_role

        Mass update of Role data  # noqa: E501
        """
        pass

    def test_remove_relation_for_role(self) -> None:
        """Test case for remove_relation_for_role

        Remove relation for Role  # noqa: E501
        """
        pass

    def test_unfollow_role(self) -> None:
        """Test case for unfollow_role

        Unfollow the Role stream  # noqa: E501
        """
        pass

    def test_unlink_role(self) -> None:
        """Test case for unlink_role

        Unlink Role from Entities  # noqa: E501
        """
        pass

    def test_update_role_item(self) -> None:
        """Test case for update_role_item

        Update a record of the Role  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
