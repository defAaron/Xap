from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import requests
from datetime import datetime, timedelta
import os

app = Flask(__name__, static_folder='frontend/build', static_url_path='')
CORS(app)  # Enable CORS for development

BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAGmJ4gEAAAAABlAlwpmk2tRRRl7ZHbX6O5FW43w%3DiS9jAF8DccO5UhpHTiqR02WUgV5pqAbld9zgvWPzTAmNInTjnY"

@app.route("/api/search", methods=["POST"])
def search_tweet():
    try:
        # Step 1: Get the handle and date
        handle = request.form.get("handle", "").lstrip("@").strip()  # Remove leading @
        date_str = request.form.get("date", "").strip()

        if not handle or not date_str:
            return jsonify({"error": "Handle and date are required"}), 400

        # Step 2: Look up user ID
        user_id_url = f"https://api.twitter.com/2/users/by/username/{handle}"
        headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

        try:
            user_response = requests.get(user_id_url, headers=headers, timeout=10)
        except requests.exceptions.RequestException as e:
            return jsonify({"error": f"Could not connect to Twitter API. ({e})"}), 500

        if user_response.status_code != 200:
            error_message = f"Twitter API returned status {user_response.status_code}"
            try:
                error_data = user_response.json()
                if "errors" in error_data:
                    error_message += f" - {error_data['errors'][0].get('detail', 'Unknown error')}"
            except Exception:
                pass
            return jsonify({"error": error_message}), user_response.status_code

        user_data = user_response.json()
        if "data" not in user_data:
            return jsonify({"error": "User not found. Please check the handle."}), 404

        user_id = user_data["data"]["id"]

        # Step 3: Parse date safely
        try:
            start_time = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        end_time = start_time + timedelta(days=1)

        # Step 4: Request tweets
        tweets_url = f"https://api.twitter.com/2/users/{user_id}/tweets"
        params = {
            "start_time": start_time.isoformat("T") + "Z",
            "end_time": end_time.isoformat("T") + "Z",
            "max_results": 10,  # Can go up to 100
            "tweet.fields": "created_at,text",
        }

        try:
            tweets_response = requests.get(
                tweets_url, headers=headers, params=params, timeout=10
            )
        except requests.exceptions.RequestException as e:
            return jsonify({"error": f"Could not connect to Twitter API. ({e})"}), 500

        if tweets_response.status_code != 200:
            error_message = f"Twitter API returned status {tweets_response.status_code}"
            try:
                error_data = tweets_response.json()
                if "errors" in error_data:
                    error_message += f" - {error_data['errors'][0].get('detail', 'Unknown error')}"
            except Exception:
                pass
            return jsonify({"error": error_message}), tweets_response.status_code

        tweets_data = tweets_response.json()
        if "data" in tweets_data and len(tweets_data["data"]) > 0:
            # Show the first tweet
            tweet_text = tweets_data["data"][0]["text"]
        else:
            tweet_text = "No tweets found on that date."

        return jsonify({"tweet": tweet_text}), 200

    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route("/")
def serve():
    """Serve the React app in production"""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files from React build"""
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run(debug=True)