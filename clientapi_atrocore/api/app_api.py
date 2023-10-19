# coding: utf-8

"""
    AtroCore REST API documentation

    This is a REST API documentation for AtroCore data platform and its modules (AtroPIM, AtroDAM and others), which is based on [OpenAPI (Swagger) Specification](https://swagger.io/specification/). You can generate your client [here](https://openapi-generator.tech/docs/generators).<br><br><h3>Video tutorials:</h3><ul><li>[How to authorize?](https://youtu.be/GWfNRvCswXg)</li><li>[How to select specific fields?](https://youtu.be/i7o0aENuyuY)</li><li>[How to filter data records?](https://youtu.be/irgWkN4wlkM)</li></ul>

    The version of the OpenAPI document: 1.6.55
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError

from typing_extensions import Annotated
from pydantic import Field, StrictBool, StrictInt

from typing import Optional

from clientapi_atrocore.models.get_authorized_user_data200_response import GetAuthorizedUserData200Response

from clientapi_atrocore.api_client import ApiClient
from clientapi_atrocore.api_response import ApiResponse
from clientapi_atrocore.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AppApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_authorized_user_data(self, authorization_token_only : StrictBool, authorization_token_lifetime : Annotated[Optional[StrictInt], Field(description="Lifetime should be set in hours. 0 means no expiration. If this parameter is not passed, the globally configured parameter is used.")] = None, authorization_token_idletime : Annotated[Optional[StrictInt], Field(description="Idletime should be set in hours. 0 means no expiration. If this parameter is not passed, the globally configured parameter is used.")] = None, **kwargs) -> GetAuthorizedUserData200Response:  # noqa: E501
        """Generate authorization token and return authorized user data.  # noqa: E501

        Generate authorization token and return authorized user data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_authorized_user_data(authorization_token_only, authorization_token_lifetime, authorization_token_idletime, async_req=True)
        >>> result = thread.get()

        :param authorization_token_only: (required)
        :type authorization_token_only: bool
        :param authorization_token_lifetime: Lifetime should be set in hours. 0 means no expiration. If this parameter is not passed, the globally configured parameter is used.
        :type authorization_token_lifetime: int
        :param authorization_token_idletime: Idletime should be set in hours. 0 means no expiration. If this parameter is not passed, the globally configured parameter is used.
        :type authorization_token_idletime: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetAuthorizedUserData200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_authorized_user_data_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        return self.get_authorized_user_data_with_http_info(authorization_token_only, authorization_token_lifetime, authorization_token_idletime, **kwargs)  # noqa: E501

    @validate_arguments
    def get_authorized_user_data_with_http_info(self, authorization_token_only : StrictBool, authorization_token_lifetime : Annotated[Optional[StrictInt], Field(description="Lifetime should be set in hours. 0 means no expiration. If this parameter is not passed, the globally configured parameter is used.")] = None, authorization_token_idletime : Annotated[Optional[StrictInt], Field(description="Idletime should be set in hours. 0 means no expiration. If this parameter is not passed, the globally configured parameter is used.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Generate authorization token and return authorized user data.  # noqa: E501

        Generate authorization token and return authorized user data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_authorized_user_data_with_http_info(authorization_token_only, authorization_token_lifetime, authorization_token_idletime, async_req=True)
        >>> result = thread.get()

        :param authorization_token_only: (required)
        :type authorization_token_only: bool
        :param authorization_token_lifetime: Lifetime should be set in hours. 0 means no expiration. If this parameter is not passed, the globally configured parameter is used.
        :type authorization_token_lifetime: int
        :param authorization_token_idletime: Idletime should be set in hours. 0 means no expiration. If this parameter is not passed, the globally configured parameter is used.
        :type authorization_token_idletime: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetAuthorizedUserData200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'authorization_token_only',
            'authorization_token_lifetime',
            'authorization_token_idletime'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_authorized_user_data" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['authorization_token_only']:
            _header_params['Authorization-Token-Only'] = _params['authorization_token_only']

        if _params['authorization_token_lifetime']:
            _header_params['Authorization-Token-Lifetime'] = _params['authorization_token_lifetime']

        if _params['authorization_token_idletime']:
            _header_params['Authorization-Token-Idletime'] = _params['authorization_token_idletime']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['basicAuth']  # noqa: E501

        _response_types_map = {
            '200': "GetAuthorizedUserData200Response",
            '304': None,
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/App/user', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
