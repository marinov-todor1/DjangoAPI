### Design Notes
Due to no specific instructions, the following assumptions were made:

1. Token Authentication is not required
2. Users are not limited only to records associated with their accounts, but can access all data

## How to use

### Methods for register/

GET register/ - Show instructions

Example Response
```json
{
    "instructions": "please register by submitting the following information",
    "email": "",
    "username": "",
    "first_name": "",
    "age": "",
    "driving_license_exp_date": ""
}
```
POST register/ - Create new user

Example Request in body --> form-data
```
email = sample@email
username = TestUserName
password = SomePassword123
repeat_password = SomePassword123
first_name = MyName
age = 33
driving_license_exp_date = YYYY-MM-DD
```
Example Response
```json
{
    "response": "successfully registered new user.",
    "email": "test10@emai.co",
    "username": "My10NewUser",
    "age": 25,
    "driving_license_exp_date": "2024-12-24"
}
```
---
### Methods for usercars/
GET usercars/ - Return all cars in the DB

Example Response
```json
[
    {
        "id": 1,
        "user": 2,
        "car_brand": 1,
        "car_model": 1,
        "first_reg": "2020-10-10",
        "odometer": 5000
    },
    {
        "id": 2,
        "user": 3,
        "car_brand": 2,
        "car_model": 2,
        "first_reg": "2024-10-14",
        "odometer": 50000
    }
]
```
POST usercars/ - Create new car
Example Request in body --> form-data
```
user = 2
car_brand = 1
car_model = 1
first_reg = 2020-10-10
odometer = 5000
```

Example Response
```json

{
    "id": 1,
    "user": 2,
    "car_brand": 1,
    "car_model": 1,
    "first_reg": "2020-10-10",
    "odometer": 5000
}
```
---
### Methods for usercar/id/
GET usercar/id/ - Returns details for a specific car by its id field

Example Response
```json
{
    "id": 2,
    "user": 3,
    "car_brand": 2,
    "car_model": 2,
    "first_reg": "2024-10-14",
    "odometer": 50000
}
```
PUT usercar/id/ - Change details for a specific car by its id field

Example Request in body --> form-data
```
user = 3
car_brand = 2
car_model = 2
first_reg = 2024-10-14
odometer = 50000
```

Example Response
```json
{
    "id": 2,
    "user": 3,
    "car_brand": 2,
    "car_model": 2,
    "first_reg": "2024-10-14",
    "odometer": 50000
}
```
DELETE usercar/id/ - Delete car record

No response is returned

---
### Methods for brands/
GET brands/ - Returns all brands in the DB

Example Response
```json
[
    {
        "id": 1,
        "brand_name": "Toyota"
    },
    {
        "id": 2,
        "brand_name": "VW"
    }
]
```
POST brands/ - Create new brand

Example Request in body --> form-data
```
brand_name = Mercedes
```
Example Response
```
{
    "id": 3,
    "brand_name": "Mercedes"
}
```
PUT brands/id/ - Edit brand record

Example Request in body --> form-data
```
brand_name = Tesla
```
Example Response
```
{
    "id": 3,
    "brand_name": "Tesla"
}
```
DELETE brands/id/ - Delete brand record

No response is returned

---
### Methods for models/
GET models/ - Returns all models in the DB

Example Response
```json
[
    {
        "id": 1,
        "name": "Avensis",
        "brand": 1
    },
    {
        "id": 2,
        "name": "Passat",
        "brand": 2
    }
]
```
POST models/ - Create new model

Example Request in body --> form-data
```
name = Auris
brand = 1
```
Example Response
```json
{
    "id": 3,
    "name": "Auris",
    "brand": 1
}
```

PUT models/id/ - Edit model

Example Request in body --> form-data
```
name = yaris
brand = 1
```
Example Response
```json
{
    "id": 3,
    "name": "yaris",
    "brand": 1
}
```
DELETE models/id/ - Delete model record

No response is returned

---
### Methods for accounts/
GET accounts/ - Returns all registered accounts

Example Response
```json
[
    {
        "id": 2,
        "age": 20,
        "driving_license_exp_date": "2020-10-10",
        "first_name": "ThirdUser",
        "email": "test3@emai.co"
    },
    {
        "id": 3,
        "age": 25,
        "driving_license_exp_date": "2024-12-24",
        "first_name": "FirstUser",
        "email": "test1@emai.co"
    }
]
```
PUT accounts/id/ - Edit account record

Example Request in body --> form-data
```
first_name = childish
age = 14
```
Example Response
```json
{
    "id": 3,
    "age": 14,
    "driving_license_exp_date": "2024-12-24",
    "first_name": "childish",
    "email": "test1@emai.co"
}
```
---