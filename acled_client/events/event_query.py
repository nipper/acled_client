from ..base_classes import BaseQuery
from .event_query_builder import EventQueryBuilder


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
