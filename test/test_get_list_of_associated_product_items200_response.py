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

from clientapi_atrocore.models.get_list_of_associated_product_items200_response import GetListOfAssociatedProductItems200Response  # noqa: E501

class TestGetListOfAssociatedProductItems200Response(unittest.TestCase):
    """GetListOfAssociatedProductItems200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetListOfAssociatedProductItems200Response:
        """Test GetListOfAssociatedProductItems200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetListOfAssociatedProductItems200Response`
        """
        model = GetListOfAssociatedProductItems200Response()  # noqa: E501
        if include_optional:
            return GetListOfAssociatedProductItems200Response(
                total = 56,
                list = [
                    clientapi_atrocore.models.associated_product.AssociatedProduct(
                        id = '', 
                        deleted = True, 
                        association_id = '', 
                        association_name = '', 
                        main_product_id = '', 
                        main_product_name = '', 
                        related_product_id = '', 
                        related_product_name = '', 
                        backward_association_id = '', 
                        backward_association_name = '', 
                        created_at = '', 
                        modified_at = '', 
                        created_by_id = '', 
                        created_by_name = '', 
                        modified_by_id = '', 
                        modified_by_name = '', 
                        sorting = 56, 
                        main_product_image_id = '', 
                        main_product_image_name = '', 
                        related_product_image_id = '', 
                        related_product_image_name = '', )
                    ]
            )
        else:
            return GetListOfAssociatedProductItems200Response(
        )
        """

    def testGetListOfAssociatedProductItems200Response(self):
        """Test GetListOfAssociatedProductItems200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
