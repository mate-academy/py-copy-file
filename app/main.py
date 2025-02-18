def copy_file(command: str) -> None:
    workflow = command.split(" ")
    if (len(workflow) == 3
            and workflow[0] == "cp"
            and workflow[1] != workflow[2]):
        with (open(f"{workflow[1]}", "r") as source_file,
              open(f"{workflow[2]}", "w") as new_file):
            new_file.write(source_file.read())
