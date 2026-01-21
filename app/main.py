import os


def copy_file(command: str) -> None:
    split_command = command.split(" ")
    if len(split_command) != 3 or split_command[0] != "cp":
        print("Invalid command format")
        return

    source_file = split_command[1]
    target_file = split_command[2]

    if source_file == target_file:
        print(f"The file {source_file} has the same name as {target_file}")
        return
    if not os.path.exists(source_file):
        print(f"source file '{source_file}' does not exist")
        return

    with open(source_file) as f1, open(target_file, "w") as f2:
        context = f1.read()
        f2.write(context)
