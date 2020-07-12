"""common functions
"""


def map_routes(route: str = None, method: str = None, desc: str = None):
    """ return dict with values of routes
    Parameters
    ----------
        route: str
            api route start with /.
        method: str
            method GET, POST, DELETE
        desc: str
            text to describe the api route
    Returns
    -------
        dict: with the given values.
    """
    return {'route': route,
            'method': method,
            'description': desc}