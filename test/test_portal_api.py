# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_atrocore.api.portal_api import PortalApi  # noqa: E501


class TestPortalApi(unittest.TestCase):
    """PortalApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PortalApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_relation_for_portal(self) -> None:
        """Test case for add_relation_for_portal

        Add relation for Portal  # noqa: E501
        """
        pass

    def test_create_portal_item(self) -> None:
        """Test case for create_portal_item

        Create a record of the Portal  # noqa: E501
        """
        pass

    def test_delete_portal_item(self) -> None:
        """Test case for delete_portal_item

        Delete a record of the Portal  # noqa: E501
        """
        pass

    def test_follow_portal(self) -> None:
        """Test case for follow_portal

        Follow the Portal stream  # noqa: E501
        """
        pass

    def test_get_linked_items_for_portal_item(self) -> None:
        """Test case for get_linked_items_for_portal_item

        Returns linked entities for the Portal  # noqa: E501
        """
        pass

    def test_get_list_of_portal_items(self) -> None:
        """Test case for get_list_of_portal_items

        Returns a collection of Portal records  # noqa: E501
        """
        pass

    def test_get_portal_item(self) -> None:
        """Test case for get_portal_item

        Returns a record of the Portal  # noqa: E501
        """
        pass

    def test_link_portal(self) -> None:
        """Test case for link_portal

        Link Portal to Entities  # noqa: E501
        """
        pass

    def test_mass_delete_portal(self) -> None:
        """Test case for mass_delete_portal

        Mass delete of Portal data  # noqa: E501
        """
        pass

    def test_mass_update_portal(self) -> None:
        """Test case for mass_update_portal

        Mass update of Portal data  # noqa: E501
        """
        pass

    def test_remove_relation_for_portal(self) -> None:
        """Test case for remove_relation_for_portal

        Remove relation for Portal  # noqa: E501
        """
        pass

    def test_unfollow_portal(self) -> None:
        """Test case for unfollow_portal

        Unfollow the Portal stream  # noqa: E501
        """
        pass

    def test_unlink_portal(self) -> None:
        """Test case for unlink_portal

        Unlink Portal from Entities  # noqa: E501
        """
        pass

    def test_update_portal_item(self) -> None:
        """Test case for update_portal_item

        Update a record of the Portal  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
