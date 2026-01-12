#No using the built in type check function
#https://www.w3schools.com/python/python_try_except.asp


def sum(arr : list) -> int:
    """
    Modify the function such that it returns the sum of all numebrs within the given list.
    :param arr:
    :return:
    """
 def sum(arr: list) -> int:
    total = 0
    for item in arr:
        try:
            total += item
        except TypeError:
            pass
    return total
    
def cleanData(rawData : list) ->list:
    """
    modify the function such that it takes in a list as an argument will return a new list that
     contains only the valeus that can be typecast to a float.
    :param rawData:
    :return:
    """
def cleanData(rawData: list) -> list:
    cleaned = []
    for item in rawData:
        try:
            cleaned.append(float(item))
        except (ValueError, TypeError):
            pass
    return cleaned

def unreliableCalculator(divisors : list) -> list:
    """
    Modify the function such that it takes in a list as an argument and returns a new list where each
    index is 100 divided by the values from the input list.
    If division ever causes an error instead have the value be the type of error as a string.
    Example the list [100,50,25,"5"] as an argument would return [1, 2, 4, "TypeError"]
    :param divisors:
    :return:
    """
def unreliableCalculator(divisors: list) -> list:
    results = []
    for item in divisors:
        try:
            results.append(100 / item)
        except Exception as e:
            results.append(type(e).__name__)
    return results
    pass
    
def upperAll(arr : list) -> None:
    """
    Modiy the function such that is uppercases all strings within the given argument list.
    The string method .upper() turns all characters in as tirng uppercase.
    You should mpdify the original list not return a new list.
    :param arr:
    :return:
    """
    x = "hello"
    print(x)
    x = x.upper()
    print(x)
def upperAll(arr: list) -> None:
    for i in range(len(arr)):
        try:
            arr[i] = arr[i].upper()
        except AttributeError:
            pass

def firstItems(arr : list) -> list:
    """
    Modify the function below such that given a list of values. Many of the list elements will be lists
    themselves. For any list element that is a list grab the first element from that list. If the list
    element is not a list then just grab the value itself.
    Create a new list of all the first indexes of inner lists or just values themselves.
    Example firstItems( [[1,2],[3,4],[5,6],[7,8]],9 ) == [1,3,5,7,9]
    :param arr:
    :return:
    """
  def firstItems(arr: list) -> list:
    result = []
    for item in arr:
        try:
            result.append(item[0])
        except Exception:
            result.append(item)
    return result
