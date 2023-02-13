import os
import random
import time

class MemoryGame:
    def __init__(self, user_name):
        self.score = 0
        self.user_name = user_name
        self.disapperarance_nums = []
        
    def drawing_square(self, lst):
        time.sleep(1)
        grid ="__|__|__"
        idx = 9
        for i in range(3):
            for j in range(3):
                print(lst[idx] if lst[idx] != 0 else " ", end=" |")
                idx -= 1
            print()
            print(grid)
        
    def generate_numbers_lst(self):
        lst = [i for i in range(9, -1, -1)]
        return lst

    def erase_at_random(self, lst):
        erase_at = random.randint(0, len(lst)-1)
        while not lst[erase_at]:
            erase_at = random.randint(0, len(lst)-1)
        return erase_at

    def check_order_of_disapperrance(self):
        user_input_order = []
        print("消えた順番に数字を入力してください")
        for i in range(9):
            user_input_order.append(input("数字を入力してください: "))
        return user_input_order == self.disapperarance_nums
    
    def start(self):
        os.system('clear')
        print("ゲームを開始しします")
        lst = self.generate_numbers_lst()
        self.drawing_square(lst)
        while sum(lst) != 0:    
            erase_at = self.erase_at_random(lst)
            self.disapperarance_nums.append(lst[erase_at])
            lst[erase_at] = 0
            self.drawing_square(lst)
            time.sleep(2)
            os.system('clear')
        print(self.disapperarance_nums)
        if self.check_order_of_disapperrance():
            print("正解です")
        else:
            print("不正解です")

if __name__ == "__main__":
    game = MemoryGame(input("ユーザ名を入力してください: "))
    game.start()
