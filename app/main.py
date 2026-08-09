import os


def copy_file(command: str) -> str:
    elements = command.split(" ")
    if elements[0] == "cp":
        if command == "":
            return
        source_file_name = elements[1]
        destination_file_name = elements[-1]
        if source_file_name == destination_file_name:
            return
        if os.path.exists(elements[1]):
            with (open(source_file_name, "r") as source_file_object,
                  open(destination_file_name, "w") as destination_file_object):
                destination_file_object.write(source_file_object.read())
            return
