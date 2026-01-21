def copy_file(command: str) -> None:
    commands_list = command.split(" ")
    source_file = commands_list[1]
    destination_file = commands_list[2]

    if (len(commands_list) == 3
            and commands_list[0] == "cp"
            and source_file != destination_file):
        try:
            with (open(source_file, "r") as file_in,
                  open(destination_file, "w") as file_out):
                file_out.write(file_in.read())
        except FileNotFoundError:
            print(f"Error: Source file {commands_list[1]} not found.")
        except Exception as e:
            print(e)


copy_file("cp file.txt new_file.txt")
