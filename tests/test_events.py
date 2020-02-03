import pytest

import acled_client.events


@pytest.fixture
def querybuilder() -> acled_client.events.EventQueryBuilder:
    import acled_client.events
    query: acled_client.acled_client.events =  acled_client.events.EventQuery.iso(1).terms("accept").event_id_cnty("TEST1234")
    return query

def test_querybuilder(querybuilder):
    assert type(querybuilder) is acled_client.events.EventQueryBuilder


def test_not_inplace(querybuilder):
    new_builder = querybuilder.iso(42, in_place=False)
    assert querybuilder != new_builder


def test_in_place(querybuilder):
    new_builder = querybuilder.iso(42, in_place=True)
    assert querybuilder == new_builder

def test_time_precision_error(querybuilder):
    with pytest.raises(ValueError):
        assert querybuilder.time_precision(4)

def test_time_precision_valid_value(querybuilder):

    query:acled_client.events.EventQueryBuilder = querybuilder.time_precision(1)
    print(query.to_dict())
    assert query.to_dict()["time_precision"] == 1
