import urllib.request
import json
limit = 100
raw = None
while not raw:
    results = []
    raw = urllib.request.urlopen("https://scrape.pastebin.com/api_scraping.php?limit=" + str(limit))
    json_raw = json.load(raw)

    for paste in json_raw:
        results.append(paste['key'])
    # print list of paste ids
    print(results)
