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

from clientapi_atrocore.models.extensible_enum_option import ExtensibleEnumOption  # noqa: E501

class TestExtensibleEnumOption(unittest.TestCase):
    """ExtensibleEnumOption unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExtensibleEnumOption:
        """Test ExtensibleEnumOption
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtensibleEnumOption`
        """
        model = ExtensibleEnumOption()  # noqa: E501
        if include_optional:
            return ExtensibleEnumOption(
                id = '',
                deleted = True,
                name = '',
                name_de_de = '',
                code = '',
                extensible_enum_id = '',
                extensible_enum_name = '',
                color = '',
                sort_order = 56,
                created_at = '',
                modified_at = '',
                created_by_id = '',
                created_by_name = '',
                modified_by_id = '',
                modified_by_name = ''
            )
        else:
            return ExtensibleEnumOption(
        )
        """

    def testExtensibleEnumOption(self):
        """Test ExtensibleEnumOption"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
