def copy_file(user_input: str) -> None:
    user_input_args = user_input.split(" ")

    assert len(user_input_args) == 3

    cmd, source_filename, destination_filename = user_input_args

    assert cmd == "cp"

    if source_filename == destination_filename:
        return

    with open(source_filename, "r") as source_file, open(
        destination_filename, "w"
    ) as destination_file:
        destination_file.write(source_file.read())
