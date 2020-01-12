import re
import acled_client.results
from acled_client.utils import builder

is_8601 = re.compile(r"\d{4}-\d{2}-\d{2}")


class QueryBuilder:
    def __init__(self):

        self._iso: int = None
        self._year: int = None
        self._set_params = []
        self._event_date = None
        self._event_date_where = None
        self._terms = False
        self.url: str = "https://api.acleddata.com/acled/read"

    def _add_term(self, item):
        if item not in self._set_params:
            self._set_params.append(item)

    def _remove_term(self, item):
        if item in self._set_params:
            self._set_params.remove(item)

    @builder
    def terms(self, terms):
        self._terms = terms
        self._add_term("_terms")

    @builder
    def iso(self, number: int):
        if not isinstance(number, int):
            return ValueError(f"ISO Country must be an integer.")
        self._iso = number
        self._add_term("_iso")

    @builder
    def year(self, year):

        if not isinstance(year, int):
            return ValueError(f"Year Country must be an integer.")

        self._year = year
        self._add_term("_year")

    @builder
    def event_date(self, start_date, end_date=None):

        if not is_8601.match(start_date):
            return ValueError(f"Start_date must be formated in 8601 format.")

        if end_date is not None and not is_8601.match(end_date):
            return ValueError(f"Start_date must be formated in 8601 format.")

        if end_date is None:
            self._event_date = start_date
            self._event_date_where = None

            self._remove_term("_event_date_where")
            self._add_term("_event_date")
        else:
            self._event_date = f"{{{start_date}|{end_date}}}"
            self._event_date_where = "BETWEEN"

            self._add_term("_event_date_where")
            self._add_term("_event_date")

    def execute(self):
        return acled_client.results.EventResults(self)

    def to_dict(self):
        return {key[1:]: getattr(self, key) for key in self._set_params}

    def to_url_parms(self):
        params_string = [f"{k}={v}" for (k, v) in self.to_dict().items()]
        return "&".join(params_string)

    def __str__(self):

        pretty_view = ""
        for term in self._set_params:
            pretty_view = pretty_view + f"{term}: {getattr(self,term)} | "

        return pretty_view


class Query:
    @classmethod
    def _builder(cls):
        return QueryBuilder()

    @classmethod
    def iso(cls, number) -> QueryBuilder:
        querybuilder = cls._builder()
        return querybuilder.iso(number)

    @classmethod
    def year(cls, year) -> QueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.year(year)

    @classmethod
    def event_date(cls, start_date, end_date=None) -> QueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.event_date(start_date, end_date)
