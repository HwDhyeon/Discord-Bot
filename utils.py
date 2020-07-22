from colors import color


def colored_print(msg: str, color_name: str, *, end='\n'):
    print(color(msg, color_name), end=end)
