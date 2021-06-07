import re
import requests
import time



def parseCookieFile_philip(cookiefile):
    """Parse a cookies.txt file and return a dictionary of key value pairs
    compatible with requests."""

    cookies = {}
    with open (cookiefile, 'r') as fp:
        for line in fp:
            if not re.match(r'^\#', line):
                lineFields = line.strip().split('\t')
                if "/" in lineFields:
                    cookies[lineFields[5]] = lineFields[6]

    return cookies


def http_request_philippinetimes():    
    cookies = parseCookieFile_philip('philippinetimes.com_cookies.txt')

    #proxies = {
    #"http": "210.8.81.246:8080", 
    #"https": "210.8.81.246:8080"
    #}

    headers = {
        'authority': 'www.philippinetimes.com',
        'cache-control': 'max-age=0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'hbcm_sd=1%7C1623036337192; session_depth=www.philippinetimes.com%3D1%7C344129722%3D1%7C146425595%3D1%7C820268263%3D1; bfp_sn_rf_8b2087b102c9e3e5ffed1c1478ed8b78=Direct; bfp_sn_rt_8b2087b102c9e3e5ffed1c1478ed8b78=1623036337547; bfp_sn_pl=1623036337|1_367813321332; _ga=GA1.2.1750680829.1623036338; _gid=GA1.2.231110052.1623036338; fpestid=gtObKWLduALJMzUZ5umZH0DEZUcRMpH5ehkTHB-nZzzXWudIGipVcyx7oOCKGB-28dKWqQ; bafp=07e53bb0-c740-11eb-969a-6fdc764a85d5',
    }

    url = 'https://www.philippinetimes.com/news/269793821/stricter-border-control-in-guimaras-starts-june-7'

    try:
        r = requests.get(url, headers=headers, cookies=cookies)
        print(r)

        html = r.content
        #result = html.encode('utf-8')
        result = html.decode('utf-8')
        response = result

        with open('hasil.txt', 'w') as f:
            f.write(response)

    except Exception as e:
        raise Exception('An error occurred in {}'.format(str(e)))


if __name__ == '__main__':
    http_request_philippinetimes()