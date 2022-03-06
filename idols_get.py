from bs4 import BeautifulSoup
import requests

BASE_URL = 'https://dbkpop.com/'

MALE_IDOLS_GROUPS_URL = 'db/male-k-pop-idols'
FEMALE_IDOLS_GROUPS_URL = 'db/female-k-pop-idols'

def get_male_idols():
    m_html_text = requests.get(BASE_URL + MALE_IDOLS_GROUPS_URL).text
    soup = BeautifulSoup(m_html_text, 'lxml')

    table = soup.find('table', id="table_1")

    male_idols = {}

    idols = table.tbody.findAll('tr')

    properties = ["", "Stage Name", "Full Name", "Korean Full Name",
                  "Korean Stage Name", "Date Of Birth", "Group",
                  "Country", "", "Height", "Weight", "Birthplace"]

    for k, idol in enumerate(idols):
        infos = idol.findAll('td')
        male_idols[k] = {}
        for i, info in enumerate(infos):
            if i < len(properties):
                male_idols[k][properties[i]] = info.text
            else:
                break

    return male_idols


def get_female_idols():
    f_html_text = requests.get(BASE_URL + FEMALE_IDOLS_GROUPS_URL).text
    soup = BeautifulSoup(f_html_text, 'lxml')

    table = soup.find('table', id="table_1")

    female_idols = {}

    idols = table.tbody.findAll('tr')

    properties = ["", "Stage Name", "Full Name", "Korean Full Name",
                  "Korean Stage Name", "Date Of Birth", "Group",
                  "Country", "", "Height", "Weight", "Birthplace"]

    for k, idol in enumerate(idols):
        infos = idol.findAll('td')
        female_idols[k] = {}
        for i, info in enumerate(infos):
            if i < len(properties):
                female_idols[k][properties[i]] = info.text
            else:
                break

    return female_idols