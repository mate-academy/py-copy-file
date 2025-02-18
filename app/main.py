def copy_file(command: str) -> None:
    command, old_file, new_file = command.split()

    if len(command.split()) == 3 and command == "cp":
        if old_file != new_file:
            try:
                with (open(old_file, "r") as file_in,
                      open(new_file, "w") as file_out):
                    data = file_in.read()
                    file_out.write(data)
                print(f"Copying completed: {old_file} -> {new_file}")
            except FileNotFoundError:
                print("Error: File not found")
        else:
            print("Error: Source and destination file names are the same")
