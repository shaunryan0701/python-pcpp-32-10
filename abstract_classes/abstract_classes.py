from abc import ABC, abstractmethod

class AbstractScanner(ABC):
    @abstractmethod
    def scan_document(self, document):
        # Scan a ducument
        pass
    
    @abstractmethod
    def get_scanner_status(self):
        # return the status of the scanner
        pass

class AbstractPrinter(ABC):
    @abstractmethod
    def print_document(self, document):
        # Print a document
        pass
    
    @abstractmethod
    def get_printer_status(self):
        # return the status of the printer
        pass