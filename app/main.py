import re


def copy_file(command: str):
    file_names = re.findall(r"(\w+[-_.,]?\w+.txt)", command)

    if file_names[0] != file_names[1]:
        with open(file_names[0], "r") as f:
            with open(file_names[1], "w") as f2:
                f2.write(f.read())
                print("File copy is created successes")


copy_file("cp test.txt test-copy.txt")
