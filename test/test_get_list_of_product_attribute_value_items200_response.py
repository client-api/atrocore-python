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

from clientapi_atrocore.models.get_list_of_product_attribute_value_items200_response import GetListOfProductAttributeValueItems200Response  # noqa: E501

class TestGetListOfProductAttributeValueItems200Response(unittest.TestCase):
    """GetListOfProductAttributeValueItems200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetListOfProductAttributeValueItems200Response:
        """Test GetListOfProductAttributeValueItems200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetListOfProductAttributeValueItems200Response`
        """
        model = GetListOfProductAttributeValueItems200Response()  # noqa: E501
        if include_optional:
            return GetListOfProductAttributeValueItems200Response(
                total = 56,
                list = [
                    clientapi_atrocore.models.product_attribute_value.ProductAttributeValue(
                        id = '', 
                        deleted = True, 
                        product_id = '', 
                        product_name = '', 
                        attribute_id = '', 
                        attribute_name = '', 
                        language = '', 
                        scope = '', 
                        channel_id = '', 
                        channel_name = '', 
                        is_variant_specific_attribute = True, 
                        count_bytes_instead_of_characters = True, 
                        amount_of_digits_after_comma = 56, 
                        value = '', 
                        attribute_type = '', 
                        attribute_asset_type = '', 
                        attribute_tooltip = '', 
                        created_at = '', 
                        modified_at = '', 
                        created_by_id = '', 
                        created_by_name = '', 
                        modified_by_id = '', 
                        modified_by_name = '', 
                        is_inherit_assigned_user = True, 
                        is_inherit_owner_user = True, 
                        is_inherit_teams = True, 
                        owner_user_id = '', 
                        owner_user_name = '', 
                        assigned_user_id = '', 
                        assigned_user_name = '', 
                        teams_ids = [
                            ''
                            ], 
                        teams_names = clientapi_atrocore.models.teams_names.teamsNames(), )
                    ]
            )
        else:
            return GetListOfProductAttributeValueItems200Response(
        )
        """

    def testGetListOfProductAttributeValueItems200Response(self):
        """Test GetListOfProductAttributeValueItems200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
