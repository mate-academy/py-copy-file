# write your code here
def copy_file(command: str) -> None:

    cp, source_file_name, copy_file_name = command.split()
    if cp != "cp" or source_file_name == copy_file_name:
        return

    with (open(source_file_name, "r") as source,
          open(copy_file_name, "w") as backup):
        backup.write(source.read())
