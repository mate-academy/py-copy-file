import os.path


def copy_file(command: str) -> None:
    commands = command.split()
    if (
        len(commands) < 3
        or commands[0] != "cp"
        or commands[1] == commands[2]
    ):
        return

    if not os.path.exists(commands[1]):
        print(f"Error: Source file '{commands[1]}' does not exist.")
        return

    try:
        with (open(commands[1], "r") as source,
              open(commands[2], "w") as target):
            target.write(source.read())
    except FileNotFoundError:
        print(f"Error: File '{commands[1]}' not found.")
    except PermissionError:
        print(f"Error: Permission denied for '{commands[2]}'.")
    except UnicodeError:
        print("Error: Unicode error while copying the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    copy_file(input("Input command: "))
