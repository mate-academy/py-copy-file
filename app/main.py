def copy_file(text: str) -> None:
    tokens = text.split(" ")

    if len(tokens) != 3:
        return

    if tokens[0] != "cp":
        return

    if tokens[1] == tokens[2]:
        return

    try:
        with (open(tokens[1], "r") as input_file,
              open(tokens[2], "w") as output_file):
            content = input_file.read()
            output_file.write(content)
    except FileNotFoundError:
        return
