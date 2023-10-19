# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_atrocore.api.attribute_group_api import AttributeGroupApi  # noqa: E501


class TestAttributeGroupApi(unittest.TestCase):
    """AttributeGroupApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AttributeGroupApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_relation_for_attribute_group(self) -> None:
        """Test case for add_relation_for_attribute_group

        Add relation for AttributeGroup  # noqa: E501
        """
        pass

    def test_create_attribute_group_item(self) -> None:
        """Test case for create_attribute_group_item

        Create a record of the AttributeGroup  # noqa: E501
        """
        pass

    def test_delete_attribute_group_item(self) -> None:
        """Test case for delete_attribute_group_item

        Delete a record of the AttributeGroup  # noqa: E501
        """
        pass

    def test_follow_attribute_group(self) -> None:
        """Test case for follow_attribute_group

        Follow the AttributeGroup stream  # noqa: E501
        """
        pass

    def test_get_attribute_group_item(self) -> None:
        """Test case for get_attribute_group_item

        Returns a record of the AttributeGroup  # noqa: E501
        """
        pass

    def test_get_linked_items_for_attribute_group_item(self) -> None:
        """Test case for get_linked_items_for_attribute_group_item

        Returns linked entities for the AttributeGroup  # noqa: E501
        """
        pass

    def test_get_list_of_attribute_group_items(self) -> None:
        """Test case for get_list_of_attribute_group_items

        Returns a collection of AttributeGroup records  # noqa: E501
        """
        pass

    def test_link_attribute_group(self) -> None:
        """Test case for link_attribute_group

        Link AttributeGroup to Entities  # noqa: E501
        """
        pass

    def test_mass_delete_attribute_group(self) -> None:
        """Test case for mass_delete_attribute_group

        Mass delete of AttributeGroup data  # noqa: E501
        """
        pass

    def test_mass_update_attribute_group(self) -> None:
        """Test case for mass_update_attribute_group

        Mass update of AttributeGroup data  # noqa: E501
        """
        pass

    def test_remove_relation_for_attribute_group(self) -> None:
        """Test case for remove_relation_for_attribute_group

        Remove relation for AttributeGroup  # noqa: E501
        """
        pass

    def test_unfollow_attribute_group(self) -> None:
        """Test case for unfollow_attribute_group

        Unfollow the AttributeGroup stream  # noqa: E501
        """
        pass

    def test_unlink_attribute_group(self) -> None:
        """Test case for unlink_attribute_group

        Unlink AttributeGroup from Entities  # noqa: E501
        """
        pass

    def test_update_attribute_group_item(self) -> None:
        """Test case for update_attribute_group_item

        Update a record of the AttributeGroup  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
