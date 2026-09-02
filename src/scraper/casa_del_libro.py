import requests

def get_url(url: str):

    headers = {
        "User_Agent": "Mozila/5.0"
    }

    session = requests.Session()

    response = session.get(url=url)
    # , headers=headers

    print(response.status_code)
    print(response.text)