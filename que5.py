data = [
    {"name": "Rohit", "amount": 500, "status": "success"},
    {"name": "Priya", "amount": 1200, "status": "failed"},
    {"name": "Aman", "amount": 700, "status": "success"},
    {"name": "Neha", "amount": 1500, "status": "pending"},
    {"name": "Rahul", "amount": 300, "status": "success"},
    {"name": "Sita", "amount": 2000, "status": "failed"},
    {"name": "Arjun", "amount": 950, "status": "success"}
]

# Filter transactions with status "success" 
successful_transactions =filter(lambda x: x['status'] == 'success', data)
amount_list = list(map(lambda x: x['amount'], successful_transactions))
from functools import reduce
total_amount= reduce(lambda x, y: x + y, amount_list)