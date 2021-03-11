import  os


def get_env_var():
    if 'TEST_ENV' in os.environ:
        return os.environ['TEST_ENV']
