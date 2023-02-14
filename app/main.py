def copy_file(command: str) -> None:
    data = command.split()
    if data[0] == "cp":
        file_1 = data[1]
        file_2 = data[2]
        with open(file_1, "r") as file_in, open(file_2, "w") as file_out:
            if file_1 != file_2:
                content_to_copy = file_in.read()
                file_out.write(content_to_copy)
