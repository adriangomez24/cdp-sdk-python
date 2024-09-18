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

from cdp.client.models.transaction_content import TransactionContent


class Transaction(BaseModel):
    """An onchain transaction."""

    network_id: StrictStr = Field(description="The ID of the blockchain network.")
    block_hash: StrictStr | None = Field(
        default=None, description="The hash of the block at which the transaction was recorded."
    )
    block_height: StrictStr | None = Field(
        default=None, description="The block height at which the transaction was recorded."
    )
    from_address_id: StrictStr = Field(description="The onchain address of the sender.")
    to_address_id: StrictStr | None = Field(
        default=None, description="The onchain address of the recipient."
    )
    unsigned_payload: StrictStr = Field(
        description="The unsigned payload of the transaction. This is the payload that needs to be signed by the sender."
    )
    signed_payload: StrictStr | None = Field(
        default=None,
        description="The signed payload of the transaction. This is the payload that has been signed by the sender.",
    )
    transaction_hash: StrictStr | None = Field(
        default=None, description="The hash of the transaction."
    )
    transaction_link: StrictStr | None = Field(
        default=None,
        description="The link to view the transaction on a block explorer. This is optional and may not be present for all transactions.",
    )
    status: StrictStr = Field(description="The status of the transaction.")
    content: TransactionContent | None = None
    __properties: ClassVar[list[str]] = [
        "network_id",
        "block_hash",
        "block_height",
        "from_address_id",
        "to_address_id",
        "unsigned_payload",
        "signed_payload",
        "transaction_hash",
        "transaction_link",
        "status",
        "content",
    ]

    @field_validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(
            ["pending", "signed", "broadcast", "complete", "failed", "unspecified"]
        ):
            raise ValueError(
                "must be one of enum values ('pending', 'signed', 'broadcast', 'complete', 'failed', 'unspecified')"
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
        """Create an instance of Transaction from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of content
        if self.content:
            _dict["content"] = self.content.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict[str, Any] | None) -> Self | None:
        """Create an instance of Transaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "network_id": obj.get("network_id"),
                "block_hash": obj.get("block_hash"),
                "block_height": obj.get("block_height"),
                "from_address_id": obj.get("from_address_id"),
                "to_address_id": obj.get("to_address_id"),
                "unsigned_payload": obj.get("unsigned_payload"),
                "signed_payload": obj.get("signed_payload"),
                "transaction_hash": obj.get("transaction_hash"),
                "transaction_link": obj.get("transaction_link"),
                "status": obj.get("status"),
                "content": TransactionContent.from_dict(obj["content"])
                if obj.get("content") is not None
                else None,
            }
        )
        return _obj