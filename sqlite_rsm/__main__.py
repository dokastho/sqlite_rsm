import click
import sqlite_rsm


@click.command()
@click.argument('mode', type=click.STRING)
def main(mode: str):
    """Run sqlite rsm with mode 'node' or 'viewer'."""

    if mode == "viewer":
        # start viewer
        sqlite_rsm.Viewer()

    elif mode == "node":
        sqlite_rsm.Node()
        pass
    else:
        print("Undefined mode.")


if __name__ == "__main__":
    # Click will provide the arguments, disable this pylint check.
    # pylint: disable=no-value-for-parameter
    main()
