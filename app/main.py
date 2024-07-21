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
        with (open(file_name_to_copy, "r") as f1,
              open(new_file_name, "w") as f2):
            f2.write(f1.read())
    except FileNotFoundError:
        print(f"File {file_name_to_copy} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
