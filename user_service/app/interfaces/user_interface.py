from abc import ABC, abstractmethod

from flask.views import MethodView


class BaseApiView(ABC, MethodView):
    pass
    # @abstractmethod
    # def handle_error(self, e, message, status_code):
    #     pass

    # @abstractmethod
    # def handle_response(self, result):
    #     pass
