from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://dbkpop.com/'

BOY_GROUPS_URL = 'db/k-pop-boybands'
GIRL_GROUPS_URL = 'db/k-pop-girlgroups'

ALL_GROUPS_YTB = 'https://kpop.daisuki.com.br/artists.html'

def get_all_groups():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'
    }
    m_html_text = requests.get(ALL_GROUPS_YTB, headers=headers).text
    # print(m_html_text)
    soup = BeautifulSoup(m_html_text, 'lxml')

    table = soup.find('table', id='outputtable')

    # print(table)

    all_groups = {}

    groups = table.findAll('tr', {"class" : "dashbottom"})

    properties = ['Artist', 'Views', 'Likes', 'Recent View/Day', 'Debut', 'View/MV', 'Like/MV', 'Sales', 'Followers']

    for k, group in enumerate(groups):
        infos = group.findAll('td')
        all_groups[k] = {}
        for i, info in enumerate(infos):
            if i < len(properties):
                toadd = info.text
                if i == 0:
                    toadd = toadd.replace('\t', '')
                    toadd = toadd.replace('\n', '')
                    idx = toadd.find('(')
                    toadd = toadd[0:idx]
                all_groups[k][properties[i]] = toadd
            else:
                break

    return all_groups

def get_boy_groups():
    bg_html_text = requests.get(BASE_URL + BOY_GROUPS_URL).text
    soup = BeautifulSoup(bg_html_text, 'lxml')

    table = soup.find('table', id="table_1")

    bgs_data = {}

    bgs = table.tbody.findAll('tr')

    properties = ["Profile", "Name", "Short Name", "Korean Name", "Debut",
                  "Company", "Current Member Count",
                  "Original Member Count", "FanClub", "Active"]

    for k, bg in enumerate(bgs):
        infos = bg.findAll('td')
        bgs_data[k] = {}
        for i, info in enumerate(infos):
            if i == 0 and info.text != '':
                bgs_data[k][properties[i]] = info.a['href']
            elif i < len(properties):
                bgs_data[k][properties[i]] = info.text
            else:
                break

    all_bgs = {}
    k = 0
    for i, bg in enumerate(bgs_data):
        if bgs_data[bg]['Active'] == 'Yes':
            all_bgs[k] = {}
            all_bgs[k] = bgs_data[bg]
            k += 1


    return all_bgs

def get_girl_groups():
    gg_html_text = requests.get(BASE_URL + GIRL_GROUPS_URL).text
    soup = BeautifulSoup(gg_html_text, 'lxml')

    table = soup.find('table', id="table_1")

    ggs_data = {}

    ggs = table.tbody.findAll('tr')

    properties = ["Profile", "Name", "Short Name", "Korean Name", "Debut",
                  "Company", "Current Member Count",
                  "Original Member Count", "FanClub", "Active"]

    for k, gg in enumerate(ggs):
        infos = gg.findAll('td')
        ggs_data[k] = {}
        for i, info in enumerate(infos):
            if i == 0 and info.text != '':
                ggs_data[k][properties[i]] = info.a['href']
            elif i < len(properties):
                ggs_data[k][properties[i]] = info.text
            else:
                break

    return ggs_data