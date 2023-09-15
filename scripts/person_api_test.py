import requests

# Define the base URL of your API
BASE_URL = 'http://127.0.0.1:8000/'  # Replace with your API's base URL

def add_person():
    # Create a new person (POST request)
    person_data = {
        'first_name': 'John6',
        'last_name': 'doe6',
        'age': 30,
    }

    response = requests.post(BASE_URL + 'create/', json=person_data)
    print("Add Person Response:")
    print(response.status_code)
    print(response.text)
    if response.status_code == 201:
        print("Person added successfully")
    else:
        print("Failed to add person")


def fetch_person(identifier):
    # Fetch details of a person (GET request)
    response = requests.get(BASE_URL + identifier + '/')

    if response.status_code == 200:
        person_data = response.json()
        print("Person details:")
        print(f"First Name: {person_data['first_name']}")
        print(f"Last Name: {person_data['last_name']}")
        print(f"Age: {person_data['age']}")
    else:
        print("Failed to fetch person details")

def modify_person(identifier, new_data):
    # Modify the details of an existing person (PUT request)
    response = requests.put(BASE_URL + identifier + '/', data=new_data)

    if response.status_code == 200:
        print("Person details updated successfully")
    else:
        print("Failed to update person details")

def remove_person(identifier):
    # Remove a person (DELETE request)
    response = requests.delete(BASE_URL + identifier + '/')

    if response.status_code == 204:
        print("Person removed successfully")
    else:
        print("Failed to remove person")

if __name__ == "__main__":
    # Test each CRUD operation
    add_person()
    fetch_person('John6')  # Use the identifier of the person you added
    modify_person('John6', {'age': 31})  # Update the age
    remove_person('John6')  # Remove the person
