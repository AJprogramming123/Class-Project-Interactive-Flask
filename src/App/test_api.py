from api_request import check_email_breach

email = "example@example.com"
data = check_email_breach(email)

if data:
    print("Success:", data)
else:
    print("No data or error.")
