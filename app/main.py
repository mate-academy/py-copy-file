from os.path import isfile


def copy_file(command: str) -> None:
    try:
        command, original_f, copy_f = command.split()
    except ValueError:
        return
    if command != "cp" or original_f == copy_f or not isfile(original_f):
        return
    with open(original_f) as file_in, open(copy_f, "w") as file_out:
        file_out.write(file_in.read())
