from os import path


def copy_file(command: str) -> None:
    command = command.split()

    if len(command) != 3 or command[0] != "cp":
        print("Invalid input format! Make sure the input "
              "string contains 3 elements separated by space, "
              "and has cp on a first place.")
        return

    if not path.exists(command[1]):
        print(f"File {command[1]} was not found!")
        return

    if command[1] == command[2]:
        print("Source and destination cannot be the same file!")
        return

    with (open(command[1], "r") as file_in,
          open(command[2], "w") as file_out):
        file_out.write(file_in.read())
