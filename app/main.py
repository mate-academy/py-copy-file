def copy_file(command: str) -> str:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    old_file = parts[1]
    new_file = parts[2]

    if old_file == new_file:
        return

    try:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
            print(f"File {file_in} copied to file {file_out}.")

    except FileNotFoundError:
        print(f"File {new_file} does not exist.")
