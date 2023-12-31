# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_atrocore.api.variable_api import VariableApi  # noqa: E501


class TestVariableApi(unittest.TestCase):
    """VariableApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VariableApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_relation_for_variable(self) -> None:
        """Test case for add_relation_for_variable

        Add relation for Variable  # noqa: E501
        """
        pass

    def test_create_variable_item(self) -> None:
        """Test case for create_variable_item

        Create a record of the Variable  # noqa: E501
        """
        pass

    def test_delete_variable_item(self) -> None:
        """Test case for delete_variable_item

        Delete a record of the Variable  # noqa: E501
        """
        pass

    def test_follow_variable(self) -> None:
        """Test case for follow_variable

        Follow the Variable stream  # noqa: E501
        """
        pass

    def test_get_linked_items_for_variable_item(self) -> None:
        """Test case for get_linked_items_for_variable_item

        Returns linked entities for the Variable  # noqa: E501
        """
        pass

    def test_get_list_of_variable_items(self) -> None:
        """Test case for get_list_of_variable_items

        Returns a collection of Variable records  # noqa: E501
        """
        pass

    def test_get_variable_item(self) -> None:
        """Test case for get_variable_item

        Returns a record of the Variable  # noqa: E501
        """
        pass

    def test_link_variable(self) -> None:
        """Test case for link_variable

        Link Variable to Entities  # noqa: E501
        """
        pass

    def test_mass_delete_variable(self) -> None:
        """Test case for mass_delete_variable

        Mass delete of Variable data  # noqa: E501
        """
        pass

    def test_mass_update_variable(self) -> None:
        """Test case for mass_update_variable

        Mass update of Variable data  # noqa: E501
        """
        pass

    def test_remove_relation_for_variable(self) -> None:
        """Test case for remove_relation_for_variable

        Remove relation for Variable  # noqa: E501
        """
        pass

    def test_unfollow_variable(self) -> None:
        """Test case for unfollow_variable

        Unfollow the Variable stream  # noqa: E501
        """
        pass

    def test_unlink_variable(self) -> None:
        """Test case for unlink_variable

        Unlink Variable from Entities  # noqa: E501
        """
        pass

    def test_update_variable_item(self) -> None:
        """Test case for update_variable_item

        Update a record of the Variable  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
