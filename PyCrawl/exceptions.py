class SentryDSNNotSet(Exception):
    def __init__(self):
        super().__init__("Sentry DSN not set.")


class InvalidMethod(Exception):
    def __int__(self, meth):
        super().__init__(f"Method {meth} is not valid. Use a method form PyCrawl.http.methods.PyCrawlMethods")
