# Check Your Code Against the Following Points

## Code Efficiency

Make sure you check that the input string contains 3 elements separated by space, and has `cp` on a first place.

## Code Style

1. Use a consistent style of quotes in your code: either double or single, but double quotes are preferred.
2. Use descriptive and correct variable names.

Good example:

```python
source_file_name = "list_of_workers.txt"
with open(source_file_name, "r") as source_file_object:
    pass
```

Bad example:

```python
f1 = "list_of_workers.txt"
with open(f1, "r") as f_s:
    pass
```

3. Be sure that you are calling needed methods only once (e.g. `.split()`).

## Clean Code

Add comments, prints, and functions to check your solution when you write your code. 
Don't forget to delete them when you are ready to commit and push your code.
