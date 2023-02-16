import os
"""
その本のタイトルをファイル名にしたメモを作成する。
まず、その本のメモがすでにあるのかを判定
なければ、作成、

"""
class BookInfo:
    def __init__(self, title, date):
        self.title = title
        self.date = date

class BookMemo:
    def __init__(self):
        self.dir = "./book_memos"

    def read(self):
        """
        読むだけ、ファイル名を入れて、なければエラーを返す
        """
        pass

    def write(self):
        """
        すでにファイルがある場合はタイトルなどは書き込まず、
        読んだ日付を書きたい
        """
        pass

    def make_file(self):
        """
        ファイルがなければ、最初にその本のタイトルでファイルを作り、
        最初にその本のタイトルと、日付を書き込む。
        """
        pass
