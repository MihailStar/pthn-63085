# 1
user = {
    "id": 4170,
    "uid": "5e941db5-9e0f-4f94-9fc5-734110c6be14",
    "password": "SyUpfo1ljm",
    "first_name": "Teresa",
    "last_name": "Wehner",
    "username": "teresa.wehner",
    "email": "teresa.wehner@email.com",
    "gender": "Non-binary",
    "phone_number": "+674 424.561.2776",
    "social_insurance_number": "637316241",
    "date_of_birth": "1993-08-17",
    "employment": {"title": "Central Hospitality Liaison", "key_skill": "Organisation"},
    "subscription": {
        "plan": "Essential",
        "status": "Idle",
        "payment_method": "Debit card",
        "term": "Annual",
    },
}
keys = input().split()
print({key: user[key] for key in keys})


# 2
people = [
    ["Amy Smith", "694.322.8133x22426"],
    ["Brian Shaw", "593.662.5217x338"],
    ["Christian Sharp", "118.197.8810"],
    ["Sean Schmidt", "9722527521"],
    ["Thomas Long", "163.814.9938"],
    ["Joshua Willis", "+1-978-530-6971x601"],
    ["Ann Hoffman", "434.104.4302"],
    ["John Leonard", "(956)182-8435"],
    ["Daniel Ross", "870-365-8303x416"],
    ["Jacqueline Moon", "+1-757-865-4488x652"],
    ["Gregory Baker", "705-576-1122"],
    ["Michael Spencer", "(922)816-0599x7007"],
    ["Austin Vazquez", "399-813-8599"],
    ["Chad Delgado", "979.908.8506x886"],
    ["Jonathan Gilbert", "9577853541"],
]
phone_book = {k: n for n, k in people}
