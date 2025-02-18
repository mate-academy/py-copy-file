# write your code here

def copy_file(command: str) -> None:
    comparison_list = command.split()
    if len(comparison_list) == 3 and "cp" in command:
        _, source_path, destination_path = comparison_list
    if source_path != destination_path:
        with (open(source_path, "r") as source_file,
              open(destination_path, "w") as destination_file):

            destination_file.write(source_file.read())
