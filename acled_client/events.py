import re

from acled_client.base_classes import BaseBuilder, BaseQuery, BaseResults
from acled_client.utils import builder

is_8601 = re.compile(r"\d{4}-\d{2}-\d{2}")


class EventQueryBuilder(BaseBuilder):
    def __init__(self):
        self._iso: int = None
        self._year: int = None
        self._event_date = None
        self._event_date_where = None
        self._event_id_cnty = None
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

    @builder
    def event_id_cnty(self, text):
        self._event_id_cnty = text
        self._add_param("_event_id_cnty")


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

    @classmethod
    def event_id_cnty(cls, string) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.event_id_cnty(string)


class EventResults(BaseResults):
    pass
