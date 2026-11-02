def copy_file(command: str) -> None:
    elements = command.split(" ")
    if (len(elements) != 3
            or (elements[0] != "cp" or elements[1] == elements[2])):
        return
    try:
        with (open(elements[1], "r") as input_file,
              open(elements[2], "w") as output_file):
            for i in input_file.readlines():
                output_file.write(i)
    except Exception:
        return
