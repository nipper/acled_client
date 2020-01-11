import re
from dataclasses import dataclass
import collections
from typing import Callable

import pycountry

is_number = re.compile("\d+")
is_text = re.compile("\w+")
is_8601 = re.compile("\d{4}-\d{2}-\d{2}")
is_year = re.compile("\d{4]")
is_coord = re.compile(
    "^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$"
)
is_timestamp = None

VALID_QUERY_TERMS = {
    "data_id": is_number,
    "iso": is_text,
    "event_id_cnty": is_text,
    "event_id_no_cnty": is_text,
    "event_date": is_8601,
    "year": is_year,
    "time_precision": is_number,
    "event_type": is_text,
    "sub_event_type": is_text,
    "actor1": is_text,
    "assoc_actor_1": is_text,
    "inter1": is_number,
    "actor2": is_text,
    "assoc_actor_2": is_text,
    "inter2": is_number,
    "interaction": is_number,
    "region": is_number,
    "country": is_text,
    "admin1": is_text,
    "admin2": is_text,
    "admin3": is_text,
    "location": is_text,
    "latitude": is_coord,
    "longitude": is_coord,
    "geo_precision": is_number,
    "source": is_text,
    "source_scale": is_text,
    "notes": is_text,
    "fatalities": is_number,
    "timestamp": is_timestamp,
    "export_type": is_text,
    "iso3": is_iso3,
    "event_date_where": is_text,
}


def is_iso3(val: any) -> bool:
    return val in [x.alpha_3 for x in pycountry.countries]


@dataclass
class Validator:
    func_validate: Callable[[any], bool]
    success_msg: str = "Pass"
    failure_msg: str = "Fail"

    def validate(self, *args):

        Return_val = collections.namedtuple("Return_val", "success msg")

        if self.func_validate(args):
            return Return_val(success=True, msg=self.success_msg)
        else:
            return Return_val(success=False, msg=self.failure_msg)
