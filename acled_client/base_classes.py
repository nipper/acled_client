from acled_client.utils import builder


class BaseBuilder:

    def __init__(self):
        self._terms = False
        self._set_params = []
        self.url: str = "https://api.acleddata.com/acled/read"

    def _add_param(self, item):
        if item not in self._set_params:
            self._set_params.append(item)

    def _remove_param(self, item):
        if item in self._set_params:
            self._set_params.remove(item)

    @builder
    def terms(self, terms):
        self._terms = terms
        self._add_param("_terms")

    def to_dict(self):
        return {key[1:]: getattr(self, key) for key in self._set_params}

    def to_url_parms(self):
        params_string = [f"{k}={v}" for (k, v) in self.to_dict().items()]
        return "&".join(params_string)

    def execute(self):
        return self.results_class(self)

    def __str__(self):

        pretty_view = ""
        for term in self._set_params:
            pretty_view = pretty_view + f"{term}: {getattr(self, term)} | "

        return pretty_view
