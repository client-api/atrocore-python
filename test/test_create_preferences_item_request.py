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

from clientapi_atrocore.models.create_preferences_item_request import CreatePreferencesItemRequest  # noqa: E501

class TestCreatePreferencesItemRequest(unittest.TestCase):
    """CreatePreferencesItemRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreatePreferencesItemRequest:
        """Test CreatePreferencesItemRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreatePreferencesItemRequest`
        """
        model = CreatePreferencesItemRequest()  # noqa: E501
        if include_optional:
            return CreatePreferencesItemRequest(
                locale = '',
                locale_id = '',
                language = '',
                decimal_mark = '',
                time_format = '',
                thousand_separator = '',
                week_start = 56,
                date_format = '',
                time_zone = '',
                default_currency = '',
                dashboard_layout = None,
                dashlets_options = None,
                shared_calendar_user_list = None,
                calendar_view_data_list = None,
                preset_filters = None,
                receive_assignment_email_notifications = True,
                receive_mention_email_notifications = True,
                receive_stream_email_notifications = True,
                assignment_notifications = True,
                auto_follow_entity_type_list = [
                    ''
                    ],
                theme = '',
                use_custom_tab_list = True,
                tab_list = [
                    ''
                    ],
                is_portal_user = True,
                follow_entity_on_stream_post = True,
                follow_created_entities = True,
                follow_created_entity_type_list = [
                    ''
                    ],
                scope_colors_disabled = True,
                tab_colors_disabled = True
            )
        else:
            return CreatePreferencesItemRequest(
        )
        """

    def testCreatePreferencesItemRequest(self):
        """Test CreatePreferencesItemRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
