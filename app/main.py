def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) == 3 and parts[0] == "cp":
        source_file = parts[1]
        destination_file = parts[2]

        if source_file != destination_file:
            with (open(source_file, "r") as file_in,
                  open(destination_file, "w") as file_out):
                file_out.write(file_in.read())
                print(f"File '{source_file}' copied to"
                      f" '{destination_file}'")
        else:
            print("Source and destination files have the same name."
                  " Doing nothing.")
    else:
        print("Invalid command."
              " Please use the format: 'cp source_file destination_file'")
