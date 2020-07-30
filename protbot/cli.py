#!/usr/bin/env python3
from .config import auth
__doc__ = """Run protbot
Usage:
    protbot [options]
    protbot run [options]

Options:
    -h --help                       show this

    --hypothesis-group-name=NAME    the hypotheis group name [default: auth.get('hypothesis-group')]

"""

from pyontutils import clifun as clif
from .core import run
from .utils import log, logd


class Options(clif.Options):
    pass


class Main(clif.Dispatcher):

    def default(self):
        pass

    def run(self):
        log.info('running')
        run(group=self.options.hypothesis_group_name)
        log.info('done')


def main():
    from . import __version__
    options, *ad = Options.setup(__doc__, version=f'protbot {__version__}')

    main = Main(options)
    if main.options.debug:
        print(main.options)

    main()


if __name__ == '__main__':
    main()
