def copy_file(command: str) -> None:
    data = command.split(" ")
    if data[1] == data[2]:
        pass
    else:
        with open(data[1], "r") as file_in, open(data[2], "w") as file_out:
            file_data = file_in.readlines()
            for row in file_data:
                file_out.write(row)
