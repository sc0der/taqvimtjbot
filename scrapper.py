import requests
from bs4 import BeautifulSoup
import re
import json
import os


class GlobalMessage:

    def init_message_file(self):
        f = open("/home/sirius/Documents/namoz_bot/messages.json","r", encoding='utf-8')
        data = json.load(f)
        return data

    def init_namoz_file(self):
        f = open("/home/sirius/Documents/namoz_bot/today.json","r", encoding='utf-8')
        data = json.load(f)
        return data
        
    def get_message(self, key_value):
        data = self.init_message_file()[key_value]
        return data

class ScraperModule:
    def __init__(self, url):
        self.url = url

    def scrap_page(self):
        data = []
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        main_content = soup.find(class_="today")
        today = {
            "bomdod":"",
            "peshin":"",
            "asr":"",
            "shom":"",
            "khuftan":"",
            "no_namaz":""
        }
        converted_list = list(main_content)[2:]
        converted_list = [self.replacer("".join(str(item).split())) for item in converted_list]
        
        for sline in converted_list:
            if sline != "":
                data.append(sline)

        today["bomdod"] = data[2]
        today["peshin"] = data[3]
        today["asr"] = data[4]
        today["shom"] = data[6]
        today["khuftan"] = data[7]
        today["no_namaz"] = data[5]
        with open("today.json", "w") as file:
            json.dump(today, file)
            file.close()
    

    def replacer(self, value):
        row2 = re.sub("<td>", '', str(value))
        row3 = re.sub("</td>", '', row2)
        return row3


class TgGroupsModule:

    def new_group(self, group_id):
        with open("groups.csv", "w") as file:
            file.write(group_id)
            file.close()

    def check_Group_id(self, group_id):
        pass