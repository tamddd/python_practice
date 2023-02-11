import os
import random
import time

def question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    ans = a + b
    print("{} + {} = ?".format(a, b))
    time.sleep(2)
    os.system('clear')
    user_input = int(input("答えを入力してください: "))
    if user_input == ans:
        print("正解です")
        return True
    else:
        print("不正解です")
        return False

def main():
    correct_count = 0
    wrong_count = 0

    number_of_question = int(input("何問解きますか？: "))

    for _ in range(number_of_question):
        if question():
            correct_count += 1
        else:
            wrong_count += 1

    if correct_count == number_of_question:
        print("全問正解！パーフェクトです")
    elif correct_count != 0:
        print("{}問中{}問正解です".format(number_of_question, correct_count))
    else:
        print("全問不正解！頑張って")

if __name__ == "__main__":
    main()
