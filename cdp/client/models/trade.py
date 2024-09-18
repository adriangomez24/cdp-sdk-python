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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing_extensions import Self

from cdp.client.models.asset import Asset
from cdp.client.models.transaction import Transaction


class Trade(BaseModel):
    """A trade of an asset to another asset"""

    network_id: StrictStr = Field(description="The ID of the blockchain network")
    wallet_id: StrictStr = Field(description="The ID of the wallet that owns the from address")
    address_id: StrictStr = Field(description="The onchain address of the sender")
    trade_id: StrictStr = Field(description="The ID of the trade")
    from_amount: StrictStr = Field(
        description="The amount of the from asset to be traded (in atomic units of the from asset)"
    )
    from_asset: Asset
    to_amount: StrictStr = Field(
        description="The amount of the to asset that will be received (in atomic units of the to asset)"
    )
    to_asset: Asset
    transaction: Transaction
    approve_transaction: Transaction | None = None
    __properties: ClassVar[list[str]] = [
        "network_id",
        "wallet_id",
        "address_id",
        "trade_id",
        "from_amount",
        "from_asset",
        "to_amount",
        "to_asset",
        "transaction",
        "approve_transaction",
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
        """Create an instance of Trade from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of from_asset
        if self.from_asset:
            _dict["from_asset"] = self.from_asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of to_asset
        if self.to_asset:
            _dict["to_asset"] = self.to_asset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict["transaction"] = self.transaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of approve_transaction
        if self.approve_transaction:
            _dict["approve_transaction"] = self.approve_transaction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of Trade from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "network_id": obj.get("network_id"),
                "wallet_id": obj.get("wallet_id"),
                "address_id": obj.get("address_id"),
                "trade_id": obj.get("trade_id"),
                "from_amount": obj.get("from_amount"),
                "from_asset": Asset.from_dict(obj["from_asset"])
                if obj.get("from_asset") is not None
                else None,
                "to_amount": obj.get("to_amount"),
                "to_asset": Asset.from_dict(obj["to_asset"])
                if obj.get("to_asset") is not None
                else None,
                "transaction": Transaction.from_dict(obj["transaction"])
                if obj.get("transaction") is not None
                else None,
                "approve_transaction": Transaction.from_dict(obj["approve_transaction"])
                if obj.get("approve_transaction") is not None
                else None,
            }
        )
        return _obj
