import acled_client.events
import pytest


@pytest.fixture
def querybuilder():
    import acled_client.events

    return acled_client.events.EventQuery.iso(1).terms("accept").event_id_cnty("TEST1234")


def test_querybuilder(querybuilder):
    assert type(querybuilder) is acled_client.events.EventQueryBuilder


def test_not_inplace(querybuilder):
    new_builder = querybuilder.iso(42, in_place=False)
    assert querybuilder != new_builder


def test_in_place(querybuilder):
    new_builder = querybuilder.iso(42, in_place=True)
    assert querybuilder == new_builder
