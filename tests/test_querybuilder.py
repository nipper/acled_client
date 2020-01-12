import acled_client.events
import pytest


@pytest.fixture
def querybuilder():
    import acled_client.events

    return acled_client.events.EventQuery.iso(1)


def test_querybuilder(querybuilder):
    assert type(querybuilder) is acled_client.events.EventQueryBuilder


def test_set_iso(querybuilder):
    querybuilder.iso(1)
    assert querybuilder._iso == 1


def test_print_iso(querybuilder):
    querybuilder.iso(1)
    assert querybuilder.__str__() == "_iso: 1 | "
