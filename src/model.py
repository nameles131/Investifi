from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional
import os
from dyntastic import Dyntastic


# Base Model for DynamoDB
class DynamoDbModelBase(Dyntastic):
    __table_region__ = os.environ.get("AWS_REGION")
    __table_host__ = os.environ.get("DYNAMO_ENDPOINT")
    __hash_key__ = "hash_key"
    __range_key__ = "range_key"

    @property
    def __table_name__(self):
        raise NotImplementedError

    hash_key: str = Field(default=None, title="DynamoDB Partition Key")
    range_key: str = Field(default=None, title="DynamoDB Sort Key")


# User Info Model
class UserInfo(BaseModel):
    first_name: str
    last_name: str


# User Model
class User(DynamoDbModelBase):
    __table_name__ = "User"
    info: Optional[UserInfo]


# Recurring Order Model
class RecurringOrder(DynamoDbModelBase):
    __table_name__ = "RecurringOrder"
    crypto: str
    frequency: str
    amount: Decimal
