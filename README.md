# TODO List
This is a tagging task list management app. Users can create, update, delete tasks and manage tags for more flexible task organization.

## Instructions for launching the project

**1. Repository cloning**

First, clone the project repository on your local machine:

```git clone https://github.com/olessh/Todo-list.git```

```cd todo-list```

**2. Installation of a virtual environment**

It is recommended to use a virtual environment to isolate dependencies:

```python -m venv venv```

Activate the virtual environment:

```venv\Scripts\activate #Windows```

```source venv/bin/activate #MacOS/Linux```

**3. Establishing dependencies**

Install the necessary packages from the requirements.txt file:

```pip install -r requirements.txt```

**4. Database settings**

Migrations are used to create a database structure. Run the commands to apply migrations:

```python manage.py migrate```

**5. Starting the server**

Start the local server to test the project:

```python manage.py runserver```

**6. Opening in the browser**

Open your browser and go to:

http://127.0.0.1:8000/

Now you are ready to work with the project.