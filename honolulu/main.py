from flask import Flask
from flask import jsonify
from honolulu.dbResources.queries import (get_measurement_all_from,
                                          get_groupBy,
                                          get_measurement_date_partitioned_from,
                                          get_measurement_max_date,
                                          get_measurement_date_partitioned_tobs)
from honolulu.dbResources.dataframe import HonoluluDf
from honolulu.dbResources.models import  Measurement, Station
from honolulu.settings import API_ROUTES, DEBUG


app = Flask(__name__)


@app.route(API_ROUTES['root']['route'], methods=[API_ROUTES['root']['method']])
def get_all_routes():
    return jsonify(API_ROUTES)


@app.route(API_ROUTES['get_precipitation']['route'], methods=[API_ROUTES['get_precipitation']['method']])
def get_precipitation():
    prcp_result = get_measurement_all_from(column='prcp')
    return jsonify(dict(prcp_result))


@app.route(API_ROUTES['get_stations']['route'], methods=[API_ROUTES['get_stations']['method']])
def get_stations():
    stations_query = get_groupBy(Station.station)
    stations_df = HonoluluDf(stations_query, 'station', Measurement.prcp)
    return jsonify(stations_df.get_df().to_dict(orient='records'))


@app.route(API_ROUTES['get_tobs']['route'], methods=[API_ROUTES['get_tobs']['method']])
def get_tobs():
    max_date_result = get_measurement_max_date()
    tobs_result = get_measurement_date_partitioned_from(column='tobs',
                                                        end_date=max_date_result,
                                                        months_to_decrease=12)
    return jsonify(dict(tobs_result))


@app.route(API_ROUTES['get_temp']['route'], methods=[API_ROUTES['get_temp']['method']])
def get_temp(start_date):
    tobs_result = get_measurement_date_partitioned_tobs(start_date=start_date)
    return jsonify(dict(tobs_result))


@app.route(API_ROUTES['get_temp_start_end']['route'], methods=[API_ROUTES['get_temp_start_end']['method']])
def get_temp_start_end(start_date, end_date):
    COLUMN = 'tobs'
    tobs_result = get_measurement_date_partitioned_tobs(start_date=start_date,
                                                        end_date=end_date)
    stations_df = HonoluluDf(tobs_result, 'date', COLUMN)

    tobs_dict = {'min_temp': stations_df.get_df().min()[COLUMN],
                 'avg_temp': stations_df.get_df().mean()[COLUMN],
                 'max_temp': stations_df.get_df().max()[COLUMN]}

    return jsonify(tobs_dict)


if __name__ == '__main__':
    app.run(debug=DEBUG)

