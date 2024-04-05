def copy_file(command: str) -> None:
    list_of_str = command.split(" ")
    old_file_n = list_of_str[0]
    new_file_n = list_of_str[1]
    if old_file_n == new_file_n:
        return
    with open(old_file_n, "r") as file_in, open(new_file_n, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
