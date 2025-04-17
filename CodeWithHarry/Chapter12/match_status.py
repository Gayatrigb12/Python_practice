def get_status_message(status: int) -> str:
    match status:
        case 200:
            return "OK - The request was successful."
        case 201:
            return "Created - The resource was created successfully."
        case 400:
            return "Bad Request - The server could not understand the request."
        case 401:
            return "Unauthorized - Authentication is required."
        case 403:
            return "Forbidden - You don’t have permission to access this."
        case 404:
            return "Not Found - The resource could not be found."
        case 500:
            return "Internal Server Error - Something went wrong on the server."
        case _:
            return "Unknown status code."

# Input and usage
status = int(input("Enter status code (e.g., 200, 404, 500): "))
message = get_status_message(status)
print(message)
