# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_atrocore.api.export_job_api import ExportJobApi  # noqa: E501


class TestExportJobApi(unittest.TestCase):
    """ExportJobApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ExportJobApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_relation_for_export_job(self) -> None:
        """Test case for add_relation_for_export_job

        Add relation for ExportJob  # noqa: E501
        """
        pass

    def test_create_export_job_item(self) -> None:
        """Test case for create_export_job_item

        Create a record of the ExportJob  # noqa: E501
        """
        pass

    def test_delete_export_job_item(self) -> None:
        """Test case for delete_export_job_item

        Delete a record of the ExportJob  # noqa: E501
        """
        pass

    def test_follow_export_job(self) -> None:
        """Test case for follow_export_job

        Follow the ExportJob stream  # noqa: E501
        """
        pass

    def test_get_export_job_item(self) -> None:
        """Test case for get_export_job_item

        Returns a record of the ExportJob  # noqa: E501
        """
        pass

    def test_get_linked_items_for_export_job_item(self) -> None:
        """Test case for get_linked_items_for_export_job_item

        Returns linked entities for the ExportJob  # noqa: E501
        """
        pass

    def test_get_list_of_export_job_items(self) -> None:
        """Test case for get_list_of_export_job_items

        Returns a collection of ExportJob records  # noqa: E501
        """
        pass

    def test_link_export_job(self) -> None:
        """Test case for link_export_job

        Link ExportJob to Entities  # noqa: E501
        """
        pass

    def test_mass_delete_export_job(self) -> None:
        """Test case for mass_delete_export_job

        Mass delete of ExportJob data  # noqa: E501
        """
        pass

    def test_mass_update_export_job(self) -> None:
        """Test case for mass_update_export_job

        Mass update of ExportJob data  # noqa: E501
        """
        pass

    def test_remove_relation_for_export_job(self) -> None:
        """Test case for remove_relation_for_export_job

        Remove relation for ExportJob  # noqa: E501
        """
        pass

    def test_unfollow_export_job(self) -> None:
        """Test case for unfollow_export_job

        Unfollow the ExportJob stream  # noqa: E501
        """
        pass

    def test_unlink_export_job(self) -> None:
        """Test case for unlink_export_job

        Unlink ExportJob from Entities  # noqa: E501
        """
        pass

    def test_update_export_job_item(self) -> None:
        """Test case for update_export_job_item

        Update a record of the ExportJob  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
