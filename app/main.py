def copy_file(command: str) -> None:

    user_command, source_file, result_file = command.split()

    if source_file != result_file and user_command == "cd":
        with (open(source_file, "r") as file_out,
              open(result_file, "w") as file_to):
            file_to.write(file_out.read())
