from abc import ABC, abstractmethod


class HttpClient(ABC):
    @abstractmethod
    def get(self, url, params=None):
        pass
