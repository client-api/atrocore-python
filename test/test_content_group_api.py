# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_atrocore.api.content_group_api import ContentGroupApi  # noqa: E501


class TestContentGroupApi(unittest.TestCase):
    """ContentGroupApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ContentGroupApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_relation_for_content_group(self) -> None:
        """Test case for add_relation_for_content_group

        Add relation for ContentGroup  # noqa: E501
        """
        pass

    def test_create_content_group_item(self) -> None:
        """Test case for create_content_group_item

        Create a record of the ContentGroup  # noqa: E501
        """
        pass

    def test_delete_content_group_item(self) -> None:
        """Test case for delete_content_group_item

        Delete a record of the ContentGroup  # noqa: E501
        """
        pass

    def test_follow_content_group(self) -> None:
        """Test case for follow_content_group

        Follow the ContentGroup stream  # noqa: E501
        """
        pass

    def test_get_content_group_item(self) -> None:
        """Test case for get_content_group_item

        Returns a record of the ContentGroup  # noqa: E501
        """
        pass

    def test_get_linked_items_for_content_group_item(self) -> None:
        """Test case for get_linked_items_for_content_group_item

        Returns linked entities for the ContentGroup  # noqa: E501
        """
        pass

    def test_get_list_of_content_group_items(self) -> None:
        """Test case for get_list_of_content_group_items

        Returns a collection of ContentGroup records  # noqa: E501
        """
        pass

    def test_link_content_group(self) -> None:
        """Test case for link_content_group

        Link ContentGroup to Entities  # noqa: E501
        """
        pass

    def test_mass_delete_content_group(self) -> None:
        """Test case for mass_delete_content_group

        Mass delete of ContentGroup data  # noqa: E501
        """
        pass

    def test_mass_update_content_group(self) -> None:
        """Test case for mass_update_content_group

        Mass update of ContentGroup data  # noqa: E501
        """
        pass

    def test_remove_relation_for_content_group(self) -> None:
        """Test case for remove_relation_for_content_group

        Remove relation for ContentGroup  # noqa: E501
        """
        pass

    def test_unfollow_content_group(self) -> None:
        """Test case for unfollow_content_group

        Unfollow the ContentGroup stream  # noqa: E501
        """
        pass

    def test_unlink_content_group(self) -> None:
        """Test case for unlink_content_group

        Unlink ContentGroup from Entities  # noqa: E501
        """
        pass

    def test_update_content_group_item(self) -> None:
        """Test case for update_content_group_item

        Update a record of the ContentGroup  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
