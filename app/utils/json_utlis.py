import json
from copy import deepcopy
from datetime import datetime
from sqlalchemy.ext.declarative import DeclarativeMeta


class JsonUtils():
    def __init__(self, data={}, code=0, msg="", url="", token=""):
        self.data = data
        self.code = code
        self.msg = msg
        self.url = url
        self.token = token

        self.json = {
            "data": data,
            "code": code,
            "msg": msg,
            "url": url,
            "token": token
        }

    def get_json(self):
        try:
            return json.dumps(self.json)
        except:
            return json.dumps(self.json, cls=new_alchemy_encoder(), check_circular=False)


def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj.__class__, DeclarativeMeta):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    data = obj.__getattribute__(field)
                    try:
                        if isinstance(data, datetime):
                            data = data.strftime('%Y-%m-%d %H:%M:%S')
                        json.dumps(data)  # this will fail on non-encodable values, like other classes
                        fields[field] = data
                    except TypeError:
                        fields[field] = None
                return fields

            return json.JSONEncoder.default(self, obj)

    return AlchemyEncoder


if __name__ == "__main__":
    data = JsonUtils(msg="123").get_json()
    #
