# No using the built in type check function
# https://www.w3schools.com/python/python_try_except.asp

def sum(arr: list) -> int:
    """
    Return the sum of all numbers within the given list.
    Non-numeric values are ignored using try/except.
    """
    total = 0
    for item in arr:
        try:
            total += item
        except TypeError:
            # item can't be added (e.g., string, list, etc.) → skip it
            pass
    return total


def cleanData(rawData: list) -> list:
    """
    Take in a list and return a new list that contains only the values
    that can be typecast to a float.
    """
    cleaned = []
    for item in rawData:
        try:
            cleaned.append(float(item))
        except (ValueError, TypeError):
            # Can't convert to float → skip it
            pass
    return cleaned


def unreliableCalculator(divisors: list) -> list:
    """
    Take in a list and return a new list where each index is 100 divided
    by the values from the input list.
    If division causes an error, store the error type name as a string.
    Example: [100, 50, 25, "5"] → [1, 2, 4, "TypeError"]
    """
    results = []
    for item in divisors:
        try:
            results.append(100 / item)
        except Exception as e:
            results.append(type(e).__name__)
    return results


def upperAll(arr: list) -> None:
    """
    Uppercase all strings within the given list.
    Modify the original list in-place; do not return a new list.
    """
    for i in range(len(arr)):
        try:
            arr[i] = arr[i].upper()
        except AttributeError:
            # Value has no .upper() (e.g., int) → leave it unchanged
            pass


def firstItems(arr: list) -> list:
    """
    Given a list of values where many elements may themselves be lists:
    - If an element is a list, grab its first element.
    - If the element is not a list, use the value itself.
    Return a new list of these "first items".
    Example: firstItems([[1, 2], [3, 4], [5, 6], [7, 8], 9]) == [1, 3, 5, 7, 9]
    """
    result = []
    for item in arr:
        try:
            # If item supports indexing like a list (e.g. inner list),
            # this will work; for non-sequences like ints it will raise.
            result.append(item[0])
        except Exception:
            # Not indexable (or not treated as list here) → use the item itself
            result.append(item)
    return result
