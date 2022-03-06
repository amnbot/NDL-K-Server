import json
from groups_get import get_all_groups, get_boy_groups, get_girl_groups

def merge_group_cols_boys():
    allgroups = {}
    with open('data/groups/allgroups.json', 'r') as db:
        allgroups = json.load(db)
    
    boy_groups = {}
    with open('data/groups/boy_groups.json', 'r') as db:
        boy_groups = json.load(db)

    for bg_i in boy_groups:
        for group_i in allgroups:
            if boy_groups[bg_i]['Name'].lower() in allgroups[group_i]['Artist'].lower():
                boy_groups[bg_i]['Views'] = allgroups[group_i]['Views']
                boy_groups[bg_i]['Likes'] = allgroups[group_i]['Likes']

    # print(boy_groups)

    return boy_groups

def merge_group_cols_girls():
    allgroups = {}
    with open('data/groups/allgroups.json', 'r') as db:
        allgroups = json.load(db)

    girl_groups = {}
    with open('data/groups/girl_groups.json', 'r') as db:
        girl_groups = json.load(db)
    
    for gg_i in girl_groups:
        for group_i in allgroups:
            if girl_groups[gg_i]['Name'].lower() in allgroups[group_i]['Artist'].lower():
                girl_groups[gg_i]['Views'] = allgroups[group_i]['Views']
                girl_groups[gg_i]['Likes'] = allgroups[group_i]['Likes']
    
    # print(girl_groups)

    return girl_groups

def update_allgroups_json():
    allgroups = get_all_groups()
    with open('data/groups/allgroups.json', 'w') as rs:
        json.dump(allgroups, rs)

def update_boy_groups_json():
    boy_groups = get_boy_groups()
    with open('data/groups/boy_groups.json', 'w') as rs:
        json.dump(boy_groups, rs)

def update_girl_groups_json():
    girl_groups = get_girl_groups()
    with open('data/groups/girl_groups.json', 'w') as rs:
        json.dump(girl_groups, rs)

def update_all_boy_groups_json_views_likes():
    with open('data/groups/all_boy_groups.json', 'w') as rs:
        json.dump(merge_group_cols_boys(), rs)

def update_all_girl_groups_json_views_likes():
    with open('data/groups/all_girl_groups.json', 'w') as rs:
        json.dump(merge_group_cols_girls(), rs)


def update_all_gender_groups():
    # Update allgroups.json file (with both genders, views, likes, etc.)
    update_allgroups_json()

    # Update boy_groups.json file (with all info about all boy groups w/o views, likes, etc.)
    update_boy_groups_json()
    # Update all_boy_groups.json (add views and likes column to boy groups)
    update_all_boy_groups_json_views_likes()
    # Update girl_groups.json file (with all info about all girl groups w/o views, likes, etc.)
    update_girl_groups_json()
    # Update all_girl_groups.json (add views and likes column to girl groups)
    update_all_girl_groups_json_views_likes()