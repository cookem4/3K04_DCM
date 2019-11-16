import threading

basic_thread: threading.Thread
egm_thread: threading.Thread

# The goal here is to have a serial port that uses one thread to constantly listen for egm data
# this thread is stopped when others need the serial port and continued

listening_for_egm = False

