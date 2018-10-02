#!/usr/bin/env python3

from time import sleep

from padawan import Padawan

if __name__ == "__main__":
    app = Padawan()
    app.start()

    try:
        while 1:
            sleep(0.1)
    except KeyboardInterrupt:
        pass
    finally:
        app.stop()
