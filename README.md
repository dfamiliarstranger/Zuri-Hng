# Zuri-Hng
This is my Zuri Hng solution folder for task 1 and Task 2

```markdown
# Person API
 A simple REST API capable of CRUD operations on a "person" resource, interfacing with any database of your choice. Your API should dynamically handle parameters, such as adding or retrieving a person by name.

## Table of Contents

- [Installation](#installation)
- [Running the API](#running-the-api)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [UML Diagram](#uml-diagram)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (version 3.10.4)
- Django (version 4.2.5)
- Django Rest Framework (version 3.14.0)
- charset-normalizer==3.2.0
- asgiref==3.7.2
- idna==3.4
- certifi==2023.7.22
- pytz==2023.3.post1
- requests==2.31.0
- sqlparse==0.4.4
- urllib3==2.0.4
- typing_extensions==4.7.1
- tzdata==2023.3


### Installation Steps

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-api
   ```

3. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

4. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Running the API

1. Run database migrations:

   ```bash
   python manage.py migrate
   ```

2. Start the development server:

   `bash
   python manage.py runserver
   `

   The API should now be running at `http://localhost:8000/`.

## API Endpoints

- `POST /create/`: Create a new person.
- `GET /<str:identifier>/`: Fetch details of a person by their identifier.
- `PUT /<str:identifier>/`: Update the details of a person by their identifier.
- `DELETE /<str:identifier>/`: Remove a person by their identifier.

## Usage

### Adding a New Person

To add a new person, make a POST request to `/create/` with the following JSON data:

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "age": 30
}
```

### Fetching Person Details

To fetch details of a person, make a GET request to `/<str:identifier>/`, where `<str:identifier>` is the person's identifier.

### Modifying Person Details

To update the details of a person, make a PUT request to `/<str:identifier>/` with the data you want to update. For example, to change the age of a person:

```json
{
  "age": 31
}
```

### Removing a Person
To remove a person, make a DELETE request to `/<str:identifier>/`, where `<str:identifier>` is the person's identifier.

### UML Diagram
![UML Diagram](docs/uml/UMl%20TASK2.drawio.pnguml_diagram.png)


## Contributing
Contributions are welcome! Please fork this repository and create a pull request.

## License
This is my Zuri Hng solution for Task 2.
```

This README.md file provides clear instructions for setting up and running your API, as well as information on the available API endpoints and how to use them.