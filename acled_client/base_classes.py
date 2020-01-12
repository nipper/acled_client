from acled_client.utils import builder
from typing import Generator

import requests
import pandas

class BaseBuilder:

    def __init__(self):
        self._terms = False
        self._set_params = []
        self.url: str = "https://api.acleddata.com/acled/read"

    def _add_param(self, item):
        if item not in self._set_params:
            self._set_params.append(item)

    def _remove_param(self, item):
        if item in self._set_params:
            self._set_params.remove(item)

    @builder
    def terms(self, terms):
        self._terms = terms
        self._add_param("_terms")

    def to_dict(self):
        return {key[1:]: getattr(self, key) for key in self._set_params}

    def to_url_parms(self):
        params_string = [f"{k}={v}" for (k, v) in self.to_dict().items()]
        return "&".join(params_string)

    def execute(self):
        return self.results_class(self)

    def __str__(self):

        pretty_view = ""
        for term in self._set_params:
            pretty_view = pretty_view + f"{term}: {getattr(self, term)} | "

        return pretty_view


class BaseQuery:

    _builder_class = BaseBuilder

    @classmethod
    def _builder(cls):
        return cls._builder_class()


class BaseResults:

    def __init__(self,query = None):
        self.query = query
        self.query_results: requests.Response = None
        self.query_page: int = 1

        self._execute_query(page=self.query_page)

    def data(self) -> Generator:
        """
        :return: A generator with iterates through the request results.
        """
        while True:
            yield self.query_results.json()["data"]

            if self.query_results.json()["count"] < 500:
                break

            self._execute_query(page=self.query_page)

            self.query_page = self.query_page + 1

    def _execute_query(self, page=1):

        if self.query is None:
            return UnboundLocalError(
                f"This results object is malformed and missing a query."
            )

        self.query_results: requests.Response = requests.get(
            self.query.url, {**self.query.to_dict(), **{"page": page}}
        )

    def to_dataframe(self, page: int = 1) -> pandas.DataFrame:
        """
        :param page: The page to start on. Defaults to 1.
        :return: A pandas data frame with all results.
        """
        # Reset the page in case if the generator has been called. Not sure how i want to handle this.
        self.query_page = page

        return pandas.concat(pandas.DataFrame(x) for x in self.data())
