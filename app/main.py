def copy_file(command: str):
    file = command.split(" ")[1]
    print(file)
    new_file = command.split(" ")[2]
    print(new_file)
    if file == new_file:
        return None
    with open(f"{file}", "r") as file_in, open(f"{new_file}", "w") as file_out:
        a = file_in.read()
        b = file_out.write(f"{a}")
