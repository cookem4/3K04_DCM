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
            if callable(x) and hasattr(self.oInstance, 'run_serial_decorator') and x.__name__ != "function_to_ignore":
                return self.serial_safe(x)
            else:
                return x

        def serial_safe(self, serial_using_function):
            def new_function(*args, **kwargs):
                self.oInstance.time_since_last_call = datetime.now()
                output = None
                try:
                    self.oInstance.open()
                    output = serial_using_function(*args, **kwargs)
                    self.oInstance.close()
                except (SerialException, SerialTimeoutException, Exception) as e:
                    self.oInstance.close()
                    print(e)
                return output

            return new_function

    return DecoratorClass


def serial_ignore(func):
    def function_to_ignore(*args, **kwargs):
        return func(*args, **kwargs)

    return function_to_ignore
