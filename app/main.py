def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) < 3:
        return
    func, file, destination_file = parts
    if func != "cp":
        print("no command")
        return
    if file == destination_file:
        print("File name is the same, copying aborted.")
        return
    try:
        with (open(f"{file}.txt", "r") as file_in,
              open(f"{destination_file}.txt", "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        print("No such file")
