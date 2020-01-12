import re
from typing import Generator

import pandas
import requests

from acled_client.base_classes import BaseBuilder,BaseQuery
from acled_client.utils import builder

is_8601 = re.compile(r"\d{4}-\d{2}-\d{2}")

class EventQueryBuilder(BaseBuilder):

    def __init__(self):
        self._iso: int = None
        self._year: int = None
        self._event_date = None
        self._event_date_where = None
        self.results_class = EventResults

        super().__init__()

    @builder
    def iso(self, number: int):
        if not isinstance(number, int):
            return ValueError(f"ISO Country must be an integer.")
        self._iso = number
        self._add_param("_iso")

    @builder
    def year(self, year):

        if not isinstance(year, int):
            return ValueError(f"Year must be an integer.")

        self._year = year
        self._add_param("_year")

    @builder
    def event_date(self, start_date, end_date=None):

        if not is_8601.match(start_date):
            return ValueError(f"Start_date must be formated in 8601 format.")

        if end_date is not None and not is_8601.match(end_date):
            return ValueError(f"Start_date must be formated in 8601 format.")

        if end_date is None:
            self._event_date = start_date
            self._event_date_where = None

            self._remove_param("_event_date_where")
            self._add_param("_event_date")
        else:
            self._event_date = f"{{{start_date}|{end_date}}}"
            self._event_date_where = "BETWEEN"

            self._add_param("_event_date_where")
            self._add_param("_event_date")


class EventQuery(BaseQuery):

    _builder_class = EventQueryBuilder

    @classmethod
    def iso(cls, number) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.iso(number)

    @classmethod
    def year(cls, year) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.year(year)

    @classmethod
    def event_date(cls, start_date, end_date=None) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.event_date(start_date, end_date)


class EventResults:
    def __init__(self, query=None):
        self.query = query
        self.query_results: requests.Response = None
        self.query_page: int = 1

        # Executes the query populating the initial results
        self._execute_query(page=self.query_page)

    def _execute_query(self, page=1):

        if self.query is None:
            return UnboundLocalError(
                f"This results object is malformed and missing a query."
            )

        self.query_results: requests.Response = requests.get(
            self.query.url, {**self.query.to_dict(), **{"page": page}}
        )

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

    def to_dataframe(self, page: int = 1) -> pandas.DataFrame:
        """
        :param page: The page to start on. Defaults to 1.
        :return: A pandas data frame with all results.
        """
        # Reset the page in case if the generator has been called. Not sure how i want to handle this.
        self.query_page = page

        return pandas.concat(pandas.DataFrame(x) for x in self.data())
