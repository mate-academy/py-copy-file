def copy_file(command: str) -> None:
    parts_command = command.split()
    if len(parts_command) != 3 or parts_command[0] != "cp":
        print("Incorrect data! "
              "The command should look like this "
              "'cp file.txt file-copy.txt'. ")
        return
    elif parts_command[1] == parts_command[2]:
        print("You cannot copy a file to a file with the same name."
              " Does nothing. ")
        return
    try:
        with (open(parts_command[1], "r") as file_in,
              open(parts_command[2], "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"The file '{parts_command[1]}' was not found.")
