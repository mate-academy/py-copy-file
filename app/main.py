def copy_file(command: str) -> None:
    find_txt = command.index("txt")
    first_file_name = command[3 : (find_txt + 3)]
    second_file_name = command[(find_txt + 4) :]

    with open(first_file_name, "r") as file_in, open(
        second_file_name, "w"
    ) as file_out:
        file_in_content = file_in.read()
        file_out.write(str(file_in_content))
