"""
    This module implements queries created with sqlAlchemy.

"""

import logging
from datetime import datetime
import dateutil.relativedelta
from sqlalchemy import func
from honolulu.dbResources.models import  Measurement
from honolulu.db import db_connection


def get_count(table_value):
    """
    Parameters
    ----------
        table_value: table from Sqlalchemy model.
            Model from Sqlalchemy table and module in
            format 'module.table'.
    Returns
    -------
        Int: with count of all rows from the 'module.table'.
    """
    try:
        return db_connection()[1].query(table_value).count()

    except Exception as exc:
        logging.warning(exc)


def get_groupBy(table_value):
    """
    Parameters
    ----------
        table_value: table from Sqlalchemy model.
            Model from Sqlalchemy table and module
            in format 'module.table'.
    Returns
    -------
        Int: with count of all rows from the 'module.table'.
    """
    try:
        return db_connection()[1].query(func.row_number()
                                        .over(order_by=func.count(table_value).label(str(table_value)+'_numb').desc())
                                        .label("row_number"),
                                        table_value,
                                        func.count(table_value) \
                                        .label(str(table_value)+'_numb')).group_by(table_value).all()

    except Exception as exc:
        logging.warning(exc)


def get_measurement_date_partitioned_from(column: str = None,
                                          end_date: str = None,
                                          months_to_decrease: int = None):
    """
    Parameters
    ----------
        column: str
            set 'tobs' or 'prcp' column.
        end_date: str
            determine the final date to get data.
        months_to_decrease: Int
            number of months to calculate from which
            date do filter.
    Returns
    -------
        list: with the values of the query
    """

    try:
        source_dict = {'prcp': Measurement.prcp,
                       'tobs': Measurement.tobs}

        if column is None or column not in source_dict:
            return [('error', 'column error')]

        table_lable = source_dict[column]
        lable_name = column

        trfm_date = datetime.strptime(end_date, "%Y-%m-%d")
        start_date = trfm_date - dateutil.relativedelta.relativedelta(months=months_to_decrease)

        return db_connection()[1].query(Measurement.date.label('date'),
                                        table_lable.label(str(lable_name))) \
            .filter(Measurement.date > start_date.strftime("%Y-%m-%d"),
                    Measurement.date < end_date) \
            .order_by(table_lable.label(str(lable_name)).desc()).all()

    except Exception as exc:
        logging.info(exc)


def get_measurement_all_from(column: str = None):
    """
    Parameters
    ----------
        column: str
            set 'tobs' or 'prcp' column.
    Returns
    -------
        list: with the values of the query
    """
    try:
        source_dict = {'prcp': Measurement.prcp,
                       'tobs': Measurement.tobs}

        if column is None or column not in source_dict:
            return [('error', 'column error')]

        table_lable = source_dict[column]
        lable_name = column

        return db_connection()[1].query(Measurement.date.label('date'),
                                        table_lable.label(str(lable_name))) \
            .order_by(table_lable.label(str(lable_name)).desc()).all()

    except Exception as exc:
        logging.warning(exc)


def get_measurement_max_date():
    """
    Returns
    -------
        str: max date in the table Measurement
    """
    return list(db_connection()[1].query(func.max(Measurement.date)).all())[0][0]


def get_measurement_date_partitioned_tobs(start_date, end_date=None):
    """
    Parameters
    ----------
        start_date: str
            determine the start date to get data.
        end_date: str
            determine the final date to get data.
    Returns
    -------
        list: with the values of the query
    """
    try:

        if end_date is None:
            actual_date = datetime.now()
            end_date = actual_date.strftime("%Y-%m-%d")

        return db_connection()[1].query(Measurement.date.label('date'),
                                        Measurement.tobs.label(str('tobs'))) \
            .filter(Measurement.date > start_date,
                    Measurement.date < end_date) \
            .order_by(Measurement.tobs.label(str('tobs')).desc()).all()

    except Exception as exc:
        logging.warning(exc)
