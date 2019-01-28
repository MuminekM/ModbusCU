import logging
from modbuscu.rekuperator import Rekuperator
from modbuscu.zasilacz_awaryjny import ZasilaczAwaryjny
from modbus_tk import modbus_rtu
import serial
import sys

if __name__ == "__main__":

    if len(sys.argv)>1:
        port = sys.argv[1]
    else:
        port = 'COM11'

    logging.basicConfig(filename='error.log',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        level=logging.DEBUG)
    try:
        server = modbus_rtu.RtuServer(serial.Serial(port))
    except Exception as e:
        print(e)
        logging.error(f'Wybrany port szeregowy {port} nie jest dostępny', exc_info=False)
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