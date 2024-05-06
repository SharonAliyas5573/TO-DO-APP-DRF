# TO_DO_DRF

TO_DO_DRF is a Django REST Framework project for managing tasks.

## Features

- User registration and authentication
- CRUD operations for tasks
- Filtering tasks by status and priority
- JWT token authentication

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/SharonAliyas5573/TO-DO-APP-DRF.git
2. Install the requirements:
    ```sh
    python manage.py migrate
3. Run the server:
    ```sh
    python manage.py runserver


# API Documentation

## Auth
1. ### Register User

    - **Endpoint:** `POST auth/register/`

    - **Description:** Creates a new user.

    - **Request Body:**

        ```json
        {
        "username": "string",
        "password": "string"
        }

        ```
    - **Responses**:

        - ```201 Created```: User created successfully. Returns the user details.
        - ```400 Bad Request```: Validation errors. Returns the errors.

2. ### Login User
    - **Endpoint**: POST auth/login/

    - **Description**: Authenticates a user and returns a JWT token.

    - **Request Body**:
        ``` json
        {
        "username": "string",
        "password": "string"
        }
        ```
    - **Responses**:

        - ```200 OK```: Authentication successful. Returns a JWT token in the access_token field of the response body.
        - ```400 Bad Request```: Wrong credentials. Returns an error message.
3. ### Logout User
    - ***Endpoint***: POST auth/logout/

    - ***Description***: Deletes the JWT token for the authenticated user, effectively logging out the user.

    - ***Headers***: 
        ```json
        {
        "Authorization": "<token>"
        }
        ```
    - ***Responses***:

        - ```200 OK```: User logged out successfully. Returns a success message.
        - ```401 Unauthorized```: User not authenticated.

## Task

***Headers***:

``` json
    {
    "Authorization": "<token>"
    }
```

1. ### List Tasks
    - ***Endpoint***: ```GET /tasks/```

    - ***Description***: Returns a list of tasks for the authenticated user.

    - ***Query Parameters***:

        - **status** : Filters tasks by status. Possible values are '**completed**', '**expired**', and '**active**'.
        - **priority** : Filters tasks by priority. Can be a comma-separated list of priorities. Possible values are '**L**', '**M**', and '**H**'.

    - ***Responses***:
        - ```200 OK```: Returns a list of tasks.
2. ### Create Task
    - ***Endpoint***: ```POST /tasks/```

    - ***Description***: Creates a new task for the authenticated user.
    - ***Request Body***: 
        ```json
        {
        "title": "string",
        "description": "string",
        "priority": "string",
        "deadline": "string"
        }
        ```
    - ***Responses***:
        - ```201 Created```: Task created successfully. Returns the task details.
        - ```400 Bad Request```: Validation errors. Returns the errors.

3. ### Retrieve Task
    - ***Endpoint***: ```GET /tasks/{id}/```
    - ***Description***: Retrieves the details of a task for the authenticated user.
    - ***Responses***:
        - ```200 OK```: Returns the task details.
        - ```404 Not Found```: Task not found.

4. ### Update Task
    - ***Endpoint***: ```PUT /tasks/{id}/```
    - ***Description***: Updates a task for the authenticated user.
    - ***Request Body***:
        ```json
        {
        "title": "string",
        "description": "string",
        "priority": "string",
        "deadline": "string"
        }
        ```
    - ***Responses***:
        - ```200 OK```: Task updated successfully. Returns the updated task details.
        - ```400 Bad Request```: Validation errors. Returns the errors.
        - ```404 Not Found```: Task not found.

5. ### Delete Task
    - ***Endpoint***: ```DELETE /tasks/{id}/```
    - ***Description***: Deletes a task for the authenticated user.
    - ***Responses***:
        - ```204 No Content```: Task deleted successfully.
        - ```404 Not Found```: Task not found.        

