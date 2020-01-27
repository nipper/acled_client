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
        self._valid_parameters = self._valid_parameters + ["iso", "year", "event_date", "event_id_cnty"]

    @builder
    def iso(self, number: int):
        if not isinstance(number, int):
            return ValueError(f"ISO Country must be an integer.")
        self._set_parameter("iso", number)

    @builder
    def year(self, year):

        if not isinstance(year, int):
            return ValueError(f"Year must be an integer.")
        self._set_parameter("year", year)

    @builder
    def event_date(self, start_date, end_date=None):

        if not is_8601.match(start_date):
            raise ValueError(f"Start_date must be formatted in 8601 format.")

        if end_date is not None and not is_8601.match(end_date):
            raise ValueError(f"Start_date must be formatted in 8601 format.")

        if end_date is None:
            self._set_parameter("event_date", start_date)
            self._remove_parameter("event_date_where")
        else:
            self._set_parameter("event_date", f"{{{start_date}|{end_date}}}")
            self._set_parameter("event_date_where", "BETWEEN")

    @builder
    def event_id_cnty(self, text):
        self._set_parameter("event_id_cnty", text)

    @builder
    def time_precision(self, number):

        if number not in (1, 2, 3):
            raise ValueError(f"Time precision can only be 1, 2 or 3. {number} isn't valid.")


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

    @classmethod
    def event_id_no_cnty(cls, string) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.event_id_no_cnty(string)

    @classmethod
    def time_precision(cls, number) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.time_precision(number)

    @classmethod
    def event_type(cls, string) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.event_type(string)

    @classmethod
    def sub_event_type(cls, string) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.sub_event_type(string)

    @classmethod
    def actor1(cls, actor) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.actor1(actor)

    @classmethod
    def assoc_actor_1(cls, assoc_actor_1) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.assoc_actor_1(assoc_actor_1)

    @classmethod
    def inter1(cls, inter1) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.inter1(inter1)

    @classmethod
    def actor2(cls, actor2) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.actor2(actor2)

    @classmethod
    def assoc_actor_2(cls, assoc_actor_2) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.assoc_actor_2(assoc_actor_2)

    @classmethod
    def inter2(cls, inter2) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.inter2(inter2)

    @classmethod
    def interaction(cls, interaction) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.interaction(interaction)

    @classmethod
    def region(cls, region) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.region(region)

    @classmethod
    def country(cls, country) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.country(country)

    @classmethod
    def admin1(cls, admin1) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.admin1(admin1)

    @classmethod
    def admin2(cls, admin2) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.admin2(admin2)

    @classmethod
    def admin3(cls, admin3) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.admin3(admin3)

    @classmethod
    def location(cls, location) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.location(location)

    @classmethod
    def latitude(cls, latitude) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.latitude(latitude)

    @classmethod
    def longitude(cls, longitude) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.longitude(longitude)

    @classmethod
    def geo_precision(cls, geo_precision) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.geo_precision(geo_precision)

    @classmethod
    def source(cls, source) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.source(source)

    @classmethod
    def source_scale(cls, source_scale) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.source_scale(source_scale)

    @classmethod
    def notes(cls, notes) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.notes(notes)

    @classmethod
    def fatalities(cls, fatalities) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.fatalities(fatalities)

    @classmethod
    def timestamp(cls, timestamp) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.timestamp(timestamp)

    @classmethod
    def iso3(cls, iso3) -> EventQueryBuilder:
        querybuilder = cls._builder()

        return querybuilder.iso3(iso3)


class EventResults(BaseResults):
    pass
