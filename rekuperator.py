import sys
import modbus_slave
import modbus_tk
import logging
from modbus_tk import modbus_rtu
import modbus_tk.defines as cst
import serial
import time
PORT = 'COM11'

class Rekuperator(modbus_slave.ModbusSlave):
    def __init__(self, server,address=1):
        self.adres = address
        super().__init__(server, self.adres)
        self.device.add_block('wietrzenie', cst.COILS, 0, 1)

    wietrzenie = modbus_slave.Coil('wietrzenie', 0)

class ZasilaczAwaryjny(modbus_slave.ModbusSlave):
    def __init__(self, server, address):
        self.adres = address
        super().__init__(server, self.adres)

if __name__ == "__main__":

    logging.basicConfig(filename='error.log',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        level=logging.DEBUG)
    try:
        server = modbus_rtu.RtuServer(serial.Serial(PORT))
    except serial.serialutil.SerialException:
        logging.error(f'Wybrany port szeregowy {PORT} nie jest dostępny', exc_info=False)
        raise ValueError('Wybrany port szeregowy nie jest dostępny')
    server.start()
    rekuperator = Rekuperator(server=server)
    print(rekuperator.wietrzenie)
    rekuperator.wietrzenie = 1
    print(rekuperator.wietrzenie)
   # time.sleep(10)
    rekuperator.wietrzenie = 0
    print(rekuperator.wietrzenie)
    rekuperator.wietrzenie = -1
    #zasilacz = ZasilaczAwaryjny(server=server, address=400)
    server.stop()