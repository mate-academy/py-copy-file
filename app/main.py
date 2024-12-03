def copy_file(command: str) -> None:
    command = [command_param for command_param in command.split()]
    if len(command) == 3:
        command_cp = command[0]
        file_source = command[1]
        file_target = command[2]
        if file_source != file_target and command_cp == "cp":
            try:
                with (open(file_source, "r") as file_source_obj,
                      open(file_target, "w") as file_target_obj):
                    file_target_obj.write(file_source_obj.read())
            except FileNotFoundError as e:
                print(f"Error: {e}")
                print("Desired file was not found")
            except IOError as e:
                print(f"Error: {e}")
                print("Something happened during read/write")
