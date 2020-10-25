"""
This a easy package to send and recieve email with the terminal, just in development, not support send too complex messages
"""
import sys
try:
    import click
except Exception as e:
    import logging
    logging.critical('You must installed click to use the sdml module')
    sys.exit(1)

import hy as _hy
from .sdml import easy_mail_sender, Message, Connect
