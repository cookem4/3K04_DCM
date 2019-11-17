from datetime import datetime

from serial import SerialException, SerialTimeoutException

from main.communication import SerialBase


def serial_safe_methods(serial_using_class: SerialBase):
    class DecoratorClass(object):
        def __init__(self, *args, **kwargs):
            self.oInstance: SerialBase = serial_using_class(*args, **kwargs)

        def __getattribute__(self, item):
            try:
                x = super(DecoratorClass, self).__getattribute__(item)
                return x
            except AttributeError:
                pass

            x = self.oInstance.__getattribute__(item)
            if callable(x) and hasattr(self.oInstance, 'run_serial_decorator'):
                if x.__name__ == "dont_close_serial":
                    return self.open_serial_before(x)
                else:
                    return self.close_serial_after(self.open_serial_before(x))
            else:
                return x

        def open_serial_before(self, serial_using_function):
            def new_function(*args, **kwargs):
                self.oInstance.time_since_last_call = datetime.now()
                self.oInstance.open()
                return serial_using_function(*args, **kwargs)

            return new_function

        def close_serial_after(self, serial_using_function):
            def new_function(*args, **kwargs):
                try:
                    output = serial_using_function(*args, **kwargs)
                    self.oInstance.close()
                except (SerialException, SerialTimeoutException, Exception) as e:
                    self.oInstance.close()
                    print(e)
                return output

            return new_function

    return DecoratorClass


def leave_serial_open(func):
    def dont_close_serial(*args, **kwargs):
        return func(*args, **kwargs)

    return dont_close_serial
