class Scanner:
    def scan(self):
        print('scan() method from the scanner class')
        
class Printer:
    def print(self):
        print('print() method from the scanner class')
        
class Fax:
    def send(self):
        print('send() method from the fax class')
        
    def print(self):
        print('print() method from the fax class')
        
class MFD_SPF(Scanner, Printer, Fax):
    pass

class MFD_SFP(Scanner, Fax, Printer):
    pass

spf = MFD_SPF()

sfp = MFD_SFP()

spf.scan()
sfp.scan()

spf.print()
sfp.print()

spf.send()
sfp.send()