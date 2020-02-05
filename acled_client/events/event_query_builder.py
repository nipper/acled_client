from ..base_classes import BaseBuilder
from ..utils import builder
from ._utils import is_8601, valid_number
from .event_results import EventResults


class EventQueryBuilder(BaseBuilder):
    def __init__(self):
        self.results_class = EventResults
        super().__init__()
        self._valid_parameters = self._valid_parameters + [
            "iso",
            "year",
            "event_date",
            "event_id_cnty",
            "event_date_where",
            "time_precision",
            "event_type",
            "sub_event_type",
            "actor1",
            "assoc_actor_1",
            "inter1",
            "inter2",
            "actor2",
            "assoc_actor_2",
            "interaction",
            "region",
            "country",
            "admin1",
            "admin2",
            "admin3",
            "location",
            "latitude",
            "longitude",
            "geo_precision",
            "source",
            "source_scale",
            "notes",
            "fatalities",
            "iso3",
        ]

    @valid_number
    @builder
    def iso(self, number: int):
        if not isinstance(number, int):
            return ValueError(f"ISO Country must be an integer.")
        self._set_parameter("iso", number)

    @valid_number
    @builder
    def year(self, year):

        if not isinstance(year, int):
            return ValueError(f"Year must be an integer.")
        self._set_parameter("year", year)

    @builder
    def event_date(self, start_date, where=None, end_date=None):

        if not is_8601.match(start_date):
            raise ValueError(f"Start_date must be formatted in 8601 format.")

        if where and where not in ("=", ">", "<", "BETWEEN"):
            raise ValueError(f"event_date_where must be one of: '=','>','<','BETWEEN'")

        if end_date is not None and not is_8601.match(end_date):
            raise ValueError(f"Start_date must be formatted in 8601 format.")

        if end_date:
            self._set_parameter("event_date", f"{{{start_date}|{end_date}}}")
            self._set_parameter("event_date_where", "BETWEEN")
        else:
            where = "%3D" if (where is None or where == "=") else where
            self._set_parameter("event_date", start_date)
            self._set_parameter("event_date_where", where)

    @builder
    def event_id_cnty(self, text):
        self._set_parameter("event_id_cnty", text)

    @valid_number
    @builder
    def time_precision(self, number):

        if number not in (1, 2, 3):
            raise ValueError(f"Time precision can only be 1, 2 or 3. {number} isn't valid.")

        self._set_parameter("time_precision", number)

    @builder
    def event_type(self, event_type):
        self._set_parameter("event_type", event_type)

    @builder
    def sub_event_type(self, sub_event_type):
        self._set_parameter("sub_event_type", sub_event_type)

    @builder
    def actor1(self, actor1):
        self._set_parameter("actor1", actor1)

    @builder
    def assoc_actor_1(self, assoc_actor_1):
        self._set_parameter("assoc_actor_1", assoc_actor_1)

    @valid_number
    @builder
    def inter1(self, inter1):
        self._set_parameter("inter1", inter1)

    @builder
    def actor2(self, actor2):
        self._set_parameter("actor2", actor2)

    @builder
    def assoc_actor_2(self, assoc_actor_2):
        self._set_parameter("assoc_actor_2", assoc_actor_2)

    @valid_number
    @builder
    def inter2(self, inter2):
        self._set_parameter("inter2", inter2)

    @valid_number
    @builder
    def interaction(self, interaction):
        self._set_parameter("interaction", interaction)

    @valid_number
    @builder
    def region(self, region):
        self._set_parameter("region", region)

    @builder
    def country(self, country):
        self._set_parameter("country", country)

    @builder
    def admin1(self, admin1):
        self._set_parameter("admin1", admin1)

    @builder
    def admin2(self, admin2):
        self._set_parameter("admin2", admin2)

    @builder
    def admin3(self, admin3):
        self._set_parameter("admin3", admin3)

    @builder
    def location(self, location):
        self._set_parameter("location", location)

    @builder
    def latitude(self, latitude):
        self._set_parameter("latitude", latitude)

    @builder
    def longitude(self, longitude):
        self._set_parameter("longitude", longitude)

    @builder
    def geo_precision(self, geo_precision):
        self._set_parameter("geo_precision", geo_precision)

    @builder
    def source(self, source):
        self._set_parameter("source", source)

    @builder
    def source_scale(self, source_scale):
        self._set_parameter("source_scale", source_scale)

    @builder
    def notes(self, notes):
        self._set_parameter("notes", notes)

    @builder
    def fatalities(self, fatalities):
        self._set_parameter("fatalities", fatalities)

    @builder
    def iso3(self, iso3):
        self._set_parameter("iso3", iso3)
