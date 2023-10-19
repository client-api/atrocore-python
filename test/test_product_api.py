# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_atrocore.api.product_api import ProductApi  # noqa: E501


class TestProductApi(unittest.TestCase):
    """ProductApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProductApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_relation_for_product(self) -> None:
        """Test case for add_relation_for_product

        Add relation for Product  # noqa: E501
        """
        pass

    def test_create_product_item(self) -> None:
        """Test case for create_product_item

        Create a record of the Product  # noqa: E501
        """
        pass

    def test_delete_product_item(self) -> None:
        """Test case for delete_product_item

        Delete a record of the Product  # noqa: E501
        """
        pass

    def test_follow_product(self) -> None:
        """Test case for follow_product

        Follow the Product stream  # noqa: E501
        """
        pass

    def test_get_linked_items_for_product_item(self) -> None:
        """Test case for get_linked_items_for_product_item

        Returns linked entities for the Product  # noqa: E501
        """
        pass

    def test_get_list_of_product_items(self) -> None:
        """Test case for get_list_of_product_items

        Returns a collection of Product records  # noqa: E501
        """
        pass

    def test_get_product_item(self) -> None:
        """Test case for get_product_item

        Returns a record of the Product  # noqa: E501
        """
        pass

    def test_link_product(self) -> None:
        """Test case for link_product

        Link Product to Entities  # noqa: E501
        """
        pass

    def test_mass_delete_product(self) -> None:
        """Test case for mass_delete_product

        Mass delete of Product data  # noqa: E501
        """
        pass

    def test_mass_update_product(self) -> None:
        """Test case for mass_update_product

        Mass update of Product data  # noqa: E501
        """
        pass

    def test_remove_relation_for_product(self) -> None:
        """Test case for remove_relation_for_product

        Remove relation for Product  # noqa: E501
        """
        pass

    def test_unfollow_product(self) -> None:
        """Test case for unfollow_product

        Unfollow the Product stream  # noqa: E501
        """
        pass

    def test_unlink_product(self) -> None:
        """Test case for unlink_product

        Unlink Product from Entities  # noqa: E501
        """
        pass

    def test_update_product_item(self) -> None:
        """Test case for update_product_item

        Update a record of the Product  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()