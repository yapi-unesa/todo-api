# TODO API

Simple REST API untuk manage TODO list, built with Flask.

## 👨‍💻 Author

**Haidar** - Mahasiswa Informatika Semester 4

## ✨ Features

- ✅ Create TODO
- ✅ Read all TODOs
- ✅ Read single TODO
- ✅ Update TODO
- ✅ Delete TODO
- ✅ Timestamps (created_at, updated_at)

## 🛠️ Tech Stack

- Python 3.x
- Flask (Web Framework)
- Flask-CORS (Handle CORS)

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/yapi-unesa/todo-api.git
cd todo-api

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
python app.py
```

## 🚀 API Endpoints

### Base URL

```
http://127.0.0.1:5000
```

### 1. Get All TODOs

```http
GET /todos
```

**Response:**

```json
{
  "success": true,
  "count": 2,
  "data": [...]
}
```

### 2. Get Single TODO

```http
GET /todos/:id
```

### 3. Create TODO

```http
POST /todos
Content-Type: application/json

{
  "title": "Belajar Flask",
  "description": "Tutorial TODO API"
}
```

### 4. Update TODO

```http
PUT /todos/:id
Content-Type: application/json

{
  "title": "Updated title",
  "completed": true
}
```

### 5. Delete TODO

```http
DELETE /todos/:id
```

## 📚 Learning Journey

Project ini dibuat sebagai bagian dari persiapan magang semester 6.

### What I Learned:

- REST API concepts
- HTTP methods (GET, POST, PUT, DELETE)
- Flask framework basics
- Git & GitHub workflow
- API documentation

## 📄 License

MIT License - Feel free to use this project for learning!

---

⭐ **Star this repo if you found it helpful!**
