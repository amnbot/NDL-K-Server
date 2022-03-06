import json
from mvs_get import get_bg_mvs, get_gg_mvs

def update_bg_mvs_json():
    bg_mvs = get_bg_mvs()
    with open('data/mvs/bg_mvs.json', 'w') as rs:
        json.dump(bg_mvs, rs)

def update_gg_mvs_json():
    gg_mvs = get_gg_mvs()
    with open('data/mvs/gg_mvs.json', 'w') as rs:
        json.dump(gg_mvs, rs)

def update_all_gender_mvs():

    # Update bg mvs
    update_bg_mvs_json()

    # Update gg mvs
    update_gg_mvs_json()