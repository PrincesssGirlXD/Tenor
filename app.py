from flask import Flask, request, jsonify
import httpx
import json

app = Flask(__name__)

@api.route('/')
def home():
    return "Hello World!"

@api.route('/search')
def search_gif():
    search_term = request.args.get('q', '')
    
    apikey = "AIzaSyBuGpE8dH_kR5s2yzp3yusdUiOhmaHs8_4"
    lmt = 1
    ckey = "my_test_app"

    url = f"https://tenor.googleapis.com/v2/search?q={search_term}&key={apikey}&client_key={ckey}&limit={lmt}"

    with httpx.Client() as client:
        response = client.get(url)

        if response.status_code == 200:
            data = response.json()
            gif_url = data['results'][0]['media_formats']['tinygif']['url']
            return jsonify({'gif_url': gif_url})
        else:
            return jsonify({'error': 'Failed to fetch the GIF URL.'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
