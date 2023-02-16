"""
todoリストをテキストで保存して、
それをデータベース代わりにする。
"""


class Todo:
    def __init__(self, title, date, is_finishied=False):
        self.title = title
        self.date = date
        self.is_finishied = is_finishied

    def __str__(self):
        return "{}: {} {}".format(self.title, self.date, self.is_finishied)


class TodoList:

    def __init__(self):
        self.TODO_FILE_PATH = "todo.txt"

    def add_todo(self):
        title = input("タイトルを入力してください: ")
        date = input("日付を入力してください: ")
        with open(self.TODO_FILE_PATH, "w") as f:
            f.write(str(Todo(title, date)))
        return

    def delete_todo(self):
        with open(self.TODO_FILE_PATH, "r") as f:
            fr = f.read()
            print(fr)
        return


def main():
    todo = TodoList()
    todo.add_todo()

if __name__ == "__main__":
    main()
