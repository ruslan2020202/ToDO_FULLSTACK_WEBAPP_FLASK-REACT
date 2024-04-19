# ToDo Application

![ToDo](todo_app_image.png)

The ToDo application is a simple web application for managing tasks. With it, you can create, view, update, and delete tasks to organize your work more efficiently.

## Installation

To run the ToDo application, you'll need Docker and Docker Compose.

1. First, clone the repository:

```
git clone https://github.com/your_username/todo_app.git
```

2. Navigate to the downloaded application directory:

```
cd todo_app
```

3. Create a .env file based on the .env.example and configure it by specifying the necessary environment variables.

4. Launch the application using Docker Compose:

```
docker-compose up --build
```

5. Open your browser and go to http://localhost:5000 to start using the ToDo application.

## Usage

After launching the application, you'll see a simple and intuitive interface. To add a new task, click on the "Add Task" button and enter its description. You can also mark tasks as complete, edit, and delete them.

## Technologies

The ToDo application is built using the following technologies:

- Flask - a microframework for web applications in Python.
- MySQL - a relational database for storing tasks and their properties.
- Docker - a platform for developing, shipping, and running applications in containers.
- HTML/CSS - for creating the user interface.

## Author

The ToDo application was developed by [Your Name or Username](link to GitHub profile or other platform).

## License

This project is licensed under the [MIT License](LICENSE).
```

