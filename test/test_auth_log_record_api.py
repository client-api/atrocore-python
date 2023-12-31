# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_atrocore.api.auth_log_record_api import AuthLogRecordApi  # noqa: E501


class TestAuthLogRecordApi(unittest.TestCase):
    """AuthLogRecordApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AuthLogRecordApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_relation_for_auth_log_record(self) -> None:
        """Test case for add_relation_for_auth_log_record

        Add relation for AuthLogRecord  # noqa: E501
        """
        pass

    def test_create_auth_log_record_item(self) -> None:
        """Test case for create_auth_log_record_item

        Create a record of the AuthLogRecord  # noqa: E501
        """
        pass

    def test_delete_auth_log_record_item(self) -> None:
        """Test case for delete_auth_log_record_item

        Delete a record of the AuthLogRecord  # noqa: E501
        """
        pass

    def test_follow_auth_log_record(self) -> None:
        """Test case for follow_auth_log_record

        Follow the AuthLogRecord stream  # noqa: E501
        """
        pass

    def test_get_auth_log_record_item(self) -> None:
        """Test case for get_auth_log_record_item

        Returns a record of the AuthLogRecord  # noqa: E501
        """
        pass

    def test_get_linked_items_for_auth_log_record_item(self) -> None:
        """Test case for get_linked_items_for_auth_log_record_item

        Returns linked entities for the AuthLogRecord  # noqa: E501
        """
        pass

    def test_get_list_of_auth_log_record_items(self) -> None:
        """Test case for get_list_of_auth_log_record_items

        Returns a collection of AuthLogRecord records  # noqa: E501
        """
        pass

    def test_link_auth_log_record(self) -> None:
        """Test case for link_auth_log_record

        Link AuthLogRecord to Entities  # noqa: E501
        """
        pass

    def test_mass_delete_auth_log_record(self) -> None:
        """Test case for mass_delete_auth_log_record

        Mass delete of AuthLogRecord data  # noqa: E501
        """
        pass

    def test_mass_update_auth_log_record(self) -> None:
        """Test case for mass_update_auth_log_record

        Mass update of AuthLogRecord data  # noqa: E501
        """
        pass

    def test_remove_relation_for_auth_log_record(self) -> None:
        """Test case for remove_relation_for_auth_log_record

        Remove relation for AuthLogRecord  # noqa: E501
        """
        pass

    def test_unfollow_auth_log_record(self) -> None:
        """Test case for unfollow_auth_log_record

        Unfollow the AuthLogRecord stream  # noqa: E501
        """
        pass

    def test_unlink_auth_log_record(self) -> None:
        """Test case for unlink_auth_log_record

        Unlink AuthLogRecord from Entities  # noqa: E501
        """
        pass

    def test_update_auth_log_record_item(self) -> None:
        """Test case for update_auth_log_record_item

        Update a record of the AuthLogRecord  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
