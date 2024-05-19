# Niyo Group Backend Developer Assessment – Damilola Olagunju

This is the repo to the Backend Developer Assessment for Niyo Group

## Table of Contents

- [Development Setup](#development-setup)
- [API](#api)

## Development Setup

To set up the project locally, please make sure you have [Docker](https://www.docker.com/products/docker-desktop/) installed.

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd niyo-group-interview
    ```

3. Run the docker container:

    ```bash
    docker compose up
    ```

    The project will be running at `http://0.0.0.0:8000`.


## Data models 

This project has two data models: `User`, and `Task`. The `Task` model has a foreign key to the `User` model via the `assigned_to` attr.

### `User`
```python
    """
    This model is used to represent a user.

    Attributes:
    -----------
    id : UUIDField
        The id of the user.
    created : DateTimeField
        The date and time the user was created.
    modified : DateTimeField
        The date and time the user was last modified.
    is_active : BooleanField
        The status of the user.
    is_verified : BooleanField
        The verification status of the user.
    is_superuser : BooleanField
        The superuser status of the user.
    is_staff : BooleanField
        The staff status of the user.
    email : EmailField
        The email of the user.
    first_name : CharField
        The first name of the user.
    last_name : CharField
        The last name of the user.
    """
```

### Task
```python
    """
    Task model

    This model is used to represent a task.

    Attributes:
    -----------
    id : UUIDField
        The id of the task.
    created : DateTimeField
        The date and time the task was created.
    modified : DateTimeField
        The date and time the task was last modified.
    title : CharField
        The title of the task.
    description : TextField
        The description of the task.
    completed : BooleanField
        The completion status of the task.
    due_date : DateField
        The due date of the task.
    assigned_to : ForeignKey
        The User the task is assigned to.

    Methods:
    --------
    __str__()
        Returns the title of the task as a string.
    """
```

## API

The project exposes the following endpoints:

### `/api/users/`
- `GET /api/users/token/`: login endpoint to authenticate a registred user and return the JWT token
- `POST /api/users/token/refresh`: endpoint to refresh an expired token
- `POST /api/users/register`: endpoint to register a user

### `/api/tasks/`
- `GET /api/tasks/`: endpoint to list all the tasks assigned to the authenticated user
- `GET /api/tasks/{pk}/`: endpoint to retreive a single task
- `PUT /api/tasks/{pk}/`: endpoint to update a single task
- `DELETE /api/tasks/{pk}/`: endpoint to delete a single task
