def copy_file(command: str) -> None:
    command = command.split()
    if len(command) < 3:
        return
    if command[0] != "cp":
        return
    first_file = command[1]
    second_file = command[2]
    if first_file == second_file:
        return

    try:
        with (open(first_file, "r") as original_file,
              open(second_file, "w") as coped_file):
            coped_file.write(original_file.read())
    except FileNotFoundError:
        print("File not found")
