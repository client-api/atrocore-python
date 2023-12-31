# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_atrocore.api.brand_api import BrandApi  # noqa: E501


class TestBrandApi(unittest.TestCase):
    """BrandApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BrandApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_relation_for_brand(self) -> None:
        """Test case for add_relation_for_brand

        Add relation for Brand  # noqa: E501
        """
        pass

    def test_create_brand_item(self) -> None:
        """Test case for create_brand_item

        Create a record of the Brand  # noqa: E501
        """
        pass

    def test_delete_brand_item(self) -> None:
        """Test case for delete_brand_item

        Delete a record of the Brand  # noqa: E501
        """
        pass

    def test_follow_brand(self) -> None:
        """Test case for follow_brand

        Follow the Brand stream  # noqa: E501
        """
        pass

    def test_get_brand_item(self) -> None:
        """Test case for get_brand_item

        Returns a record of the Brand  # noqa: E501
        """
        pass

    def test_get_linked_items_for_brand_item(self) -> None:
        """Test case for get_linked_items_for_brand_item

        Returns linked entities for the Brand  # noqa: E501
        """
        pass

    def test_get_list_of_brand_items(self) -> None:
        """Test case for get_list_of_brand_items

        Returns a collection of Brand records  # noqa: E501
        """
        pass

    def test_link_brand(self) -> None:
        """Test case for link_brand

        Link Brand to Entities  # noqa: E501
        """
        pass

    def test_mass_delete_brand(self) -> None:
        """Test case for mass_delete_brand

        Mass delete of Brand data  # noqa: E501
        """
        pass

    def test_mass_update_brand(self) -> None:
        """Test case for mass_update_brand

        Mass update of Brand data  # noqa: E501
        """
        pass

    def test_remove_relation_for_brand(self) -> None:
        """Test case for remove_relation_for_brand

        Remove relation for Brand  # noqa: E501
        """
        pass

    def test_unfollow_brand(self) -> None:
        """Test case for unfollow_brand

        Unfollow the Brand stream  # noqa: E501
        """
        pass

    def test_unlink_brand(self) -> None:
        """Test case for unlink_brand

        Unlink Brand from Entities  # noqa: E501
        """
        pass

    def test_update_brand_item(self) -> None:
        """Test case for update_brand_item

        Update a record of the Brand  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
