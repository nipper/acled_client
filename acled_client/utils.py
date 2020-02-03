import pandas

interactors = [
    "State Forces",
    "Rebel Forces",
    "Militia Groups",
    "Communal/Identity Groups",
    "Rioters",
    "Protestors",
    "Civlians",
    "Foreign/Others",
]

regions = [
    "Northern Africa",
    "Southern Asia",
    "Western Asia",
    "South-Eastern Asia",
    "South Asia",
    "Middle East",
    "Europe",
]

nice_column_names = {
    "data_id": "data_id",
    "iso": "country_iso",
    "event_id_cnty": "event_id_by_country",
    "event_id_no_cnty": "event_id_number_country",
    "event_date": "event_date",
    "year": "year",
    "time_precision": "time_precision",
}

def builder(func):
    """
    Decorator for wrapper "builder" functions.  These are functions on the Query class or other classes used for
    building queries which mutate the query and return self.  To make the build functions immutable, this decorator is
    used which will deepcopy the current instance.  This decorator will return the return value of the inner function
    or the new copy of the instance.  The inner function does not need to return self.
    """
    import copy

    def _copy(self, *args, **kwargs):

        if "in_place" not in kwargs:
            mutate = False
        else:
            mutate = kwargs["in_place"]
            kwargs.pop("in_place")  # removes in_place so our wrapped functions dont need to worry about it.

        if mutate:
            object_to_use = self
        else:
            object_to_use = copy.copy(self)

        func(object_to_use, *args, **kwargs)
        return object_to_use

    return _copy
