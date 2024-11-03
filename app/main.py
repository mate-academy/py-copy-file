def copy_file(command: str) -> None:
    command_attributes = [command_param
                          for command_param in command.split()
                          if command_param not in ["cp", ""]]
    file_source = command_attributes[0]
    file_target = command_attributes[1]
    if file_source != file_target:
        with (open(file_source, "r") as file_source_obj,
              open(file_target, "w") as file_target_obj):
            file_target_obj.write(file_source_obj.read())
