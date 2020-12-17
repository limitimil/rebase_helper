import sys

class FeatureToggle:

    @staticmethod
    def disable(method):
        def wrapper(*argv, **argkw):
            sys.stderr.write("method {method} has been disabled.")
            return
        return wrapper


