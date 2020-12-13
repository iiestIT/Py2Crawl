from PyCrawl.utils.logging import init_logger
from PyCrawl.settings.base_settings import BaseSettings
from PyCrawl.utils.sentry import init_sentry
from PyCrawl.exceptions import SentryDSNNotSet


class PyCrawl:
    def __int__(self, settings=BaseSettings()):
        self.settings = settings
        self.logger = init_logger()

        if self.settings.SENTRY:
            if not self.settings.SENTRY_DSN == type(str):
                raise SentryDSNNotSet
            init_sentry(str(self.settings.SENTRY_DSN))

    def crawl(self, spider, *args, **kwargs):
        pass
