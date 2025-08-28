# Personal To-Do List Application

## 📌 Problem Statement
People often struggle to keep track of their daily tasks. This application helps users organize tasks, mark them as completed, and manage their work effectively — all from a simple command-line interface.

---

## 🚀 Features
- Add tasks with **title, description, and category** (Work, Personal, Urgent).
- View all tasks with **status** (Pending / Completed).
- Mark tasks as completed.
- Delete tasks.
- Search tasks by category.
- Filter tasks by status (Pending / Completed).
- Data persistence using **JSON file** (tasks are saved automatically).

---

## ⚙️ How to Run
1. Clone or download the project.
2. Open a terminal inside the project folder.
3. Run the app:
   ```bash
   python todo.py
   ```
4. A `tasks.json` file will be created automatically to store tasks.

---

## 📂 Project Structure
```
todo_app/
├── todo.py       # Main Python script
├── tasks.json    # Stores tasks (auto-created)
└── README.md     # Documentation
```

---

## 🖼️ Screenshots (Optional if GUI used)
*CLI version sample output:*
```
===== Personal To-Do List =====
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Search by Category
6. Filter by Status
7. Exit
Choose an option:
```

---

## 🧩 Code Overview
- `Task` class → Represents a task with attributes.
- `save_tasks()` & `load_tasks()` → Handles file persistence (JSON).
- Menu options → For user interaction (add, view, mark, delete).
- `search_by_category()` & `filter_by_status()` → Advanced filtering.

---

## 🔮 Future Improvements
- Add **due dates** & **priority levels**.
- Add **sorting (Urgent first)**.
- Add **Tkinter GUI** for better user experience.
- Add **reminder notifications**.

---

👨‍💻 Developed as a beginner-friendly Python project.

