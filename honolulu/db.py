from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from honolulu.settings import DATABASE_CONNECTION


def db_connection(data_base=DATABASE_CONNECTION['route']):
    """Creation of the DB connection.
    Parameters
    ----------
        data_base: str
            sqlite Database location as String.
    Returns
    -------
         tuple:
            base 'automap_base' object.
            session 'create_engine' for create a new format ,
            engine :class: 'Session' creation of DB session .
    """
    base = automap_base()
    engine = create_engine(data_base)
    session = Session(engine)

    return base, session, engine