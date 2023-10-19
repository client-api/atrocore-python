# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from clientapi_atrocore.api.job_api import JobApi  # noqa: E501


class TestJobApi(unittest.TestCase):
    """JobApi unit test stubs"""

    def setUp(self) -> None:
        self.api = JobApi()  # noqa: E501

    def tearDown(self) -> None:
        pass

    def test_add_relation_for_job(self) -> None:
        """Test case for add_relation_for_job

        Add relation for Job  # noqa: E501
        """
        pass

    def test_create_job_item(self) -> None:
        """Test case for create_job_item

        Create a record of the Job  # noqa: E501
        """
        pass

    def test_delete_job_item(self) -> None:
        """Test case for delete_job_item

        Delete a record of the Job  # noqa: E501
        """
        pass

    def test_follow_job(self) -> None:
        """Test case for follow_job

        Follow the Job stream  # noqa: E501
        """
        pass

    def test_get_job_item(self) -> None:
        """Test case for get_job_item

        Returns a record of the Job  # noqa: E501
        """
        pass

    def test_get_linked_items_for_job_item(self) -> None:
        """Test case for get_linked_items_for_job_item

        Returns linked entities for the Job  # noqa: E501
        """
        pass

    def test_get_list_of_job_items(self) -> None:
        """Test case for get_list_of_job_items

        Returns a collection of Job records  # noqa: E501
        """
        pass

    def test_link_job(self) -> None:
        """Test case for link_job

        Link Job to Entities  # noqa: E501
        """
        pass

    def test_mass_delete_job(self) -> None:
        """Test case for mass_delete_job

        Mass delete of Job data  # noqa: E501
        """
        pass

    def test_mass_update_job(self) -> None:
        """Test case for mass_update_job

        Mass update of Job data  # noqa: E501
        """
        pass

    def test_remove_relation_for_job(self) -> None:
        """Test case for remove_relation_for_job

        Remove relation for Job  # noqa: E501
        """
        pass

    def test_unfollow_job(self) -> None:
        """Test case for unfollow_job

        Unfollow the Job stream  # noqa: E501
        """
        pass

    def test_unlink_job(self) -> None:
        """Test case for unlink_job

        Unlink Job from Entities  # noqa: E501
        """
        pass

    def test_update_job_item(self) -> None:
        """Test case for update_job_item

        Update a record of the Job  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()