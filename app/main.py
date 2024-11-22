import os


def copy_file(argument: str) -> None:
    file_source = argument.split(" ")[1]
    file_destination = argument.split(" ")[2]
    if not os.path.isfile(file_source):
        print(f"File '{file_source}' is not exist.")
        return
    elif os.path.isfile(file_destination):
        print(f"File '{file_destination}' is exist.")
        return
    with open(file_source, "r") as f1, open(file_destination, "w") as f2:
        f2.write(f1.read())
