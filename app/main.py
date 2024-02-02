def copy_file(command: str) -> None:
    words_of_command = command.split(" ")
    if words_of_command[1] != words_of_command[2]:
        with (open(words_of_command[1], "r") as file_in,
              open(words_of_command[2], "w") as file_out):
            file_out.write(file_in.read())
