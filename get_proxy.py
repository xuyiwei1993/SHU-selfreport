import requests
from bs4 import BeautifulSoup


def verify_proxy(ip, port):
    try:
        requests.get('https://selfreport.shu.edu.cn/Default.aspx', proxies={
            'http': f'http://{ip}:{port}',
            'https': f'http://{ip}:{port}'
        }, timeout=3)
    except Exception as e:
        return False

    return True


if __name__ == '__main__':
    r = requests.get('https://free-proxy-list.net/')

    soup = BeautifulSoup(r.text, 'html.parser')

    for tr in soup.select('table tbody tr'):
        ip = tr.select('td')[0].text.strip()
        port = tr.select('td')[1].text.strip()

        if verify_proxy(ip, port):
            print(ip, port)
