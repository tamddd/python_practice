import sys

def reverse(input_path, output_path):
    with open(input_path, "r") as f:
        s = f.read()
        with open(output_path, "w") as write_file:
            write_file.write(s[::-1])

def copy(input_path, output_path):
    with open(input_path, "r") as f:
        s = f.read()
        with open(output_path, "w") as write_file:
            write_file.write(s)

def duplicate_contents(input_path, n):
    with open(input_path, "r") as f:
        s = f.read()
    for _ in range(n):
        with open(input_path, "w") as f:
            f.write(s)

def replace_string(input_path, needle, new_string):
    with open(input_path, "r") as f:
        s = f.read()
    reps = s.replace(needle, new_string)
    with open(input_path, "r") as f:
        f.write(reps)

def main():
    if len(sys.argv) < 2:
        print("引数がたりません")
        exit()
    input_path = sys.argv[1]
    command = sys.argv[0]

    if command == "replace":
        n = sys.argv[2]
    elif command == "replace":
        needle = sys.argv[2]
        new_string = sys.argv[3]
    else:
        output_path = sys.argv[2]

    if command == "reverse":
        reverse(input_path, output_path)
    elif command == "copy":
        copy(input_path, output_path)
    elif command == "duplicate":
        duplicate_contents(input_path, n)
    elif command == "replace":
        replace_string(input_path, needle, new_string)
    else:
        print("そのコマンドはありません")
        exit()

if __name__ == "__main__":
    main()
