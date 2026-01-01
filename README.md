# XAP - Twitter Tweet Finder

A web application that allows you to search for tweets from a specific Twitter/X user on a given date. Built with React frontend and Flask backend.

## Features

- 🔍 Search for tweets by Twitter handle and date
- 📅 Find the first tweet posted by a user on a specific date
- 🎨 Clean and intuitive user interface
- ⚡ Fast and responsive search experience
- 🛡️ Error handling for invalid inputs and API errors

## Tech Stack

### Frontend
- **React** 18.2.0
- **React Scripts** 5.0.1
- Modern CSS for styling

### Backend
- **Flask** - Python web framework
- **Flask-CORS** - Cross-origin resource sharing
- **Requests** - HTTP library for Twitter API calls

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python** 3.7 or higher
- **Node.js** 18 or higher (and npm)
- **Twitter API Bearer Token** - You'll need a Twitter API v2 bearer token to use this application

## Installation

### 1. Clone the repository

```bash
git clone <repository-url>
cd xap
```

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
```

### 3. Frontend Setup

```bash
cd frontend
npm install
```

## Configuration

### Twitter API Token

1. Obtain a Twitter API Bearer Token from the [Twitter Developer Portal](https://developer.twitter.com/)

2. Update the `BEARER_TOKEN` in `backend/app.py`:

```python
BEARER_TOKEN = "your_bearer_token_here"
```

**Note:** For production, consider using environment variables instead of hardcoding the token:

```python
import os
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN", "undefined")
```

Then set the environment variable:
```bash
export TWITTER_BEARER_TOKEN="your_bearer_token_here"
```

## Running the Application

### Development Mode

#### Start the Backend Server

```bash
cd backend
python app.py
```

The backend server will run on `http://localhost:5000` (or the port Flask assigns).

#### Start the Frontend Development Server

In a new terminal:

```bash
cd frontend
npm start
```

The frontend will run on `http://localhost:3000` and automatically proxy API requests to the backend.

### Production Mode

#### Build the Frontend

```bash
cd frontend
npm run build
```

This creates a `build` folder with the production-ready React app.

#### Run the Backend (serves frontend)

The Flask app is configured to serve the React build files. Make sure the `frontend/build` directory exists, then:

```bash
cd backend
python app.py
```

The application will be available at `http://localhost:5000`.

## Project Structure

```
xap/
├── backend/
│   ├── app.py              # Flask backend server
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── public/
│   │   └── index.html      # HTML template
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── App.css         # App styles
│   │   ├── index.js        # React entry point
│   │   ├── index.css       # Global styles
│   │   └── components/
│   │       ├── SearchForm.js      # Search form component
│   │       ├── SearchForm.css     # Form styles
│   │       ├── ResultDisplay.js   # Results display component
│   │       └── ResultDisplay.css  # Results styles
│   ├── Dockerfile          # Docker configuration for frontend
│   └── package.json        # Node.js dependencies
└── README.md
```

## API Endpoints

### POST `/api/search`

Search for a tweet by Twitter handle and date.

**Request:**
- Content-Type: `multipart/form-data` or `application/x-www-form-urlencoded`
- Parameters:
  - `handle` (string, required): Twitter username (with or without @)
  - `date` (string, required): Date in YYYY-MM-DD format

**Response:**
```json
{
  "tweet": "Tweet text here..."
}
```

**Error Response:**
```json
{
  "error": "Error message here"
}
```

**Status Codes:**
- `200` - Success
- `400` - Bad request (missing or invalid parameters)
- `404` - User not found
- `500` - Server error

## Usage

1. Open the application in your browser
2. Enter a Twitter handle (e.g., `elonmusk` or `@elonmusk`)
3. Select a date using the date picker
4. Click "Search"
5. The first tweet from that user on that date will be displayed

## Docker Support

The frontend includes a Dockerfile for containerized deployment:

```bash
cd frontend
docker build -t xap-frontend .
docker run -p 3000:3000 xap-frontend
```

## Notes

- The application searches for tweets within a 24-hour window starting from the selected date
- Only the first tweet found on that date is returned (up to 10 tweets are fetched from the API)
- The Twitter API has rate limits - be mindful of usage
- Make sure your Twitter API token has the necessary permissions to read tweets

## License

[Add your license here]

## Contributing

[Add contributing guidelines here]
