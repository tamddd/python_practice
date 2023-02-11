import os
import random
import time

wrong_count = 0
correct_count = 0
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
        correct_count += 1
    else:
        print("不正解です")
        wrong_count += 1

print("{}問正解しました。".format(correct_count))
print("{}問間違え増田。".format(wrong_count)
      if wrong_count != 0
      else "全問正解です。 パーフェクト！！！")
