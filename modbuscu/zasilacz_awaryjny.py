from modbuscu.modbus_slave import ModbusSlave

class ZasilaczAwaryjny(ModbusSlave):
    def __init__(self, server, address):
        self.adres = address
        super().__init__(server, self.adres)