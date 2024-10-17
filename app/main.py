def copy_file(line: str) -> None:
    old_file_name = line.split()[1]
    new_file_name = line.split()[2]
    with open(old_file_name, "r") as file_in, open(new_file_name, "w") as file_out:
        if old_file_name != new_file_name and line.split()[0] == "cp":
            content = file_in.read()
            file_out.write(content)
