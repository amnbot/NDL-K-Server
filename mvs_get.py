from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://dbkpop.com/'


BG_MVS_URL = 'db/k-pop-boyband-mvs'
GG_MVS_URL = 'db/k-pop-girlgroup-mvs'

ALL_MVS_YTB = 'https://kpop.daisuki.com.br/mvs.html?options=100&tags=dorvpnezjs&cols=100000000&ord=7A&lmode=2'


def get_all_mvs():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
    }
    m_html_text = requests.get(ALL_MVS_YTB, headers=headers).text
    # print(m_html_text)
    soup = BeautifulSoup(m_html_text, 'lxml')

    table = soup.find('div', id='list_results')
    mvs = table.findAll('div', {'class': 'list_tiles_item'})

    all_mvs = {}

    properties = ['Artist', 'Views', 'Likes', 'View/Like', 'Recent View/day', 'Recent Like/day', 'Average View/day', 'Age']

    for k, mv in enumerate(mvs):
        infos = mv.findAll('div')
        all_mvs[k] = {}
        for i, info in enumerate(infos):
            if i < len(properties):
                toadd = info.text
                all_mvs[k][properties[i]] = toadd
            else:
                break

    print(all_mvs)

    return all_mvs

def get_bg_mvs():
    bg_mvs_html_text = requests.get(BASE_URL + BG_MVS_URL).text
    soup = BeautifulSoup(bg_mvs_html_text, 'lxml')

    table = soup.find('table', id="table_1")

    bg_mvs_data = {}

    bg_mvs = table.tbody.find_all('tr')

    properties = ["Post", "Release Date", "Artist", "Song Name",
                  "Korean Name", "Director", "Video", "Type", "Release Type"]

    for k, mv in enumerate(bg_mvs):
        infos = mv.findAll('td')
        bg_mvs_data[k] = {}
        for i, info in enumerate(infos):
            if i == 6:
                bg_mvs_data[k][properties[i]] = info.a['href']
            elif i < len(properties):
                bg_mvs_data[k][properties[i]] = info.text
            else:
                break

    return bg_mvs_data


def get_gg_mvs():
    gg_mvs_html_text = requests.get(BASE_URL + GG_MVS_URL).text
    soup = BeautifulSoup(gg_mvs_html_text, 'lxml')

    table = soup.find('table', id="table_1")

    gg_mvs_data = {}

    gg_mvs = table.tbody.find_all('tr')

    properties = ["Post", "Release Date", "Artist", "Song Name",
                  "Korean Name", "Director", "Video", "Type", "Release Type"]

    for k, mv in enumerate(gg_mvs):
        infos = mv.findAll('td')
        gg_mvs_data[k] = {}
        for i, info in enumerate(infos):
            if i == 6:
                gg_mvs_data[k][properties[i]] = info.a['href']
            elif i < len(properties):
                gg_mvs_data[k][properties[i]] = info.text
            else:
                break

    return gg_mvs_data
