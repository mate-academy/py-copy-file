def copy_file(command: str) -> None:

    command_content = command.split(" ")

    if len(command_content) == 3:
        command, filename_in, filename_out = command_content

        if command == "cp" and filename_in != filename_out:
            with (open(filename_in, "r") as file_in,
                  open(filename_out, "w") as file_out):
                for line in file_in.readlines():
                    file_out.write(line)
