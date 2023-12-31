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

from clientapi_atrocore.models.get_list_of_product_items200_response import GetListOfProductItems200Response  # noqa: E501

class TestGetListOfProductItems200Response(unittest.TestCase):
    """GetListOfProductItems200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetListOfProductItems200Response:
        """Test GetListOfProductItems200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetListOfProductItems200Response`
        """
        model = GetListOfProductItems200Response()  # noqa: E501
        if include_optional:
            return GetListOfProductItems200Response(
                total = 56,
                list = [
                    clientapi_atrocore.models.product.Product(
                        id = '', 
                        deleted = True, 
                        name = '', 
                        name_de_de = '', 
                        classifications_ids = [
                            ''
                            ], 
                        classifications_names = clientapi_atrocore.models.classifications_names.classificationsNames(), 
                        brand_id = '', 
                        brand_name = '', 
                        sku = '', 
                        is_active = True, 
                        amount = '', 
                        price = '', 
                        price_currency = '', 
                        product_status = '', 
                        tax_id = '', 
                        tax_name = '', 
                        ean = '', 
                        mpn = '', 
                        packaging_id = '', 
                        packaging_name = '', 
                        uvp = '', 
                        tag = [
                            ''
                            ], 
                        long_description = '', 
                        long_description_de_de = '', 
                        product_serie_id = '', 
                        product_serie_name = '', 
                        parents_ids = [
                            ''
                            ], 
                        parents_names = clientapi_atrocore.models.parents_names.parentsNames(), 
                        sort_order = 56, 
                        data = clientapi_atrocore.models.data.data(), 
                        catalog_id = '', 
                        catalog_name = '', 
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
                        teams_names = clientapi_atrocore.models.teams_names.teamsNames(), 
                        sorting = 56, 
                        contents_ids = [
                            ''
                            ], 
                        contents_names = clientapi_atrocore.models.contents_names.contentsNames(), 
                        is_inherit_assigned_user = True, 
                        is_inherit_owner_user = True, 
                        is_inherit_teams = True, 
                        task_status = [
                            ''
                            ], 
                        attachments = '', )
                    ]
            )
        else:
            return GetListOfProductItems200Response(
        )
        """

    def testGetListOfProductItems200Response(self):
        """Test GetListOfProductItems200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
