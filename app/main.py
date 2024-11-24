def copy_file(input_str: str) -> None:
    old_name, new_name = input_str.strip("cp ").split()
    if old_name != new_name:
        with open(old_name, "r") as input_file, open(new_name, "a") as output_file:
            for line in input_file:
                output_file.write(line)
