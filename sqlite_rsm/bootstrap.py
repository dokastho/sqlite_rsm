import click
import requests


@click.command()
@click.argument('mode', type=click.STRING)
def main(mode: str):
    """Run sqlite rsm with mode 'node' or 'viewer'."""
    
    if mode == "viewer":
        # start viewer
        pass        
        # requests.post()...
        
        
    elif mode == "node":
        pass
    else:
        print("Undefined mode.")

if __name__ == "__main__":
    # Click will provide the arguments, disable this pylint check.
    # pylint: disable=no-value-for-parameter
    main()