from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"status": "error", "message": "No file uploaded"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"}), 400
    
    # Save the file temporarily
    file_path = f"uploads/{file.filename}"
    file.save(file_path)
    
    # Send the file path to backend for processing
    response = {
        "status": "success",
        "message": "File uploaded successfully",
        "file_path": file_path
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
