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
from typing import Any, ClassVar

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing_extensions import Self

from cdp.client.models.staking_operation_metadata import StakingOperationMetadata
from cdp.client.models.transaction import Transaction


class StakingOperation(BaseModel):
    """A list of onchain transactions to help realize a staking action."""

    id: StrictStr = Field(description="The unique ID of the staking operation.")
    wallet_id: StrictStr | None = Field(
        default=None, description="The ID of the wallet that owns the address."
    )
    network_id: StrictStr = Field(description="The ID of the blockchain network.")
    address_id: StrictStr = Field(
        description="The onchain address orchestrating the staking operation."
    )
    status: StrictStr = Field(description="The status of the staking operation.")
    transactions: list[Transaction] = Field(
        description="The transaction(s) that will execute the staking operation onchain."
    )
    metadata: StakingOperationMetadata | None = None
    __properties: ClassVar[list[str]] = [
        "id",
        "wallet_id",
        "network_id",
        "address_id",
        "status",
        "transactions",
        "metadata",
    ]

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["initialized", "complete", "failed", "unspecified"]):
            raise ValueError(
                "must be one of enum values ('initialized', 'complete', 'failed', 'unspecified')"
            )
        return value

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
        """Create an instance of StakingOperation from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in transactions (list)
        _items = []
        if self.transactions:
            for _item_transactions in self.transactions:
                if _item_transactions:
                    _items.append(_item_transactions.to_dict())
            _dict["transactions"] = _items
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict["metadata"] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of StakingOperation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "wallet_id": obj.get("wallet_id"),
                "network_id": obj.get("network_id"),
                "address_id": obj.get("address_id"),
                "status": obj.get("status"),
                "transactions": [Transaction.from_dict(_item) for _item in obj["transactions"]]
                if obj.get("transactions") is not None
                else None,
                "metadata": StakingOperationMetadata.from_dict(obj["metadata"])
                if obj.get("metadata") is not None
                else None,
            }
        )
        return _obj
