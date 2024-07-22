def copy_file(command: str) -> None:
    garbage, copy_name, new_name = command.split()
    if copy_name == new_name:
        return
    try:
        with open(copy_name, "r") as file_in, open(new_name, "w") as file_out:
            data = file_in.read()
            file_out.write(data)
    except FileNotFoundError:
        print("No such file in the directory")
