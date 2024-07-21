import shutil


def copy_file(command: str) -> None:
    splited = command.split()

    if len(splited) != 3:
        print("Command must have 3 arguments: 'cp <source> <destination>'")
        return

    cp = splited[0]
    if cp != "cp":
        print("Command must be started from 'cp'")
        return

    file_name_to_copy = splited[1]
    new_file_name = splited[2]

    if file_name_to_copy == new_file_name:
        print("Files can't have the same titles")
        return

    try:
        shutil.copy(file_name_to_copy, new_file_name)
        print(f"File '{file_name_to_copy}' copied into '{new_file_name}'")
    except FileNotFoundError:
        print(f"File '{file_name_to_copy}' is not found")
    except Exception as e:
        print(f"Error: {e}")
