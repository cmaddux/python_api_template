"""Command Line Interface for the collections service.

Usage:
    cli.py [fetch] [decrypt] NAME

Options:
    -h --help  Show this screen.
    --version  Show version.

"""

import sys
import iorw
import datasets
import encryption

from docopt import docopt

# Load info about all appropriate datasets into
# memory
dataRepo = datasets.Repository()
dataRepo.loadDatasets('./fixtures/datasets.yaml')

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Collections CLI 0.1')
    if arguments['fetch']:
        datasets.fetch(arguments['NAME'], dataRepo)
    if arguments['decrypt']:
        datasets.decrypt(arguments['NAME'], dataRepo)
