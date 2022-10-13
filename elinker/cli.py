import typer
import yaml

from pathlib import Path
from importlib import resources
from typing import Optional
from rich.console import Console

from elinker import data

__app_name__ = "elinker"
__version__ = "0.1.0"

app = typer.Typer()
console = Console()

# APP_DIR_PATH = Path(typer.get_app_dir(__app_name__))
with resources.path(data, "config.yml") as path:
    CONFIG_FILE_PATH = Path(path)
    CONFIG_FILE_PATH.touch(exist_ok=True)

with open(CONFIG_FILE_PATH) as conf_file:
    print(f"CONFIG_FILE_PATH: {CONFIG_FILE_PATH}")
    CONFIG = yaml.load(conf_file, Loader=yaml.FullLoader)
    CONFIG = CONFIG if CONFIG else {}


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"version: {__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> Optional[bool]:
    return version


@app.command()
def config(
    key: Optional[str] = typer.Option(
        None,
        "--key",
        "-k",
        help="Set the key",
    ),
    value: Optional[str] = typer.Option(
        None,
        "--value",
        "-w",
        help="Set the value",
    ),
    clear: Optional[bool] = typer.Option(
        None,
        "--clear",
        "-c",
        help="Clear all values",
    ),
) -> None:
    global CONFIG
    if clear and key is None:
        CONFIG = {}
    elif clear:
        CONFIG.pop(key, None)
    elif key is not None:
        CONFIG[key] = value
    CONFIG_FILE_PATH.write_text(yaml.dump(CONFIG))
    console.print(f"CURRENT CONFIG SETTINGS: {CONFIG}")
