def copy_file(command: str) -> None:
    list_of_tokens = command.split()
    if list_of_tokens[1] == list_of_tokens[2]:
        return None
    with open(list_of_tokens[1], "r") as file_in, \
            open(list_of_tokens[2], "w") as file_out:
        file_out.write(file_in.read())
