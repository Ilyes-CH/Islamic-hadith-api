weather : str = "good"

match(weather):
    case("good"):
        print('good weather')
    case('not good'):
        print('bad weather')
    case _:
        pass