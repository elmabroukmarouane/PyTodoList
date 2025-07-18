# 📝 Django To-Do List App

A simple, elegant, and fully featured **ToDo List** web app built with **Django** and **SQLite**.

This project is designed as a single-page app with Bootstrap 5 styling and minimal JavaScript for smooth user experience — no external JS frameworks required!

---

## Features

### Task Management
- **Add tasks** with title, due date, and priority (High, Medium, Low)  
- **Edit task titles inline**  
- **Mark tasks as completed** by clicking checkbox or anywhere on the task line  
- **Delete tasks** with confirmation prompt  
- **Auto-sort tasks**: incomplete first, then by due date and priority  
- **Task metadata:** creation and last update timestamps  

### UI / UX
- Responsive design using **Bootstrap 5**  
- **Light/Dark mode toggle** with persistent user preference  
- Task highlighting and styling based on completion and priority  
- Icons from **Bootstrap Icons** for visual cues  

### Export
- Export all tasks to a **CSV file** including all fields (title, completed, due date, priority, created/updated timestamps)  

---

## Installation & Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/django-todo-app.git
    cd django-todo-app
    ```

2. Create and activate a virtual environment (recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # macOS/Linux
    venv\Scripts\activate     # Windows
    ```

3. Install dependencies:
    ```bash
    pip install django
    ```

4. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Usage

- Use the form at the top to add new tasks with optional due date and priority  
- Click the checkbox or anywhere on a task line to toggle completion  
- Click the task title to edit it inline (press Enter or click outside to save)  
- Click the trash icon to delete a task (confirmation required)  
- Use the **Theme** button to toggle light/dark mode; your choice is saved  
- Export all tasks to CSV with the **Export CSV** button  

---

## Project Structure

```
todo/
├── migrations/
├── templates/
│   └── todo/
│       └── index.html
├── static/
│   └── css/
│       └── styles.css  # custom styles including dark mode & completed tasks
├── __init__.py
├── admin.py
├── apps.py
├── models.py          # Task model with title, completed, due_date, priority, timestamps
├── tests.py
├── urls.py            # URL patterns including add, toggle, delete, export
├── views.py           # Views with AJAX support and export to CSV
manage.py
README.md
```

---

## Models

### Task

| Field       | Type          | Description                          |
|-------------|---------------|------------------------------------|
| `title`     | CharField     | Task title                         |
| `completed` | BooleanField  | Completion status                  |
| `due_date`  | DateField     | Optional due date                  |
| `priority`  | IntegerField  | Task priority (1=High, 2=Med, 3=Low) |
| `created_at`| DateTimeField | Timestamp when task was created    |
| `updated_at`| DateTimeField | Timestamp when task was last updated |

---

## Dependencies

- Python 3.8+  
- Django 4.x  
- Bootstrap 5 (via CDN)  
- Bootstrap Icons (via CDN)  

---

## Future Improvements

- User authentication & personalized task lists  
- Task reminders/notifications  
- Task categories or tags  
- Drag-and-drop task ordering  
- API endpoints for mobile or SPA frontend  

---

## License

MIT License © 2025 - MEL

