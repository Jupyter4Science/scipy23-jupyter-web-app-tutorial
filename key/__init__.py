from .dashboard.helpers import answer

def load_ipython_extension(ipython):
    ipython.register_magics(answer)