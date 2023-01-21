def copy_file(command: str) -> None:
    file_names = command[3:].split(" ")
    if file_names[0] != file_names[1]:
        with open(file_names[0],
                  "r") as file_in, open(file_names[1], "w") as file_out:
            file_out.write(file_in.read())
