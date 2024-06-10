from lib763.multp import start_process
from lib763.Bash import Bash
from lib763.macro import get_all_window_names, activate_window, maximize_window
from common.CONST import DEVICE_NAME,SCRCPY_PATH
import time


def __execute_scrcpy():
    bash = Bash()
    bash.execute(f"cd {SCRCPY_PATH} & scrcpy.exe ")


def start_scrcpy():
    start_process(__execute_scrcpy)
    while True:
        time.sleep(1)
        if DEVICE_NAME in get_all_window_names():
            break
    activate_window(DEVICE_NAME)
    maximize_window(DEVICE_NAME)
