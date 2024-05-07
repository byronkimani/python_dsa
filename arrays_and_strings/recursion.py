def recurse(i: int):
    if i > 3:
        return
    print(i)
    recurse(i + 1)
    print(f'End of call where i = {i}')
    return


recurse(1)
