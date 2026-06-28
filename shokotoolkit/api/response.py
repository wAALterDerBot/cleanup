from dataclasses import dataclass


@dataclass(slots=True)
class ApiResponse:

    status: int

    data: object

    headers: dict
