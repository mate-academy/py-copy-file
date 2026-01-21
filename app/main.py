def copy_file(command: str) -> None:
    if len(command.split(" ")) != 3 or not command.split(" ")[0] == "cp":
        return
    in_name, out_name = command.split(" ")[1:]
    if in_name == out_name:
        return
    with open(in_name, "r") as file_in, open(out_name, "w") as file_out:
        file_out.write(file_in.read())
