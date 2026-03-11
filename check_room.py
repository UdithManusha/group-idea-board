import requests

def check_hostel_room(student_id):
    """
    Function to check hostel room number using the UCSC Student Portal Official API.
    
    Args:
        student_id (str): The student's ID number.
    
    Returns:
        str: The hostel room number if successful, or an error message.
    """
    # Assuming the API endpoint is a GET request to retrieve room info
    # Note: This is a fictional API based on the name provided. In a real scenario, 
    # consult the official API documentation for exact endpoints and parameters.
    url = f"https://ucsc-student-portal-official-api.com/hostel/room?student_id={student_id}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        
        data = response.json()
        room_number = data.get('room_number')
        if room_number:
            return f"Your hostel room number is: {room_number}"
        else:
            return "Room number not found in the response."
    except requests.exceptions.RequestException as e:
        return f"Error fetching room number: {str(e)}"

if __name__ == "__main__":
    student_id = input("Enter your student ID: ")
    result = check_hostel_room(student_id)
    print(result)