def copy_file(name: str) -> None:
    file_names = name.split()
    if len(file_names) != 3 and file_names[0] != "cp":
        print("The command look like this: cp file.txt file-copy.txt")
    elif file_names[1] == file_names[2]:
        print("Program does nothing, "
              "please enter another name for second file")
    else:
        with (open(file_names[1], "r") as file_in,
              open(file_names[2], "w") as file_out):
            for line in file_in:
                file_out.write(line)
