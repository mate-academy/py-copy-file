def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        command_to_execute, file, new_file = command.split()
        if file == new_file:
            return
        if command_to_execute.lower() == "cp":
            try:
                with open(file, "r") as source, open(new_file, "w") as new:
                    new.write(source.read())
            except (FileNotFoundError, IOError) as err:
                print("Error: ", err)
