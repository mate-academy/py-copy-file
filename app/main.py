import os


def copy_file(command: str) -> None:
    if len(command.split()) == 0:
        print("Command is empty")
        return

    if command.split()[0] != "cp" or len(command.split()) < 3:
        print("Command is not correct")
        return

    source_file_name = command.split()[1]
    target_file_name = command.split()[2]

    if not os.path.exists(source_file_name):
        print(f"File {source_file_name} doesn't exist")
        return

    if source_file_name == target_file_name:
        print(f"File {source_file_name} and {target_file_name} are the same")
        return

    with (
        open(source_file_name, "r") as source_file,
        open(target_file_name, "w") as target_file
    ):
        data = source_file.read()
        target_file.write(data)
