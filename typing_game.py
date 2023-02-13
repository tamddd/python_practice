from collections import deque
import os
import readchar
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
        start = time.time()
        miss_count = 0
        os.system('clear')
        for i in self.txt:
            if i == "":
                continue
            print(i)
            deq_txt = deque(i)
            while len(deq_txt) != 1:
                now_char = deq_txt.popleft()
                while not self.is_correct_input(readchar.readkey(), now_char):
                    miss_count += 1
                os.system('clear')
                print("".join(deq_txt))
        print("終了です")
        print("{}回ミスしました".format(miss_count)if miss_count != 0\
              else "ノーミス、パーフェクトです")
        print("タイムは{}秒です。".format(time.time() - start))
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
