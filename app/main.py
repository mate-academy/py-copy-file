def copy_file(command: str) -> None:
    command = command.split()
    if len(command) == 3:
        linux_command, file_in, file_out = command

        if linux_command == "cp" and file_in != file_out:
            with (open(file_in, "r") as file_in,
                  open(file_out, "w") as file_out):
                file_out.write(file_in.read())
