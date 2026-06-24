from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>MEDFLIQ</h1>
    <h2>Contact : 9876543210</h2>
    <h3>Services</h3>
    <ul>
        <li>AI Solutions</li>
        <li>Cloud Services</li>
        <li>Healthcare Analytics</li>
    </ul>
    '''

app.run(host='0.0.0.0', port=5000)