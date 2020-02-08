import time
from typing import Generator

import pandas
import requests
import toml

from acled_client.utils import builder


class BaseBuilder:
    def __init__(self):
        self._terms = False
        self._set_params = {}
        self.title = "None"
        self.times_executed = []
        self.url: str = "https://api.acleddata.com/acled/read"
        self._valid_parameters = ["terms", "timestamp"]

    def _set_parameter(self, parameter, value):

        if parameter not in self._valid_parameters:
            raise KeyError(f"{parameter} is not a valid parameter for {self.__class__}")

        self._set_params[parameter] = value

    def _remove_parameter(self, parameter):
        if parameter not in self._valid_parameters:
            raise KeyError(f"{parameter} is not a valid parameter for {self.__class__}")

        try:
            self._set_params.pop(parameter)
            return True
        except KeyError:
            pass

    @builder
    def terms(self, terms):
        self._set_parameter("terms", terms)

    @builder
    def timestamp(self, timestamp):
        self._set_parameter("timestamp", timestamp)

    def to_dict(self):
        return self._set_params

    def execute(self, use_timestamp=False):

        if use_timestamp:
            self.times_executed.append(time.time())
            return self.results_class(self.timestamp(max(self.times_executed)))
        else:
            return self.results_class(self)

    def __str__(self):

        pretty_view: str = ""
        for term in self._set_params:
            pretty_view = pretty_view + f"{term}: {getattr(self, term)} | "

        return pretty_view

    def toml_dump(self):

        base_dict = {"title": self.title, "query_info": {"class": type(self)}, "params": self.to_dict()}

        return toml.dumps(base_dict)

    def toml_dumps(self, file):

        with open(file, "rt") as f:
            f.write(self.toml_dump())


class BaseQuery:

    _builder_class = BaseBuilder

    @classmethod
    def _builder(cls):
        return cls._builder_class()


class BaseResults:
    def __init__(self, query=None):
        self._dtype_lookup = {}

        if self._subclass_dtypes:
            self._dtype_lookup.update(self._subclass_dtypes)

        self.query: BaseQuery = query
        self.query_results: requests.Response = None
        self._query_page: int = 1
        self.string_type = "object"
        self._succesful_query: bool = False
        if query:
            self._execute_query(page=self._query_page)

    def data(self) -> Generator:
        """
        :return: A generator with iterates through the request results.
        """
        while True:
            yield self.query_results.json()["data"]

            if self.query_results.json()["count"] < 500:
                break

            self._execute_query(page=self._query_page)

            self._query_page = self._query_page + 1

    def _execute_query(self, page=1):

        if self.query is None:
            return UnboundLocalError(f"This results object is malformed and missing a query.")

        query_results: requests.Response = requests.get(self.query.url, {**self.query.to_dict(), **{"page": page}})

        if query_results.json()["success"]:
            self._succesful_query = True
            self.query_results = query_results
        else:
            self.query_results = query_results
            pass

    def to_dataframe(self, page: int = 1) -> pandas.DataFrame:
        """
        :param page: The page to start on. Defaults to 1.
        :return: A pandas data frame with all results.
        """
        import pandas

        # Reset the page in case if the generator has been called. Not sure how i want to handle this.
        self._query_page = page

        results = pandas.concat([pandas.DataFrame(x) for x in self.data()])

        results = results.astype(self._dtype_lookup)

        return results
