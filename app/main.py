def copy_file(text: str) -> None:
    text_buffer = []
    text_separ = text.split(" ")

    if text_separ[0] != "cp":
        return
    if len(text_separ) != 3:
        return
    if text_separ[1] == text_separ[2]:
        return

    try:
        with (open(text_separ[1], "r") as input_file,
              open(text_separ[2], "w") as output_file):
            for line in input_file:
                text_buffer.append(line)
            output_file.write("\n".join(text_buffer))
    except FileNotFoundError:
        return
