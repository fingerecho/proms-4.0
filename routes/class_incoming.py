from abc import ABCMeta, abstractmethod
import database

from . import w_l

class IncomingClass(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, request):
        self.request = request
        self.graph = None
        self.uri = None
        self.named_graph_uri = None
        self.error_messages = None

    @abstractmethod
    def valid(self):
        pass

    @abstractmethod
    def determine_uri(self):
        pass

    def stored(self):
        """ Add an item to PROMS"""
        if self.graph is None or self.named_graph_uri is None:
            msg = 'The graph and the named_grapoh_uri properties of this class instance must not be None when trying ' \
                  'to store this instance in the provenance DB.'
            self.error_messages = msg
            return False
        try:
            w_l(str(self.graph))
            w_l(str(self.named_graph_uri))
            database.insert(self.graph, self.named_graph_uri)
            return True
        except Exception as e:
            self.error_messages = ['Could not connect to the provenance database']
            return False
