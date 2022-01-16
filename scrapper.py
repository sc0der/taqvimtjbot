import requests
from bs4 import BeautifulSoup
import re
import json
import csv
import os
import requests

class GlobalMessage:

    def init_message_file(self):
        f = open("/home/sirius/Documents/namoz_bot/messages.json","r", encoding='utf-8')
        data = json.load(f)
        return data

    def init_chats_file(self):
        data = []
        csv_file = open("/home/sirius/Documents/namoz_bot/chats.csv")
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            data = row
        return set(data)

    def add_new_chat(self, chat_id):
        csv_file = open("/home/sirius/Documents/namoz_bot/chats.csv", "a")
        csv_file.write(str(chat_id)+",")
        csv_file.close()

    def sendNotification(self, notification,bot_token, bot_chatID):
        send_text = 'https://api.telegram.org/bot' + bot_token + \
            '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=HTML&text=' + notification
        response = requests.get(send_text)
        return response.json()

    def send_text(self, notification,bot_token):
        for item in self.init_chats_file():
            print(item)
            self.sendNotification(notification,bot_token, item)

    def init_namoz_file(self):
        f = open("/home/sirius/Documents/namoz_bot/today.json","r", encoding='utf-8')
        data = json.load(f)
        return data
        
    def get_message(self, key_value):
        data = self.init_message_file()[key_value]
        return data
    
    def get_namoz(self, key_value):
        data = self.init_namoz_file()[key_value]
        return data

    def converter(self, value):
        text = value.split("-")
        msg = f"""Az: {text[0]} \nTo: {text[1]}"""
        return msg
class ScraperModule:
    def __init__(self, url):
        self.url = url

    def scrap_page(self):
        data = []
        page = requests.get(self.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        main_content = soup.find(class_="today")
        today = {
            "day":"",
            "date":'',
            "subh":"",
            "zukhr":"",
            "asr":"",
            "maghrib":"",
            "isha":"",
            "no_namaz":""
        }
        # print(list(main_content)[1:])
        converted_list = list(main_content)
        converted_list = [self.replacer("".join(str(item).split())) for item in converted_list]
        
        for sline in converted_list:
            if sline != "":
                print(sline)
                data.append(sline)

        today["day"] = data[0]
        today["date"] = data[1]
        today["subh"] = data[3]
        today["zukhr"] = data[4]
        today["asr"] = data[5]
        today["maghrib"] = data[7]
        today["isha"] = data[8]
        today["no_namaz"] = data[6]
        with open("today.json", "w", encoding='utf8') as file:
            json.dump(today, file, ensure_ascii=False)
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