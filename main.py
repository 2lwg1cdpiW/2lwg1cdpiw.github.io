from flask import Flask, request, render_template, Response

app = Flask(__name__)

# This dictionary will store your scripts
pastes = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/make', methods=['POST'])
def create_paste():
    # Get the script content from the form
    script_name = request.form['name']
    script_content = request.form['content']

    # Store it in the 'pastes' dictionary
    pastes[script_name] = script_content

    return f'Script "{script_name}" saved successfully!'

@app.route('/raw/<script_name>')
def view_raw(script_name):
    if script_name in pastes:
        # Return raw script content as plain text
        return Response(pastes[script_name], mimetype='text/plain')
    else:
        return "Script not found!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)