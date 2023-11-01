def copy_file(command: str) -> None:
    sep_phrases = command.split()
    old_filename = sep_phrases[1]
    new_filename = sep_phrases[2]
    if sep_phrases[0] == "cp" and old_filename != new_filename:

        with (
            open(old_filename, "r") as file_in,
            open(new_filename, "w") as file_out
        ):

            file_out.write(
                file_in.read()
            )
