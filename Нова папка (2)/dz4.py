

def divider(a, b):
 if a < b:
    raise ValueError
 if b > 100:
    raise IndexError
 else:
    return a/b

data = {10: 2, 2: 5, "123": 4, 18: 0, 45 : 15, 8: 4}

while True:
    key = 0
    result = []
    try:
        for key in data:
            res = divider(key, data[key])
            result.append(res)

    except(ValueError):
        print(f"ValueError : {key}")
        del data[key]
        continue

    except(TypeError):
        print(f"TypeError : {key}")
        del data[key]
        continue

    except(ZeroDivisionError):
        print(f"ZeroDivisionError : {key}")
        del data[key]
        continue



    else:
        print(result)
        break
   