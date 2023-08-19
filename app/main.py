def copy_file(command: str) -> None:
    # Split the command string to list with:
    # [0] command name
    # [1] file name to copy
    # [2] new file

    files_list = command.split()
    # Check files names

    if files_list[1] == files_list[2]:
        pass
    # Check the command

    if files_list[0] == "cp":
        # Open file and create copy with its content
        with (open(files_list[1], "r") as file_in,
              open(files_list[2], "w") as file_out):
            copy_content = file_in.read()
            file_out.write(copy_content)
    # If command is not "cp"

    else:
        print("Command is incorrect!")
