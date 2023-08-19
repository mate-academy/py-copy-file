def copy_file(command: str) -> None:
    command = command.split(" ")

    file_in_name = command[1]
    file_out_name = command[2]

    if file_in_name != file_out_name:
        with (open(file_in_name, "r") as file_in,
              open(file_out_name, "w") as file_out):
            file_out.write(file_in.read())
