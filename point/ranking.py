from os import path
import datetime
import json
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

from point.config.setting import Settings


class Ranking:
    def __init__(self):
        root = Tk()
        root.withdraw()
        self.settings = Settings()
        self.ranking_file = self.settings.ranking_file
        self.records = self.read_record()

    def read_record(self):
        if not path.exists(self.ranking_file):
            return []

        with open(self.ranking_file, 'r', encoding='utf-8') as fp:
            records = json.load(fp)

        return records

    def get_ranking(self, new_score):
        if not self.records:
            return 1

        score_list = []
        for record in self.records:
            score = record.get('score', None)
            if score and score not in score_list:
                score_list.append(score)
        score_list.sort(reverse=True)

        ranking = 1
        for score in score_list:
            if new_score >= score:
                break
            else:
                ranking += 1
        # sorted_records = sorted(self.records, key=lambda k: (k.get('score', 0)))
        return ranking

    def save_record(self, name, score):
        new_record = {"name": name, "score": score, "date": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        self.records.append(new_record)
        with open(self.ranking_file, 'w', encoding='utf-8') as fp:
            json.dump(self.records, fp, indent=4, ensure_ascii=False)

    def add_new_record(self, score):
        ranking = self.get_ranking(score)
        prompt_string = "得分: " + str(score) + \
                        "\n排名: " + str(ranking) + \
                        "\n名字: "
        name = simpledialog.askstring(title="保存记录", prompt=prompt_string, initialvalue="")
        if name:
            messagebox.showinfo(title="提示", message="感谢您的参与!")
            self.save_record(name, score)
