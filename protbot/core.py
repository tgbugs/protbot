from hyputils.subscribe import setup_websocket
from .config import auth
from .utils import log


def run(group=None):
    if group is None:
        group = auth.get('hypothesis-group')

    log.info('TODO')
