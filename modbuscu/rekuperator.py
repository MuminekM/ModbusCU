from modbuscu.modbus_slave import ModbusSlave, Coil, InputRegister
import modbus_tk.defines as cst


class Rekuperator(ModbusSlave):
    def __init__(self, server,address=1):
        self.adres = address
        super().__init__(server, self.adres)
        self.device.add_block('wietrzenie', cst.COILS, 0, 1)
        self.device.add_block('godzina', cst.HOLDING_REGISTERS, 80, 1)

    wietrzenie = Coil('wietrzenie', 0)
    godzina = InputRegister('godzina', 80)
