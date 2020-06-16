
def function_said(times= 3):
    def function_wrapper(decorated_function):
        def wrapper(*args, **kwargs):
            print('Function said: ',end='')
            for _ in range(times):
                decorated_function(*args, **kwargs)

        return wrapper

    return function_wrapper

@ function_said(times=5)
def main(name):

    print(f'Hello  {name}')

if __name__ == '__main__':

    main('Radek')