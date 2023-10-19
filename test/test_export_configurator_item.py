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

from clientapi_atrocore.models.export_configurator_item import ExportConfiguratorItem  # noqa: E501

class TestExportConfiguratorItem(unittest.TestCase):
    """ExportConfiguratorItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExportConfiguratorItem:
        """Test ExportConfiguratorItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExportConfiguratorItem`
        """
        model = ExportConfiguratorItem()  # noqa: E501
        if include_optional:
            return ExportConfiguratorItem(
                id = '',
                deleted = True,
                attribute_value = '',
                zip = True,
                file_name_template = '',
                name = '',
                column = '',
                sort_order = 56,
                column_type = '',
                export_into_separate_columns = True,
                export_by = [
                    ''
                    ],
                filter_field = '',
                filter_field_value = [
                    ''
                    ],
                type = '',
                value_modifier = [
                    ''
                    ],
                attribute_name_value = '',
                is_attribute_multi_lang = True,
                language = '',
                entity = '',
                remove = '',
                scope = '',
                created_at = '',
                export_feed_id = '',
                export_feed_name = '',
                mask = '',
                editable = True,
                offset_relation = 56,
                limit_relation = 56,
                sort_field_relation = '',
                sort_order_relation = '',
                fixed_value = '',
                attribute_id = '',
                attribute_name = '',
                channel_id = '',
                channel_name = ''
            )
        else:
            return ExportConfiguratorItem(
                column_type = '',
        )
        """

    def testExportConfiguratorItem(self):
        """Test ExportConfiguratorItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()