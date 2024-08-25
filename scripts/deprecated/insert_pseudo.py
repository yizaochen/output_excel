import requests

# Define the API endpoint
api_url = "http://localhost:8000/transactions/"

# Define the pseudo data you want to insert
pseudo_data = [
    {
        "bank_slip_date": "2023-12-01",
        "customer_id": "CUST003",
        "bank_code": "CTBC002",
        "bank_slip_currency": "GBP",
        "bank_slip_amount": "36769.77",
        "customer_name": "John Doe",
        "bank_slip_customer": "Charlie Davis",
        "country": "Germany",
        "file_path": "/path/to/file_14.pdf",
        "predict_type": "C",
        "process_status": "Processing",
        "reference_number": "REF398565",
        "remit_type": "Mobile",
        "bank_slip_remark": "Check Details",
        "change_date": "2023-09-18",
        "ar_no": "AR67890",
    },
    {
        "bank_slip_date": "2023-09-15",
        "customer_id": "CUST001",
        "bank_code": "CTBC005",
        "bank_slip_currency": "AUD",
        "bank_slip_amount": "15844.96",
        "customer_name": "Jane Smith",
        "bank_slip_customer": "John Doe",
        "country": "USA",
        "file_path": "/path/to/file_12.pdf",
        "predict_type": "A",
        "process_status": "Fail",
        "reference_number": "REF752842",
        "remit_type": "ATM",
        "bank_slip_remark": "N/A",
        "change_date": "2023-12-19",
        "ar_no": "AR09876",
    },
    {
        "bank_slip_date": "2023-12-19",
        "customer_id": "CUST005",
        "bank_code": "CTBC005",
        "bank_slip_currency": "USD",
        "bank_slip_amount": "32209.00",
        "customer_name": "Jane Smith",
        "bank_slip_customer": "Charlie Davis",
        "country": "Japan",
        "file_path": "/path/to/file_22.pdf",
        "predict_type": "B",
        "process_status": "Cancel",
        "reference_number": "REF697428",
        "remit_type": "Online",
        "bank_slip_remark": "Urgent",
        "change_date": "2024-04-28",
        "ar_no": "AR09876",
    },
    {
        "bank_slip_date": "2024-05-16",
        "customer_id": "CUST001",
        "bank_code": "CTBC003",
        "bank_slip_currency": "USD",
        "bank_slip_amount": "39205.61",
        "customer_name": "John Doe",
        "bank_slip_customer": "Charlie Davis",
        "country": "USA",
        "file_path": "/path/to/file_99.pdf",
        "predict_type": "A",
        "process_status": "Processing",
        "reference_number": "REF942906",
        "remit_type": "Branch",
        "bank_slip_remark": "N/A",
        "change_date": "2024-01-06",
        "ar_no": "AR12345",
    },
    {
        "bank_slip_date": "2023-11-23",
        "customer_id": "CUST005",
        "bank_code": "CTBC001",
        "bank_slip_currency": "JPY",
        "bank_slip_amount": "4444.82",
        "customer_name": "Charlie Davis",
        "bank_slip_customer": "Bob Johnson",
        "country": "USA",
        "file_path": "/path/to/file_11.pdf",
        "predict_type": "B",
        "process_status": "Finish",
        "reference_number": "REF912681",
        "remit_type": "ATM",
        "bank_slip_remark": "Approved",
        "change_date": "2023-10-05",
        "ar_no": "AR12345",
    },
]


# Function to send POST requests to create transactions
def create_transaction(data):
    response = requests.post(api_url, json=data)
    if response.status_code == 201:
        print(f"Transaction created successfully: {data['reference_number']}")
    else:
        print(f"Failed to create transaction: {response.text}")


# Loop through the pseudo data and send POST requests
for record in pseudo_data:
    create_transaction(record)
