"""
Honolulu settings for project.

"""

from honolulu.commons import map_routes

# Debug mode set false for production
DEBUG = True

# name of database and another configurations
DATABASE_CONNECTION = {
    'type': 'sqlite',
    'route': 'sqlite:///hawaii.sqlite',
}

# Api mapped routes
API_ROUTES = {
    'root': map_routes('/', 'GET', 'Shows all routes with their respective methods'),
    'get_precipitation': map_routes('/api/v1.0/precipitation', 'GET', 'return all precipitation records from DB'),
    'get_stations': map_routes('/api/v1.0/stations', 'GET', 'return all stations from dataframe'),
    'get_tobs': map_routes('/api/v1.0/tobs', 'GET', 'return measure of temperatures for the last year'),
    'get_temp': map_routes('/api/v1.0/<start_date>', 'GET', 'return average, max and min measure '
                                                            'temperature from date to present'),
    'get_temp_start_end': map_routes('/api/v1.0/<start_date>/<end_date>', 'GET', '''return average, max and min measure 
                                                                            temperature between given two dates '''),
}

