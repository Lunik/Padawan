#!/usr/bin/env python3

from time import sleep

from padawanv6 import PadawanV6

if __name__ == "__main__":
    app = PadawanV6()
    app.start()

    try:
        while 1:
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        app.stop()
