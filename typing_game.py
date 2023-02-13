import os
import time

"""
テキストを取ってくる。
それを一文字ずつfor文で回して、
それと同じ文字を入力すればOK
ダメならもう一度。

通常、文字入力した後はエンターキーを押して入力を確定させる必要があるが、
タイピングゲームなので、それを省く必要がある。
"""

class TypingGame:

    def __init__(self):
        self.txt = self.get_text()

    def get_text(self):
        TXT_PATH = "typing.txt"
        txt_lst = []
        with open(TXT_PATH, "r") as f:
            f = f.readlines()
            for i in f:
                txt_lst.append(i)
        return txt_lst

    def is_correct_input(self, user_input, txt):
        return user_input == txt
    
    def game(self):
        os.system('clear')
        for i in self.txt:
            if i == "":
                continue
            deq_txt = deque(i)
            while len(deq_txt) != 0:
                now_char = deq.popleft()
                while not is_correct_input(  ,now_char):
                    
                print(deq_txt)

    def start(self):
        is_start = input("ゲームを始めますか？: はい（Y）いいえ（N) ")
        if is_start == "Y":
            self.game()
        else:
            print("終了します。")
            exit()

def main():
    game = TypingGame()
    game.start()

if __name__ == "__main__":
    main()
