from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS untuk bisa diakses dari frontend

# Database sementara (nanti upgrade ke SQLite)
todos = []
next_id = 1


# ========== HOMEPAGE ==========
@app.route('/')
def home():
    """API Documentation Homepage"""
    return jsonify({
        'message': '🚀 TODO API by Haidar',
        'version': '1.0.0',
        'endpoints': {
            'GET /todos': 'Get all todos',
            'GET /todos/<id>': 'Get single todo',
            'POST /todos': 'Create new todo',
            'PUT /todos/<id>': 'Update todo',
            'DELETE /todos/<id>': 'Delete todo'
        },
        'github': 'https://github.com/yapi-unesa/todo-api'
    })


# ========== GET ALL TODOS ==========
@app.route('/todos', methods=['GET'])
def get_todos():
    """Ambil semua todo items"""
    return jsonify({
        'success': True,
        'count': len(todos),
        'data': todos
    }), 200


# ========== GET SINGLE TODO ==========
@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    """Ambil satu todo berdasarkan ID"""
    todo = next((t for t in todos if t['id'] == todo_id), None)
    
    if not todo:
        return jsonify({
            'success': False,
            'error': 'Todo not found'
        }), 404
    
    return jsonify({
        'success': True,
        'data': todo
    }), 200


# ========== CREATE TODO ==========
@app.route('/todos', methods=['POST'])
def create_todo():
    """Bikin todo baru"""
    global next_id
    
    data = request.get_json()
    
    # Validasi input
    if not data or 'title' not in data:
        return jsonify({
            'success': False,
            'error': 'Title is required'
        }), 400
    
    if len(data['title'].strip()) == 0:
        return jsonify({
            'success': False,
            'error': 'Title cannot be empty'
        }), 400
    
    # Bikin todo object baru
    new_todo = {
        'id': next_id,
        'title': data['title'],
        'description': data.get('description', ''),
        'completed': False,
        'created_at': datetime.now().isoformat(),
        'updated_at': None
    }
    
    todos.append(new_todo)
    next_id += 1
    
    return jsonify({
        'success': True,
        'message': 'Todo created successfully',
        'data': new_todo
    }), 201


# ========== UPDATE TODO ==========
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update todo yang sudah ada"""
    todo = next((t for t in todos if t['id'] == todo_id), None)
    
    if not todo:
        return jsonify({
            'success': False,
            'error': 'Todo not found'
        }), 404
    
    data = request.get_json()
    
    # Update fields yang dikirim
    if 'title' in data:
        todo['title'] = data['title']
    if 'description' in data:
        todo['description'] = data['description']
    if 'completed' in data:
        todo['completed'] = data['completed']
    
    # Update timestamp
    todo['updated_at'] = datetime.now().isoformat()
    
    return jsonify({
        'success': True,
        'message': 'Todo updated successfully',
        'data': todo
    }), 200


# ========== DELETE TODO ==========
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Hapus todo"""
    global todos
    
    todo = next((t for t in todos if t['id'] == todo_id), None)
    
    if not todo:
        return jsonify({
            'success': False,
            'error': 'Todo not found'
        }), 404
    
    todos = [t for t in todos if t['id'] != todo_id]
    
    return jsonify({
        'success': True,
        'message': f'Todo "{todo["title"]}" deleted successfully'
    }), 200


# ========== MARK ALL AS COMPLETED ==========
@app.route('/todos/complete-all', methods=['PUT'])
def complete_all():
    """Mark semua todos sebagai completed"""
    if not todos:
        return jsonify({
            'success': False,
            'error': 'No todos found'
        }), 404
    
    for todo in todos:
        todo['completed'] = True
        todo['updated_at'] = datetime.now().isoformat()
    
    return jsonify({
        'success': True,
        'message': f'{len(todos)} todos marked as completed',
        'data': todos
    }), 200


# ========== RUN SERVER ==========
if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 TODO API Server Starting...")
    print("="*50)
    print(f"📍 Local:   http://127.0.0.1:5000")
    print(f"📖 Docs:    http://127.0.0.1:5000")
    print("="*50 + "\n")
    
    app.run(debug=True, port=5000)
# ```

# **Copy semua**, paste ke `app.py`, **Save**.

# ---

# ## ✅ **Verifikasi File Sudah Benar**

# Di VS Code, struktur folder kamu sekarang:
# ```
# todo-api/
# ├── venv/              (folder biru - jangan dibuka)
# ├── .gitignore         (file - ada titik di depan!)
# ├── app.py             (file - icon Python)
# ├── README.md          (file - icon Markdown)