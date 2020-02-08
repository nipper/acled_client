import re

is_8601 = re.compile(r"\d{4}-\d{2}-\d{2}")


def valid_number(func):
    def func_wrapper(self, num, *args, **kwargs):

        try:
            int(num)
        except ValueError:
            raise ValueError(f"{num} isn't a number")

        res = func(self, num, *args, **kwargs)

        return res

    return func_wrapper
