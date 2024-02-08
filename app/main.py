def copy_file(input_str: str) -> None:
    list_str = input_str.split()
    if list_str[1] == list_str[2]:
        return None
    with open(list_str[1], "r") as file_in, open(list_str[2], "w") as file_out:
        text_from_file_in = file_in.read()
        file_out.write(text_from_file_in)
