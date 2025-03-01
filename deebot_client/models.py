"""Models module."""
from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum, StrEnum, unique
from pathlib import Path
from typing import TYPE_CHECKING, Required, TypedDict

if TYPE_CHECKING:
    from deebot_client.capabilities import Capabilities
    from deebot_client.const import DataType


ApiDeviceInfo = TypedDict(
    "ApiDeviceInfo",
    {
        "class": Required[str],
        "company": Required[str],
        "deviceName": str,
        "did": Required[str],
        "name": Required[str],
        "nick": str,
        "resource": Required[str],
    },
    total=False,
)


@dataclass(frozen=True)
class StaticDeviceInfo:
    """Static device info."""

    data_type: DataType
    capabilities: Capabilities


class DeviceInfo:
    """Device info."""

    def __init__(
        self, api_device_info: ApiDeviceInfo, static_device_info: StaticDeviceInfo
    ) -> None:
        self._api_device_info = api_device_info
        self._static_device_info = static_device_info

    @property
    def api_device_info(self) -> ApiDeviceInfo:
        """Return all data goten from the api."""
        return self._api_device_info

    @property
    def company(self) -> str:
        """Return company."""
        return self._api_device_info["company"]

    @property
    def did(self) -> str:
        """Return did."""
        return str(self._api_device_info["did"])

    @property
    def name(self) -> str:
        """Return name."""
        return str(self._api_device_info["name"])

    @property
    def nick(self) -> str | None:
        """Return nick name."""
        return self._api_device_info.get("nick", None)

    @property
    def resource(self) -> str:
        """Return resource."""
        return str(self._api_device_info["resource"])

    @property
    def get_class(self) -> str:
        """Return device class."""
        return str(self._api_device_info["class"])

    @property
    def data_type(self) -> DataType:
        """Return data type."""
        return self._static_device_info.data_type

    @property
    def capabilities(self) -> Capabilities:
        """Return capabilities."""
        return self._static_device_info.capabilities


@dataclass(frozen=True)
class Room:
    """Room representation."""

    name: str
    id: int
    coordinates: str


@unique
class State(IntEnum):
    """State representation."""

    IDLE = 1
    CLEANING = 2
    RETURNING = 3
    DOCKED = 4
    ERROR = 5
    PAUSED = 6


@unique
class CleanAction(StrEnum):
    """Enum class for all possible clean actions."""

    START = "start"
    PAUSE = "pause"
    RESUME = "resume"
    STOP = "stop"


@unique
class CleanMode(StrEnum):
    """Enum class for all possible clean modes."""

    AUTO = "auto"
    SPOT_AREA = "spotArea"
    CUSTOM_AREA = "customArea"


@dataclass(frozen=True)
class Credentials:
    """Credentials representation."""

    token: str
    user_id: str
    expires_at: int = 0


def _str_to_bool_or_cert(value: bool | str) -> bool | str:
    """Convert string to bool or certificate."""
    if isinstance(value, bool):
        return value

    if value is not None:
        value = value.lower()
        if value in ("y", "yes", "t", "true", "on", "1"):
            return True
        if value in ("n", "no", "f", "false", "off", "0"):
            return False
        path = Path(str(value))
        if path.exists():
            # User could provide a path to a CA Cert as well, which is useful for Bumper
            if path.is_file():
                return value
            msg = f"Certificate path provided is not a file: {value}"
            raise ValueError(msg)

    msg = f'Cannot convert "{value}" to a bool or certificate path'
    raise ValueError(msg)
