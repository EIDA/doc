#!/usr/bin/env python3
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "jinja2>=3.1.6",
# ]
# ///

# Generate a documentation template for a given service
#

import jinja2

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(autoescape=select_autoescape())

# TODO generate all the documentation to a given target directory
# TODO set options to get the author, the service and render the templates accordingly
