from decimal import Decimal
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .model import User, RecurringOrder

app = FastAPI(
    title="Investifi Backend Coding Challenge",
)


@app.get("/")
def hello_world():
    return {"hello": "world"}


# Data model for POST request
class RecurringOrderRequest(BaseModel):
    user_id: str
    crypto: str
    frequency: str
    amount: Decimal


# this is the get recurring-orders for a user. This route is functioning.
@app.get("/recurring-orders")
def get_recurring_orders(user_id: str):
    if not user_id:
        raise HTTPException(status_code=400, detail="User ID is required")
    try:
        # Return all recurring orders associated with the user
        orders = RecurringOrder.query(hash_key=user_id)
        return orders
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Added this route to test the list of user. The route is functioning and is being used by the recurring-orders [POST]
@app.get("/users")
def get_user(user_id: str):
    if not user_id:
        raise HTTPException(status_code=400, detail="User ID is required")
    try:
        # Query the existing users for the given user_id
        users = list(User.query(hash_key=user_id))  # using list to make sure if the list is empty to return False
        result = [{"ID": u.hash_key, "First Name": u.info.first_name, "Last Name": u.info.last_name} for u in users]
        return False if not users else result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# This is the recurring-order post and it's fully functioning.
@app.post("/recurring-orders")
def post_recurring_orders(order: RecurringOrderRequest):
    try:
        user_exist = get_user(order.user_id)
        # Check if the user exists.
        if not user_exist:
            raise HTTPException(status_code=400, detail="User does not exists")
        existing_orders = RecurringOrder.query(hash_key=order.user_id)
        # Check if the user has a recurring order already for the given crypto
        if order.crypto not in ('BTC', 'ETH'):
            raise HTTPException(status_code=400, detail="Not a valid crypto")
        # Check if the user has a recurring order already for the given frequency
        elif order.frequency not in ('Daily', 'Bi-Monthly'):
            raise HTTPException(status_code=400, detail="Not a valid frequency")
        # Check if the user has a request is for a valid amount (valid amount is above 0)
        elif order.amount <= 0:
            raise HTTPException(status_code=400, detail="Not a valid amount")
        else:  # Check if there's no recurring for the given crypto/frequency
            for d in existing_orders:
                if d.crypto == order.crypto and d.frequency == order.frequency:
                    raise HTTPException(status_code=400, detail="Recurring order already exists for this crypto/frequency")
        # If no recurring of that given crypto/frequency for that user, then create the recurring order.
        new_order = RecurringOrder(
            hash_key=order.user_id,
            range_key=f"{order.user_id}-{order.crypto}-{order.frequency}",
            crypto=order.crypto,
            frequency=order.frequency,
            amount=order.amount,
        )
        new_order.save()
        return "Recurring order was created successfully"
    except Exception as e:
        return e
