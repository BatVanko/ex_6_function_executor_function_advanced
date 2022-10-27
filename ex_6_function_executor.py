def func_executor(func, *args):
    def func(*args):
        result = tuple(s.upper() for s in strings)
        return result








def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
