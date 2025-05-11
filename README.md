# Coding Challenge Readme

Welcome to the Investifi Backend Engineering coding challenge! This challenge is designed to assess your coding skills, problem-solving abilities, and "grit". Before you begin, please take a moment to read through this readme to understand the challenge requirements, instructions, and guidelines.

## Challenge Description

Investifi challange completed by adding 3 routes. First route /recurring-orders which will return all recurring orders for a given user, the second is /users which will return all available users on the users db. The last is /recurring-orders which is a POST route to submit a recurring order for a given user. I used the method associated with the route users to check if the user exists already or not. Optimized the code for better readability. the recurring-orders post route will have the validation before submitting any new recurring for the user. It will validate if the order is coming with a valid amount, it will also check if the request submitted for ETH/BTC only and the recurring type is Daily/Bi-Monthly only, and will validate as well if there are no recurring like that in the DB before it save the request

### Challenge Items
- A POST route that allows a user to input a recurring order (COMPLETED)
- A GET route to return said user's recurring orders (COMPLETED)
  - For example - I pass in User `1`, I will receive all recurring orders for User `1`
- A recurring order can be for BTC or ETH only (validation check) (COMPLETED)
- A recurring order's frequency can be Daily or Bi-Monthly only (validation check) (COMPLETED)
- A recurring order must have an associated USD amount with it greater than 0. (COMPLETED)
- A recurring order must be associated with a user (COMPLETED)
- A user can only ever have 1 recurring order for a given crypto/frequency pair (COMPLETED)
  - For example: a User can only have 1 recurring order with a `Daily` frequency and for crypto `BTC`. If a second recurring order were to be placed for  `Daily`/`BTC` a validation error is expected to be raised

## Getting Started

Inserted into the DB the below users in the users table.

{
  "hash_key": "1",
  "range_key": "info",
  "info": {
    "first_name": "David",
    "last_name": "Tano"
  }
},
{
  "hash_key": "2",
  "range_key": "info",
  "info": {
    "first_name": "Sara",
    "last_name": "James"
  }
}

===================== VALID POST REQUESTS =====================

curl -X POST "http://127.0.0.1:8000/recurring-orders" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "1", "crypto": "BTC", "frequency": "Daily", "amount": 100}'

curl -X POST "http://127.0.0.1:8000/recurring-orders" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "1", "crypto": "ETH", "frequency": "Daily", "amount": 100}'

curl -X POST "http://127.0.0.1:8000/recurring-orders" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "1", "crypto": "BTC", "frequency": "Bi-Monthly", "amount": 100}'

curl -X POST "http://127.0.0.1:8000/recurring-orders" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "1", "crypto": "ETH", "frequency": "Bi-Monthly", "amount": 100}'

===================== INVALID POST REQUESTS =====================

curl -X POST "http://127.0.0.1:8000/recurring-orders" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "1", "crypto": "ADA", "frequency": "Daily", "amount": 100}'

curl -X POST "http://127.0.0.1:8000/recurring-orders" \
     -H "Content-Type: application/json" \
     -d '{"user_id": "1", "crypto": "BTC", "frequency": "Yearly", "amount": 100}'

===================== OTHER ROUTES =====================

-- GET REQUESTS
curl "http://127.0.0.1:8000/users?user_id=2"
curl "http://127.0.0.1:8000/recurring-orders?user_id=1"
