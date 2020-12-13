class SentryDSNNotSet(Exception):
    def __init__(self):
        super().__init__("Sentry DSN not set.")
