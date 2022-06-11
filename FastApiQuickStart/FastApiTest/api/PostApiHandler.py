from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

sample_data = [
    {'first_name': "James", 'last_name': "Felton"},
    {'first_name': "Ameesh", 'last_name': "Kapoor"},
    {'first_name': "Jim", 'last_name': "Saxton"},
    {'first_name': "Eric", 'last_name': "Walden"},
    {'first_name': "Nick", 'last_name': "Roman"},
    {'first_name': "Chen", 'last_name': "Liu"}
]


def query_request_handler(query_dict):
    '''
    :param
        query_dict: {
              "filterName": "string",
              "filterValue": "string",
              "recordsLimit": 0
            }
    :return:
        JSON Result
    '''
    filter_name = None
    filter_value = None
    limit_records = 10
    result_json = []
    for key, value in query_dict.items():
        if key == 'filterName':
            if value in ['first_name', 'last_name']:
                filter_name = value
        elif key == 'filterValue':
            filter_value = value
        elif key == 'recordsLimit':
            limit_records = value

    if None not in [filter_name, filter_value]:
        result_json = [item for item in sample_data
                       if item[filter_name].find(filter_value) >= 0]

    if 0 < limit_records < len(result_json):
        result_json = result_json[:limit_records]

    return {'postResult': True, 'postMessage': result_json}


class PostApiQuery(BaseModel):
    '''

    '''
    filterName: str
    filterValue: str
    recordsLimit: int


def get_query_response(query):
    query_dict = jsonable_encoder(query)
    return query_request_handler(query_dict)
