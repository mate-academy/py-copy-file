import os


def copy_file(command: str) -> None:
    command_parts = command.split()

    if command_parts[1] == command_parts[2]:
        return

    if command_parts[0] != "cp":
        print("Wrong command use 'cp'.")
        return

    if not os.path.exists(command_parts[1]):
        print(f"File {command_parts[1]} not exist.")
        return

    try:
        with (open(command_parts[1], "r") as source_file,
              open(command_parts[2], "w") as destination_file):
            read_all = source_file.read()
            destination_file.write(read_all)
    except IOError as e:
        print(f"Error during copy file {e}")
