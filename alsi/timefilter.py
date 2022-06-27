from datetime import datetime
from typing import NamedTuple, Optional

Timefilter = NamedTuple(
    "Timefilter",
    [
        ("start", Optional[datetime]),
        ("end", Optional[datetime]),
        ("limit", Optional[int]),
    ],
)
