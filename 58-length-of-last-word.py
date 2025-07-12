def lengthOfLastWord(s: str) -> int:
    end: int = len(s) - 1

    while s[end] == " ":
        end -= 1

    start: int = end
    while start >= 0 and s[start] != " ":
        start -= 1

    return end - start
