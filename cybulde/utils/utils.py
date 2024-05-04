import socket
import logging
import subprocess
logging.basicConfig(level=logging.NOTSET)


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(f"[{socket.gethostname()}] {name}")
    return logger

def run_shell_command(cmd: str) -> str:
    return subprocess.run(cmd, text=True, shell=True, check=True, capture_output=True).stdout