#!/usr/bin/env python

# Third party modules
import click

# First party modules
import ml_alqadi


@click.group()
@click.version_option(version=ml_alqadi.__version__)
def entry_point():
    """Awesomeproject spreads pure awesomeness."""
