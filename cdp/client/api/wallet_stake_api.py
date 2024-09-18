"""Coinbase Platform API

This is the OpenAPI 3.0 specification for the Coinbase Platform APIs, used in conjunction with the Coinbase Platform SDKs.

The version of the OpenAPI document: 0.0.1-alpha
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from typing import Annotated, Any

from pydantic import Field, StrictFloat, StrictInt, StrictStr, validate_call

from cdp.client.api_client import ApiClient, RequestSerialized
from cdp.client.api_response import ApiResponse
from cdp.client.models.broadcast_staking_operation_request import BroadcastStakingOperationRequest
from cdp.client.models.create_staking_operation_request import CreateStakingOperationRequest
from cdp.client.models.staking_operation import StakingOperation
from cdp.client.rest import RESTResponseType


class WalletStakeApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_call
    def broadcast_staking_operation(
        self,
        wallet_id: Annotated[
            StrictStr, Field(description="The ID of the wallet the address belongs to.")
        ],
        address_id: Annotated[
            StrictStr, Field(description="The ID of the address the staking operation belongs to.")
        ],
        staking_operation_id: Annotated[
            StrictStr, Field(description="The ID of the staking operation to broadcast.")
        ],
        broadcast_staking_operation_request: BroadcastStakingOperationRequest,
        _request_timeout: None
        | Annotated[StrictFloat, Field(gt=0)]
        | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> StakingOperation:
        """Broadcast a staking operation

        Broadcast a staking operation.

        :param wallet_id: The ID of the wallet the address belongs to. (required)
        :type wallet_id: str
        :param address_id: The ID of the address the staking operation belongs to. (required)
        :type address_id: str
        :param staking_operation_id: The ID of the staking operation to broadcast. (required)
        :type staking_operation_id: str
        :param broadcast_staking_operation_request: (required)
        :type broadcast_staking_operation_request: BroadcastStakingOperationRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        _param = self._broadcast_staking_operation_serialize(
            wallet_id=wallet_id,
            address_id=address_id,
            staking_operation_id=staking_operation_id,
            broadcast_staking_operation_request=broadcast_staking_operation_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            "200": "StakingOperation",
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def broadcast_staking_operation_with_http_info(
        self,
        wallet_id: Annotated[
            StrictStr, Field(description="The ID of the wallet the address belongs to.")
        ],
        address_id: Annotated[
            StrictStr, Field(description="The ID of the address the staking operation belongs to.")
        ],
        staking_operation_id: Annotated[
            StrictStr, Field(description="The ID of the staking operation to broadcast.")
        ],
        broadcast_staking_operation_request: BroadcastStakingOperationRequest,
        _request_timeout: None
        | Annotated[StrictFloat, Field(gt=0)]
        | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[StakingOperation]:
        """Broadcast a staking operation

        Broadcast a staking operation.

        :param wallet_id: The ID of the wallet the address belongs to. (required)
        :type wallet_id: str
        :param address_id: The ID of the address the staking operation belongs to. (required)
        :type address_id: str
        :param staking_operation_id: The ID of the staking operation to broadcast. (required)
        :type staking_operation_id: str
        :param broadcast_staking_operation_request: (required)
        :type broadcast_staking_operation_request: BroadcastStakingOperationRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        _param = self._broadcast_staking_operation_serialize(
            wallet_id=wallet_id,
            address_id=address_id,
            staking_operation_id=staking_operation_id,
            broadcast_staking_operation_request=broadcast_staking_operation_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            "200": "StakingOperation",
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def broadcast_staking_operation_without_preload_content(
        self,
        wallet_id: Annotated[
            StrictStr, Field(description="The ID of the wallet the address belongs to.")
        ],
        address_id: Annotated[
            StrictStr, Field(description="The ID of the address the staking operation belongs to.")
        ],
        staking_operation_id: Annotated[
            StrictStr, Field(description="The ID of the staking operation to broadcast.")
        ],
        broadcast_staking_operation_request: BroadcastStakingOperationRequest,
        _request_timeout: None
        | Annotated[StrictFloat, Field(gt=0)]
        | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Broadcast a staking operation

        Broadcast a staking operation.

        :param wallet_id: The ID of the wallet the address belongs to. (required)
        :type wallet_id: str
        :param address_id: The ID of the address the staking operation belongs to. (required)
        :type address_id: str
        :param staking_operation_id: The ID of the staking operation to broadcast. (required)
        :type staking_operation_id: str
        :param broadcast_staking_operation_request: (required)
        :type broadcast_staking_operation_request: BroadcastStakingOperationRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        _param = self._broadcast_staking_operation_serialize(
            wallet_id=wallet_id,
            address_id=address_id,
            staking_operation_id=staking_operation_id,
            broadcast_staking_operation_request=broadcast_staking_operation_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            "200": "StakingOperation",
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        return response_data.response

    def _broadcast_staking_operation_serialize(
        self,
        wallet_id,
        address_id,
        staking_operation_id,
        broadcast_staking_operation_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: dict[str, str] = {}

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[str, str | bytes] = {}
        _body_params: bytes | None = None

        # process the path parameters
        if wallet_id is not None:
            _path_params["wallet_id"] = wallet_id
        if address_id is not None:
            _path_params["address_id"] = address_id
        if staking_operation_id is not None:
            _path_params["staking_operation_id"] = staking_operation_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if broadcast_staking_operation_request is not None:
            _body_params = broadcast_staking_operation_request

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(["application/json"])
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: list[str] = []

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/v1/wallets/{wallet_id}/addresses/{address_id}/staking_operations/{staking_operation_id}/broadcast",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def create_staking_operation(
        self,
        wallet_id: Annotated[
            StrictStr, Field(description="The ID of the wallet the address belongs to.")
        ],
        address_id: Annotated[
            StrictStr,
            Field(description="The ID of the address to create the staking operation for."),
        ],
        create_staking_operation_request: CreateStakingOperationRequest,
        _request_timeout: None
        | Annotated[StrictFloat, Field(gt=0)]
        | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> StakingOperation:
        """Create a new staking operation for an address

        Create a new staking operation.

        :param wallet_id: The ID of the wallet the address belongs to. (required)
        :type wallet_id: str
        :param address_id: The ID of the address to create the staking operation for. (required)
        :type address_id: str
        :param create_staking_operation_request: (required)
        :type create_staking_operation_request: CreateStakingOperationRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        _param = self._create_staking_operation_serialize(
            wallet_id=wallet_id,
            address_id=address_id,
            create_staking_operation_request=create_staking_operation_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            "200": "StakingOperation",
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def create_staking_operation_with_http_info(
        self,
        wallet_id: Annotated[
            StrictStr, Field(description="The ID of the wallet the address belongs to.")
        ],
        address_id: Annotated[
            StrictStr,
            Field(description="The ID of the address to create the staking operation for."),
        ],
        create_staking_operation_request: CreateStakingOperationRequest,
        _request_timeout: None
        | Annotated[StrictFloat, Field(gt=0)]
        | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[StakingOperation]:
        """Create a new staking operation for an address

        Create a new staking operation.

        :param wallet_id: The ID of the wallet the address belongs to. (required)
        :type wallet_id: str
        :param address_id: The ID of the address to create the staking operation for. (required)
        :type address_id: str
        :param create_staking_operation_request: (required)
        :type create_staking_operation_request: CreateStakingOperationRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        _param = self._create_staking_operation_serialize(
            wallet_id=wallet_id,
            address_id=address_id,
            create_staking_operation_request=create_staking_operation_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            "200": "StakingOperation",
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def create_staking_operation_without_preload_content(
        self,
        wallet_id: Annotated[
            StrictStr, Field(description="The ID of the wallet the address belongs to.")
        ],
        address_id: Annotated[
            StrictStr,
            Field(description="The ID of the address to create the staking operation for."),
        ],
        create_staking_operation_request: CreateStakingOperationRequest,
        _request_timeout: None
        | Annotated[StrictFloat, Field(gt=0)]
        | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Create a new staking operation for an address

        Create a new staking operation.

        :param wallet_id: The ID of the wallet the address belongs to. (required)
        :type wallet_id: str
        :param address_id: The ID of the address to create the staking operation for. (required)
        :type address_id: str
        :param create_staking_operation_request: (required)
        :type create_staking_operation_request: CreateStakingOperationRequest
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        _param = self._create_staking_operation_serialize(
            wallet_id=wallet_id,
            address_id=address_id,
            create_staking_operation_request=create_staking_operation_request,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            "200": "StakingOperation",
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        return response_data.response

    def _create_staking_operation_serialize(
        self,
        wallet_id,
        address_id,
        create_staking_operation_request,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: dict[str, str] = {}

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[str, str | bytes] = {}
        _body_params: bytes | None = None

        # process the path parameters
        if wallet_id is not None:
            _path_params["wallet_id"] = wallet_id
        if address_id is not None:
            _path_params["address_id"] = address_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if create_staking_operation_request is not None:
            _body_params = create_staking_operation_request

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params["Content-Type"] = _content_type
        else:
            _default_content_type = self.api_client.select_header_content_type(["application/json"])
            if _default_content_type is not None:
                _header_params["Content-Type"] = _default_content_type

        # authentication setting
        _auth_settings: list[str] = []

        return self.api_client.param_serialize(
            method="POST",
            resource_path="/v1/wallets/{wallet_id}/addresses/{address_id}/staking_operations",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )

    @validate_call
    def get_staking_operation(
        self,
        wallet_id: Annotated[
            StrictStr, Field(description="The ID of the wallet the address belongs to")
        ],
        address_id: Annotated[
            StrictStr,
            Field(description="The ID of the address to fetch the staking operation for."),
        ],
        staking_operation_id: Annotated[
            StrictStr, Field(description="The ID of the staking operation.")
        ],
        _request_timeout: None
        | Annotated[StrictFloat, Field(gt=0)]
        | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> StakingOperation:
        """Get the latest state of a staking operation

        Get the latest state of a staking operation.

        :param wallet_id: The ID of the wallet the address belongs to (required)
        :type wallet_id: str
        :param address_id: The ID of the address to fetch the staking operation for. (required)
        :type address_id: str
        :param staking_operation_id: The ID of the staking operation. (required)
        :type staking_operation_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        _param = self._get_staking_operation_serialize(
            wallet_id=wallet_id,
            address_id=address_id,
            staking_operation_id=staking_operation_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            "200": "StakingOperation",
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data

    @validate_call
    def get_staking_operation_with_http_info(
        self,
        wallet_id: Annotated[
            StrictStr, Field(description="The ID of the wallet the address belongs to")
        ],
        address_id: Annotated[
            StrictStr,
            Field(description="The ID of the address to fetch the staking operation for."),
        ],
        staking_operation_id: Annotated[
            StrictStr, Field(description="The ID of the staking operation.")
        ],
        _request_timeout: None
        | Annotated[StrictFloat, Field(gt=0)]
        | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[StakingOperation]:
        """Get the latest state of a staking operation

        Get the latest state of a staking operation.

        :param wallet_id: The ID of the wallet the address belongs to (required)
        :type wallet_id: str
        :param address_id: The ID of the address to fetch the staking operation for. (required)
        :type address_id: str
        :param staking_operation_id: The ID of the staking operation. (required)
        :type staking_operation_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        _param = self._get_staking_operation_serialize(
            wallet_id=wallet_id,
            address_id=address_id,
            staking_operation_id=staking_operation_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            "200": "StakingOperation",
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )

    @validate_call
    def get_staking_operation_without_preload_content(
        self,
        wallet_id: Annotated[
            StrictStr, Field(description="The ID of the wallet the address belongs to")
        ],
        address_id: Annotated[
            StrictStr,
            Field(description="The ID of the address to fetch the staking operation for."),
        ],
        staking_operation_id: Annotated[
            StrictStr, Field(description="The ID of the staking operation.")
        ],
        _request_timeout: None
        | Annotated[StrictFloat, Field(gt=0)]
        | tuple[Annotated[StrictFloat, Field(gt=0)], Annotated[StrictFloat, Field(gt=0)]] = None,
        _request_auth: dict[StrictStr, Any] | None = None,
        _content_type: StrictStr | None = None,
        _headers: dict[StrictStr, Any] | None = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get the latest state of a staking operation

        Get the latest state of a staking operation.

        :param wallet_id: The ID of the wallet the address belongs to (required)
        :type wallet_id: str
        :param address_id: The ID of the address to fetch the staking operation for. (required)
        :type address_id: str
        :param staking_operation_id: The ID of the staking operation. (required)
        :type staking_operation_id: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """
        _param = self._get_staking_operation_serialize(
            wallet_id=wallet_id,
            address_id=address_id,
            staking_operation_id=staking_operation_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index,
        )

        _response_types_map: dict[str, str | None] = {
            "200": "StakingOperation",
        }
        response_data = self.api_client.call_api(*_param, _request_timeout=_request_timeout)
        return response_data.response

    def _get_staking_operation_serialize(
        self,
        wallet_id,
        address_id,
        staking_operation_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:
        _host = None

        _collection_formats: dict[str, str] = {}

        _path_params: dict[str, str] = {}
        _query_params: list[tuple[str, str]] = []
        _header_params: dict[str, str | None] = _headers or {}
        _form_params: list[tuple[str, str]] = []
        _files: dict[str, str | bytes] = {}
        _body_params: bytes | None = None

        # process the path parameters
        if wallet_id is not None:
            _path_params["wallet_id"] = wallet_id
        if address_id is not None:
            _path_params["address_id"] = address_id
        if staking_operation_id is not None:
            _path_params["staking_operation_id"] = staking_operation_id
        # process the query parameters
        # process the header parameters
        # process the form parameters
        # process the body parameter

        # set the HTTP header `Accept`
        if "Accept" not in _header_params:
            _header_params["Accept"] = self.api_client.select_header_accept(["application/json"])

        # authentication setting
        _auth_settings: list[str] = []

        return self.api_client.param_serialize(
            method="GET",
            resource_path="/v1/wallets/{wallet_id}/addresses/{address_id}/staking_operations/{staking_operation_id}",
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth,
        )
