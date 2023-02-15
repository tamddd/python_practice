import os
import random
import time

class Flash_mental_arithmetic:

    def __init__(self):
        self.user_name = input("ユーザ名を入力してください: ")

    def flash(self):
        total = 0
        print("開始5秒前")
        for i in range(5, 0, -1):
            os.system('clear')
            print(i)
            time.sleep(1)
            
        for i in range(10):
            print("start")
            os.system('clear')
            num = random.randint(1, 9)
            print(num)
            time.sleep(0.7)
            os.system('clear')
            total += num
        try:
            user_input = int(input("答えを入力してください"))
        except:
            print("不正な入力です")
            return
        
        print("正解です!!!" if total == user_input)\
                            else "不正解です!!!")
        return
    
    def main(self):
        print("{}さん、ようこそ".format(self.user_name))
        is_start = input("ゲームを開始しますか？: はい（y）いいえ(n)")
        if is_start != "y":
            print("終了します")
            exit()
        else:
            self.flash()

if __name__ == "__main__":
    game = Flash_mental_arithmetic()
    game.main()
