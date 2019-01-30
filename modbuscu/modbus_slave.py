import functools
import logging
import modbus_tk.defines as cst

def check_range(min, max, critical):
    def decorator(f):
        @functools.wraps(f)
        def wrap(self, *args):
            if args[-1] not in range(min, max+1):
                msg = f'Wartość parametru {self.__class__.__name__}.{f.__name__} ({args[-1]}) jest spoza dozwolonego zakresu {min}-{max}'
                if critical:
                    logging.error(msg, exc_info=False)
                    raise ValueError(msg)
                else:
                    logging.warning(msg, exc_info=False)
                return
            return f(self, *args)
        return wrap
    return decorator

class Coil:
    def __init__(self, name, address, write_access=True):
        self.name = name
        self.address = address
        self.write_access = write_access

    def __get__(self, instance, owner):
        return instance.device.get_values(self.name, self.address, 1)[0]

    @check_range(0, 1, False)
    def __set__(self, instance, value):
        if not self.write_access:
            return
        instance.device.set_values(self.name, self.address, value)

class InputRegister:
    def __init__(self, name, address, device, length=1):
        self.name = name
        self.address = address
        self.length = length
        device.add_block(name, cst.READ_INPUT_REGISTERS, address, self.length)

    def __get__(self, instance, owner):
        return instance.device.get_values(self.name, self.address, self.length)

    def __set__(self, instance, value):
        raise NotImplemented(f'{self.name} input register jest read only')

class ModbusSlave:
    def __init__(self, server, address):
        self.device = server.add_slave(address)

    @property
    def adres(self):
        return self.adress

    @adres.setter
    @check_range(1, 247, True)
    def adres(self, adres):
        self.adress = adres