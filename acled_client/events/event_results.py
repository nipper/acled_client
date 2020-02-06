from ..base_classes import BaseResults


class EventResults(BaseResults):


    def __init__(self,query = None):

        self._subclass_dtypes = {
            "data_id": "int64",
            "inter1": "int8",
            "inter2": "int8",
            "iso": "int16",
            "event_date": "datetime64",
        }

        super().__init__(query)
