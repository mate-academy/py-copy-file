def copy_file(command: str) -> None:
    command_list = command.split()

    if (
        len(command_list) != 3
        or command_list[0] != "cp"
    ):
        return

    filename = command_list[1]
    new_filename = command_list[2]

    if filename == new_filename:
        return

    try:
        with (open(filename, "r") as file_in,
              open(new_filename, "w") as file_out):

            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
