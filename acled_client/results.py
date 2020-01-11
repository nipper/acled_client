import pandas
import requests
from typing import Generator


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
            print(self.query_page)
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
