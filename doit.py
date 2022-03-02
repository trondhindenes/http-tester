import requests
import typer
from rich.console import Console
from datetime import datetime
from time import sleep



console = Console()

FAILURE_COUNT=0

s = requests.Session()


def main(url: str, wait_secs: float = 1.0):
    global FAILURE_COUNT
    while True:
        response = None
        now = datetime.utcnow()
        try:
            response = s.get(url)
        except Exception:
            pass
        
        style = None
        status_code = None
        if response and hasattr(response, "status_code") and response.status_code > 399:
            status_code = response.status_code
            FAILURE_COUNT += 1
            style = "bold red"
        elif response:
            status_code = response.status_code
        else:
            FAILURE_COUNT += 1
            style = "bold red"
        console.print(f"{now} status code was {status_code} failure count: {FAILURE_COUNT}", style=style)
        if wait_secs > 0.0:
            sleep(wait_secs)

if __name__ == "__main__":
    typer.run(main)