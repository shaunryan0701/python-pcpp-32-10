from multi_function_device import MFD1, MFD2, MFD3

mfd1 = MFD1()
mfd1.scan_document("document1")
mfd1.get_printer_status()

mfd2 = MFD2()
mfd2.scan_document("document2")
mfd2.get_printer_status()

mfd3 = MFD3()
mfd3.scan_document("document3")
mfd3.get_printer_status()
