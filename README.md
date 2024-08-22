
# Finance Tech Website

## Project Description

This project demonstrates a full-stack application that integrates a React.js frontend with a Flask backend and Firebase for authenticated data storage functionality. The frontend, developed using React.js, communicates with the backend Flask server through RESTful API endpoints. 

The backend, built with Flask, provides a simple API that serves data to the React frontend. This setup showcases how to handle API requests, enable Cross-Origin Resource Sharing (CORS), and interact with a backend server from a React application.

### Key Features

- **React Frontend**: Fetches and displays data from the Flask API.
- **Flask Backend**: Provides an API endpoint to return JSON data.
- **CORS Support**: Allows cross-origin requests between the frontend and backend.
- **Deployment Ready**: Instructions for deploying both the frontend and backend to production environments.

This project serves as a foundational example for building and integrating modern web applications with a clear separation between frontend and backend responsibilities.

# React & Flask Integration

This project demonstrates how to integrate a React.js frontend with a Flask backend. The React frontend communicates with the Flask backend through API endpoints and how the Firebase helps to store and analyse the data.

## Project Structure
-project-root

-client       # React frontend

-server       # Flask backend

## Backend Setup (Flask)

### 1. Prerequisites

- Python 3.x
- Flask
- Flask-CORS

### 2. Installation

1. Create and activate a virtual environment:

```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
```
2. Install required packages
```
pip install flask flask-cors
```
3. Running the backend

- Create a file named app.py in the /server directory with the following content:
```
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/api/data', methods=['GET'])
def get_data():
    # Fetch or process your data
    data = {"message": "Hello from Flask!"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
```
- Start the Flask server:
```
python app.py
```
 The server will run on http://localhost:5000.

## Frontend Setup (React.js)

1. Prerequisites

	•	Node.js

	•	npm or yarn

2. Installation

	1.	Navigate to the /client directory and install dependencies:
```
cd client
npm install   # or yarn install
```

3. Fetch Data from Flask API

	1.	Modify src/App.js to fetch data from the Flask backend:

```
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
    const [data, setData] = useState(null);

    useEffect(() => {
        axios.get('http://localhost:5000/api/data')
            .then(response => setData(response.data))
            .catch(error => console.error('Error:', error));
    }, []);

    return (
        <div>
            <h1>Data from Flask API:</h1>
            {data && <pre>{JSON.stringify(data, null, 2)}</pre>}
        </div>
    );
}

export default App;
```

4. Running the Frontend

	1.	Start the React development server:

    ```
    npm start   # or yarn start
    ```

The frontend will be accessible at http://localhost:3000.

## Deployment

1. Deploy Flask Backend

Deploy your Flask backend to a cloud provider or server of your choice, such as Heroku, AWS, or DigitalOcean.

2. Deploy React Frontend

-	Build your React application:

```
cd client
npm run build   # or yarn build
```

-	Deploy the built files to a static file hosting service like Vercel, Netlify, or to the same server as Flask.

- Update API URLs

Make sure to update the API URLs in your React application to point to the deployed Flask backend.

### Acknowledgements

    •	Flask: Flask Documentation
    •	React: React Documentation
    •	axios: Axios Documentation
