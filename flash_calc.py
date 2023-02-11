import os
import random
import time

count = 0
while input("続けますか?: はい(Y) いいえ(N)") != "N":
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    ans = a + b
    print("{} + {} = ?".format(a, b))
    time.sleep(2)
    os.system('clear')
    user_input = int(input("答えを入力してください: "))

    if user_input == ans:
        print("正解です")
        count += 1
    else:
        print("不正解です")

print("{}問正解しました。".format(count))
