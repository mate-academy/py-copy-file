def copy_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format.")
        return
    _, first_file, second_file = parts
    if first_file == second_file:
        return
    try:
        with (open(first_file, "r") as file_in,
              open(second_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"File '{first_file}' not found.")
