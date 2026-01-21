def copy_file(command: str) -> None:
    command_keyword, initial_filename, copied_filename = command.split()
    if command_keyword == "cp" and initial_filename != copied_filename:
        with (open(initial_filename, "r") as source,
              (copied_filename, "w") as copied_file):
            copied_file.write(source.read())
