import httpx
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/gif")
async def search_gif(request: Request, q: str = None):
    alpha = request.query_params.get('q', '')
    
    apikey = "AIzaSyBuGpE8dH_kR5s2yzp3yusdUiOhmaHs8_4"
    lmt = 1
    ckey = "vercel_app"

    url = f"https://tenor.googleapis.com/v2/search?q={alpha}&key={apikey}&client_key={ckey}&limit={lmt}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            data = response.json()
            gif_url = data['results'][0]['media_formats']['tinygif']['url']
            return {'gif_url': gif_url}
        else:
            return {'error': 'Failed to fetch the GIF URL.'}, response.status_codeqq