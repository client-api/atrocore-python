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

from clientapi_atrocore.models.attribute import Attribute  # noqa: E501

class TestAttribute(unittest.TestCase):
    """Attribute unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Attribute:
        """Test Attribute
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Attribute`
        """
        model = Attribute()  # noqa: E501
        if include_optional:
            return Attribute(
                id = '',
                deleted = True,
                name = '',
                name_de_de = '',
                created_at = '',
                modified_at = '',
                created_by_id = '',
                created_by_name = '',
                modified_by_id = '',
                modified_by_name = '',
                owner_user_id = '',
                owner_user_name = '',
                assigned_user_id = '',
                assigned_user_name = '',
                teams_ids = [
                    ''
                    ],
                teams_names = None,
                attribute_group_id = '',
                attribute_group_name = '',
                attribute_tab_id = '',
                attribute_tab_name = '',
                extensible_enum_id = '',
                extensible_enum_name = '',
                code = '',
                type = '',
                asset_type = '',
                is_multilang = True,
                pattern = '',
                unique = True,
                prohibited_empty_value = True,
                virtual_product_field = True,
                measure_id = '',
                measure_name = '',
                default_unit = '',
                default_scope = '',
                default_channel_id = '',
                default_channel_name = '',
                is_required = True,
                sort_order_in_attribute_group = 56,
                sort_order = 56,
                sort_order_in_product = 56,
                tooltip = '',
                tooltip_de_de = '',
                description = '',
                description_de_de = '',
                amount_of_digits_after_comma = 56,
                use_disabled_textarea_in_view_mode = True
            )
        else:
            return Attribute(
                name = '',
                name_de_de = '',
                type = '',
        )
        """

    def testAttribute(self):
        """Test Attribute"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
