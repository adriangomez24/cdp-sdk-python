"""Coinbase Platform API

This is the OpenAPI 3.0 specification for the Coinbase Platform APIs, used in conjunction with the Coinbase Platform SDKs.

The version of the OpenAPI document: 0.0.1-alpha
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from datetime import datetime
from typing import Any, ClassVar

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing_extensions import Self

from cdp.client.models.ethereum_transaction_access_list import EthereumTransactionAccessList
from cdp.client.models.ethereum_transaction_flattened_trace import EthereumTransactionFlattenedTrace


class EthereumTransaction(BaseModel):
    """EthereumTransaction"""

    var_from: StrictStr = Field(description="The onchain address of the sender.", alias="from")
    gas: StrictInt | None = Field(
        default=None, description="The amount of gas spent in the transaction."
    )
    gas_price: StrictInt | None = Field(
        default=None,
        description="The price per gas spent in the transaction in atomic units of the native asset.",
    )
    hash: StrictStr | None = Field(
        default=None,
        description="The hash of the transaction as a hexadecimal string, prefixed with 0x.",
    )
    input: StrictStr | None = Field(default=None, description="The input data of the transaction.")
    nonce: StrictInt | None = Field(
        default=None, description="The nonce of the transaction in the source address."
    )
    to: StrictStr = Field(description="The onchain address of the receiver.")
    index: StrictInt | None = Field(
        default=None, description="The index of the transaction in the block."
    )
    value: StrictStr | None = Field(
        default=None,
        description="The value of the transaction in atomic units of the native asset.",
    )
    type: StrictInt | None = Field(
        default=None,
        description="The EIP-2718 transaction type. See https://eips.ethereum.org/EIPS/eip-2718 for more details.",
    )
    max_fee_per_gas: StrictInt | None = Field(
        default=None,
        description="The max fee per gas as defined in EIP-1559. https://eips.ethereum.org/EIPS/eip-1559 for more details.",
    )
    max_priority_fee_per_gas: StrictInt | None = Field(
        default=None,
        description="The max priority fee per gas as defined in EIP-1559. https://eips.ethereum.org/EIPS/eip-1559 for more details.",
    )
    priority_fee_per_gas: StrictInt | None = Field(
        default=None,
        description="The confirmed priority fee per gas as defined in EIP-1559. https://eips.ethereum.org/EIPS/eip-1559 for more details.",
    )
    transaction_access_list: EthereumTransactionAccessList | None = None
    flattened_traces: list[EthereumTransactionFlattenedTrace] | None = None
    block_timestamp: datetime | None = Field(
        default=None, description="The timestamp of the block in which the event was emitted"
    )
    mint: StrictStr | None = Field(
        default=None,
        description="This is for handling optimism rollup specific EIP-2718 transaction type field.",
    )
    __properties: ClassVar[list[str]] = [
        "from",
        "gas",
        "gas_price",
        "hash",
        "input",
        "nonce",
        "to",
        "index",
        "value",
        "type",
        "max_fee_per_gas",
        "max_priority_fee_per_gas",
        "priority_fee_per_gas",
        "transaction_access_list",
        "flattened_traces",
        "block_timestamp",
        "mint",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self | None:
        """Create an instance of EthereumTransaction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of transaction_access_list
        if self.transaction_access_list:
            _dict["transaction_access_list"] = self.transaction_access_list.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in flattened_traces (list)
        _items = []
        if self.flattened_traces:
            for _item_flattened_traces in self.flattened_traces:
                if _item_flattened_traces:
                    _items.append(_item_flattened_traces.to_dict())
            _dict["flattened_traces"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of EthereumTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "from": obj.get("from"),
                "gas": obj.get("gas"),
                "gas_price": obj.get("gas_price"),
                "hash": obj.get("hash"),
                "input": obj.get("input"),
                "nonce": obj.get("nonce"),
                "to": obj.get("to"),
                "index": obj.get("index"),
                "value": obj.get("value"),
                "type": obj.get("type"),
                "max_fee_per_gas": obj.get("max_fee_per_gas"),
                "max_priority_fee_per_gas": obj.get("max_priority_fee_per_gas"),
                "priority_fee_per_gas": obj.get("priority_fee_per_gas"),
                "transaction_access_list": EthereumTransactionAccessList.from_dict(
                    obj["transaction_access_list"]
                )
                if obj.get("transaction_access_list") is not None
                else None,
                "flattened_traces": [
                    EthereumTransactionFlattenedTrace.from_dict(_item)
                    for _item in obj["flattened_traces"]
                ]
                if obj.get("flattened_traces") is not None
                else None,
                "block_timestamp": obj.get("block_timestamp"),
                "mint": obj.get("mint"),
            }
        )
        return _obj
