import os


def copy_file(command: str) -> None:
    file_name = []
    if command.startswith("cp"):
        file_name = command.split(" ")
    if len(file_name) < 3:
        print("missing one argument in command")
        return
    if file_name[1] == file_name[2]:
        print(f"The file {file_name[1]} has the same name as {file_name[2]}")
        return
    if not os.path.exists(file_name[1]):
        print(f"source file '{file_name[1]}' does not exist")
        return

    print(file_name)
    with open(file_name[1]) as f1, open(file_name[2], "w") as f2:
        context = f1.read()
        f2.write(context)
