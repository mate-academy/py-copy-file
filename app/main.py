def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    sourse_file = parts[1]
    dest_file = parts[2]
    if sourse_file == dest_file:
        return
    try:
        with (open(sourse_file, "r") as file_in,
              open(dest_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"Error: {sourse_file} not found.")
