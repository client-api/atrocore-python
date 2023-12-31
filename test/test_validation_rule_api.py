# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_atrocore.api.validation_rule_api import ValidationRuleApi  # noqa: E501


class TestValidationRuleApi(unittest.TestCase):
    """ValidationRuleApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ValidationRuleApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_relation_for_validation_rule(self) -> None:
        """Test case for add_relation_for_validation_rule

        Add relation for ValidationRule  # noqa: E501
        """
        pass

    def test_create_validation_rule_item(self) -> None:
        """Test case for create_validation_rule_item

        Create a record of the ValidationRule  # noqa: E501
        """
        pass

    def test_delete_validation_rule_item(self) -> None:
        """Test case for delete_validation_rule_item

        Delete a record of the ValidationRule  # noqa: E501
        """
        pass

    def test_follow_validation_rule(self) -> None:
        """Test case for follow_validation_rule

        Follow the ValidationRule stream  # noqa: E501
        """
        pass

    def test_get_linked_items_for_validation_rule_item(self) -> None:
        """Test case for get_linked_items_for_validation_rule_item

        Returns linked entities for the ValidationRule  # noqa: E501
        """
        pass

    def test_get_list_of_validation_rule_items(self) -> None:
        """Test case for get_list_of_validation_rule_items

        Returns a collection of ValidationRule records  # noqa: E501
        """
        pass

    def test_get_validation_rule_item(self) -> None:
        """Test case for get_validation_rule_item

        Returns a record of the ValidationRule  # noqa: E501
        """
        pass

    def test_link_validation_rule(self) -> None:
        """Test case for link_validation_rule

        Link ValidationRule to Entities  # noqa: E501
        """
        pass

    def test_mass_delete_validation_rule(self) -> None:
        """Test case for mass_delete_validation_rule

        Mass delete of ValidationRule data  # noqa: E501
        """
        pass

    def test_mass_update_validation_rule(self) -> None:
        """Test case for mass_update_validation_rule

        Mass update of ValidationRule data  # noqa: E501
        """
        pass

    def test_remove_relation_for_validation_rule(self) -> None:
        """Test case for remove_relation_for_validation_rule

        Remove relation for ValidationRule  # noqa: E501
        """
        pass

    def test_unfollow_validation_rule(self) -> None:
        """Test case for unfollow_validation_rule

        Unfollow the ValidationRule stream  # noqa: E501
        """
        pass

    def test_unlink_validation_rule(self) -> None:
        """Test case for unlink_validation_rule

        Unlink ValidationRule from Entities  # noqa: E501
        """
        pass

    def test_update_validation_rule_item(self) -> None:
        """Test case for update_validation_rule_item

        Update a record of the ValidationRule  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
