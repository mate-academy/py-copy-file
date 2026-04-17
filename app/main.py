from os.path import isfile, abspath


def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        return
    (copy_command, file_original, file_copied) = command_parts
    if (
            copy_command != "cp"
            or not isfile(file_original)
            or abspath(file_original) == abspath(file_copied)
    ):
        return
    with (
        open(file_original, "r") as fobj_original,
        open(file_copied, "w") as fobj_copied
    ):
        fobj_copied.write(fobj_original.read())
