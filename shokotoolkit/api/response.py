"""
Response wrapper classes.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ApiResponse:
    """
    Generic response returned by the API layer.
    """

    status_code: int

    data: Any

    headers: dict[str, str]
