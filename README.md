
# Offline Smart Scheduler

## Track F — Open / Wildcard

Our project belongs to **Track F — Open / Wildcard** because it is an
**offline scheduler**. Schedulers are specifically mentioned as an
eligible project type in this track.

## About the Project

Offline Smart Scheduler is a simple Python program for creating and
managing tasks.

Users can:

- Add tasks
- View tasks
- Complete tasks
- Delete tasks
- Change task priority
- Search for tasks
- Filter tasks
- View task statistics
- Save tasks locally

The project works completely offline.

## Features

- Task creation and management
- Due date and time
- Priority levels from 1 to 5
- Pending and completed task status
- Search by task name
- Filter by priority and status
- Basic task statistics
- Local task storage
- Simple terminal interface
- No external packages

## Zero Dependencies

This project uses **no third-party Python packages**.

The project is made using basic Python functionality. This allows the
scheduler to run without installing additional packages or connecting
to an online service.

We did not use:

- Third-party Python packages
- External APIs
- Online databases
- Cloud services
- Internet connection

## Alternatives to External Libraries

Instead of using external libraries for common features, we created
our own simple implementations using Python's built-in features.

| Common Library or Tool | Our Alternative |
|---|---|
| APScheduler / schedule | Our own task scheduling and task management logic |
| pandas | Python lists and dictionaries |
| SQL database | Local text-file storage |
| Search libraries | Python string operations and list processing |
| GUI frameworks | Simple terminal-based interface |
| Online task management services | Local offline task storage |

This approach keeps the project lightweight and satisfies the
zero-dependency requirement.

## How We Implemented the Features

### Task Management

Tasks are stored as Python dictionaries inside a list.

Each task contains:

- ID
- Name
- Date
- Time
- Priority
- Status

### Local Storage

Instead of using a database or online storage service, tasks are saved
in a local text file.

Each task is stored as a line in the file, making the data easy to save
and load without an external database.

### Search

Instead of using a search library, we use Python string operations to
search task names.

The search supports case-insensitive and partial matching.

### Filtering

Tasks can be filtered using their:

- Priority
- Status
- Priority and status together

### Statistics

The program can display basic statistics about the current tasks.

### Interface

The application uses a simple terminal interface instead of an
external GUI framework.

## Project Structure

```text
offline-scheduler/
│
├── main.py
├── interface.py
├── tasks.py
├── storage.py
├── search.py
├── README.md
└── LICENSE

