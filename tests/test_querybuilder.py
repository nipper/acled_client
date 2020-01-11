import acled.query
import pytest


@pytest.fixture
def querybuilder():
    import acled.query

    return acled.query.Query.iso(1)


def test_querybuilder(querybuilder):
    assert type(querybuilder) is acled.query.QueryBuilder


def test_set_iso(querybuilder):
    querybuilder.iso(1)
    assert querybuilder._iso == 1


def test_print_iso(querybuilder):
    querybuilder.iso(5)
    assert querybuilder.__str__() == "_iso: 5 | "
