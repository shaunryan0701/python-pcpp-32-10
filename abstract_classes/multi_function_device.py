from abstract_classes import AbstractScanner, AbstractPrinter

class MFD1(AbstractScanner, AbstractPrinter):
    max_resolution = "1200x1200"

    def scan_document(self, document):
        print(f"Scanning {document}...")
    
    def get_scanner_status(self):
        print("Scanner is ready.")
    
    def print_document(self, document):
        print(f"Printing {document}...")
    
    def get_printer_status(self):
        print(f'Max resolution: {MFD1.max_resolution}')
        print("Printer is ready.")

class MFD2(MFD1):
    max_resolution = "2400x2400"

    def get_printer_status(self):
        print(f'Max resolution: {MFD2.max_resolution}')
        print("Printer is ready.")

    def get_printer_operation_history(self):
        print("Printer operation history is available.")

class MFD3(MFD2):
    max_resolution = "4800x4800"
    
    def get_printer_status(self):
        print(f'Max resolution: {MFD3.max_resolution}')
        print("Printer is ready.")

    def get_fax_operation_history(self):
        print("Fax operation history is available.")