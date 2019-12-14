import argparse

def parse_input():
    """ Argument parsing function """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", type=str, default="0.0.0.0",
                        help="ip address of the device")
    parser.add_argument("-o", "--port", type=int, default=8000,
                        help="ephemeral port number of the server (1024 to 65535)")
    return parser.parse_args()
