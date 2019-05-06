def my_func(*args, **kwargs):
    """Dummy function for testing example.
    If False is passed as a positional parameter, return False.
    If "Exception" is passed as a positional parameter, raise an exception.
    Else, return True
    """
    if False in args:
        return False
    if "Error" in args:
        raise RuntimeError
    return True
