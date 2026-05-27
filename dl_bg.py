import urllib.request

url = 'https://img.freepik.com/premium-vector/website-background-template_18678099.jpg'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as response:
        with open('bg_image.jpg', 'wb') as out_file: 
            out_file.write(response.read())
except Exception as e:
    print("Error:", e)
