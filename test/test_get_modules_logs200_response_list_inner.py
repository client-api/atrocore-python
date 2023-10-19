# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from clientapi_atrocore.models.get_modules_logs200_response_list_inner import GetModulesLogs200ResponseListInner  # noqa: E501

class TestGetModulesLogs200ResponseListInner(unittest.TestCase):
    """GetModulesLogs200ResponseListInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetModulesLogs200ResponseListInner:
        """Test GetModulesLogs200ResponseListInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetModulesLogs200ResponseListInner`
        """
        model = GetModulesLogs200ResponseListInner()  # noqa: E501
        if include_optional:
            return GetModulesLogs200ResponseListInner(
                id = '',
                deleted = True,
                post = '',
                data = None,
                type = '',
                target_type = '',
                parent_id = '',
                parent_name = '',
                related_id = '',
                related_name = '',
                attachments = '',
                number = 56,
                is_global = True,
                created_by_gender = '',
                notified_user_id_list = None,
                is_internal = True,
                created_at = '',
                modified_at = '',
                created_by_id = '',
                created_by_name = '',
                modified_by_id = '',
                modified_by_name = '',
                attribute_id = '',
                pav_id = ''
            )
        else:
            return GetModulesLogs200ResponseListInner(
        )
        """

    def testGetModulesLogs200ResponseListInner(self):
        """Test GetModulesLogs200ResponseListInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
