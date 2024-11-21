def copy_file(command: str) -> None:
    command = [command_param for command_param in command.split()]
    if len(command) == 3:
        command_cp = command_attributes[0]
        file_source = command_attributes[1]
        file_target = command_attributes[2]
        if file_source != file_target and command_cp == "cp":
            with (open(file_source, "r") as file_source_obj,
                  open(file_target, "w") as file_target_obj):
                file_target_obj.write(file_source_obj.read())
