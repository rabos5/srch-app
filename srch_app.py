from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from urllib.parse import unquote

# todo: remove
import time


app = FastAPI()

app.mount('/assets', StaticFiles(directory='assets'), name='assets')
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/', response_class=HTMLResponse)
async def search():
    with open('static/search.html', 'r') as file:
        html = file.read()
    return html


@app.get('/results', response_class=HTMLResponse)
async def results():
    with open('static/results.html', 'r') as file:
        html = file.read()
    return html


# TODO: add redis cache, asyncio to other backends, update structure of data returned, add env variables, etc...
@app.get('/api/search')
async def api_search(q: str):
    query = unquote(q)

    results = {
        'query': query,
        'results': {
            'google': [
                {
                    'url': 'https://google.com',
                    'title': 'Google',
                    'description': 'This is a description of a search result from Google.',
                    'date': 'March 30, 2023',
                    'author': 'Ryan Bostian'
                },
                {
                    'url': 'https://google.com',
                    'title': 'Google',
                    'description': 'This is a description of a search result from Google.',
                    'date': 'March 30, 2023',
                    'author': 'Ryan Bostian'
                },
                {
                    'url': 'https://google.com',
                    'title': 'Google',
                    'description': 'This is a description of a search result from Google.',
                    'date': 'March 30, 2023',
                    'author': 'Ryan Bostian'
                },
                {
                    'url': 'https://google.com',
                    'title': 'Google',
                    'description': 'This is a description of a search result from Google.',
                    'date': 'March 30, 2023',
                    'author': 'Ryan Bostian'
                },
                {
                    'url': 'https://google.com',
                    'title': 'Google',
                    'description': 'This is a description of a search result from Google.',
                    'date': 'March 30, 2023',
                    'author': 'Ryan Bostian'
                }
            ],
            'other': [
                {
                    'url': 'https://other.com',
                    'title': 'Other',
                    'description': 'This is a description of a search result from Other.',
                    'date': 'March 30, 2023',
                    'author': 'Ryan Bostian'
                },
                {
                    'url': 'https://other.com',
                    'title': 'Other',
                    'description': 'This is a description of a search result from Other.',
                    'date': 'March 30, 2023',
                    'author': 'Ryan Bostian'
                },
                {
                    'url': 'https://other.com',
                    'title': 'Other',
                    'description': 'This is a description of a search result from Other.',
                    'date': 'March 30, 2023',
                    'author': 'Ryan Bostian'
                },
                {
                    'url': 'https://other.com',
                    'title': 'Other',
                    'description': 'This is a description of a search result from Other.',
                    'date': 'March 30, 2023',
                    'author': 'Ryan Bostian'
                },
                {
                    'url': 'https://other.com',
                    'title': 'Other',
                    'description': 'This is a description of a search result from Other.',
                    'date': 'March 30, 2023',
                    'author': 'Ryan Bostian'
                }
            ]
        }
    }

    return results


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8000
    )
