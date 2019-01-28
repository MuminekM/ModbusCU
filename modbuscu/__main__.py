PORT = 'COM11'
import logging
from modbuscu.rekuperator import Rekuperator
from modbuscu.zasilacz_awaryjny import ZasilaczAwaryjny
from modbus_tk import modbus_rtu
import serial

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
    time.sleep(10)
    rekuperator.wietrzenie = 0
    print(rekuperator.wietrzenie)
    rekuperator.wietrzenie = -1
    #zasilacz = zasilacz_awaryjny.ZasilaczAwaryjny(server=server, address=400)
    server.stop()