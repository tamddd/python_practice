import os
import time

class MemoryGame:
    def __init__(self, user_name):
        self.score = 0
        self.user_name = user_name

    def drawing_square(self):
        time.sleep(2)
        grid ="__|__|__"
        lst = [i for i in range(10, 0, -1)]
        for i in range(3):
            for j in range(3):
                print(lst.pop(), end=" |")
            print()
            print(grid)
        #ここから、順番に数字を消していく
            
    def game(self):
        os.system('clear')
        print("ゲームを開始しします")
        self.drawing_square()
        
        

if __name__ == "__main__":
    game = MemoryGame(input("ユーザ名を入力してください: "))
    game.game()
