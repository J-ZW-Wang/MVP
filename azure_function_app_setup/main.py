def count_chars(inputstr: str = "Hello") -> str:
    # Count the number of characters in the input string
    return f"The input string '{inputstr}' has {len(inputstr)} characters."


if __name__ == "__main__":
    print(count_chars())
