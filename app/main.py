def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    f_part, s_part, t_part = parts
    if s_part == t_part:
        return
    try:
        with open(s_part, "r") as file_in:
            content = file_in.read()
        with open(t_part, "w") as file_out:
            file_out.write(content)
    except FileNotFoundError:
        print("File not found")
