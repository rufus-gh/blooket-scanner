import requests, random, webbrowser

# Don't forget to check readme on how to find your bsid
headers = {
    'Cookie': 'bsid=YOUR-BSID-HERE'
}

while True:
    try:
        url = 'https://fb.blooket.com/c/firebase/id?id=' + str(random.randint(1000000, 9999999))
        response = requests.get(url, headers=headers)
        print(response.json()['success'])
        if response.json()['success']:
            print(url)
            webbrowser.open('https://play.blooket.com/play?id='+url.replace('https://fb.blooket.com/c/firebase/id?id=',''))
            exit()
    except requests.RequestException as e:
        print(f"Error: {e}")
