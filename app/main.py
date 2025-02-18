def copy_file(command: str) -> None:

    command_content = command.split()

    if len(command_content) == 3:
        command_name, filename_in, filename_out = command_content

        if command_name == "cp" and filename_in != filename_out:
            with (open(filename_in, "r") as file_in,
                  open(filename_out, "w") as file_out):
                file_out.write(file_in.read())
