def copy_file(command: str) -> None:
    all_data = command.split(" ")
    with open(all_data[1], "r") as file_in, open(all_data[2], "w") as file_out:
        if all_data[1] != all_data[2]:
            content = file_in.read()
            file_out.write(content)
