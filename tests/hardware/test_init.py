"""Hardware init tests."""
from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

from deebot_client.commands.json.advanced_mode import GetAdvancedMode
from deebot_client.commands.json.battery import GetBattery
from deebot_client.commands.json.carpet import GetCarpetAutoFanBoost
from deebot_client.commands.json.charge_state import GetChargeState
from deebot_client.commands.json.clean import GetCleanInfo
from deebot_client.commands.json.clean_count import GetCleanCount
from deebot_client.commands.json.clean_logs import GetCleanLogs
from deebot_client.commands.json.clean_preference import GetCleanPreference
from deebot_client.commands.json.continuous_cleaning import GetContinuousCleaning
from deebot_client.commands.json.efficiency import GetEfficiencyMode
from deebot_client.commands.json.error import GetError
from deebot_client.commands.json.fan_speed import GetFanSpeed
from deebot_client.commands.json.life_span import GetLifeSpan
from deebot_client.commands.json.map import GetCachedMapInfo, GetMajorMap, GetMapTrace
from deebot_client.commands.json.multimap_state import GetMultimapState
from deebot_client.commands.json.network import GetNetInfo
from deebot_client.commands.json.ota import GetOta
from deebot_client.commands.json.pos import GetPos
from deebot_client.commands.json.stats import GetStats, GetTotalStats
from deebot_client.commands.json.true_detect import GetTrueDetect
from deebot_client.commands.json.voice_assistant_state import GetVoiceAssistantState
from deebot_client.commands.json.volume import GetVolume
from deebot_client.commands.json.water_info import GetWaterInfo
from deebot_client.events import (
    AdvancedModeEvent,
    AvailabilityEvent,
    BatteryEvent,
    CarpetAutoFanBoostEvent,
    CleanCountEvent,
    CleanLogEvent,
    CleanPreferenceEvent,
    ContinuousCleaningEvent,
    CustomCommandEvent,
    ErrorEvent,
    LifeSpan,
    LifeSpanEvent,
    MultimapStateEvent,
    OtaEvent,
    ReportStatsEvent,
    RoomsEvent,
    StateEvent,
    StatsEvent,
    TotalStatsEvent,
    TrueDetectEvent,
    VoiceAssistantStateEvent,
    VolumeEvent,
)
from deebot_client.events.efficiency_mode import EfficiencyModeEvent
from deebot_client.events.fan_speed import FanSpeedEvent
from deebot_client.events.map import (
    CachedMapInfoEvent,
    MajorMapEvent,
    MapChangedEvent,
    MapTraceEvent,
    PositionsEvent,
)
from deebot_client.events.network import NetworkInfoEvent
from deebot_client.events.water_info import WaterInfoEvent
from deebot_client.hardware import get_static_device_info
from deebot_client.hardware.deebot import DEVICES, FALLBACK, _load

if TYPE_CHECKING:
    from collections.abc import Callable

    from deebot_client.command import Command
    from deebot_client.events.base import Event
    from deebot_client.models import StaticDeviceInfo


@pytest.mark.parametrize(
    ("class_", "expected"),
    [
        ("not_specified", lambda: DEVICES[FALLBACK]),
        ("yna5xi", lambda: DEVICES["yna5xi"]),
    ],
)
def test_get_static_device_info(
    class_: str, expected: Callable[[], StaticDeviceInfo]
) -> None:
    """Test get_static_device_info."""
    static_device_info = get_static_device_info(class_)
    assert expected() == static_device_info


@pytest.mark.parametrize(
    ("class_", "expected"),
    [
        (
            FALLBACK,
            {
                AdvancedModeEvent: [GetAdvancedMode()],
                AvailabilityEvent: [GetBattery(is_available_check=True)],
                BatteryEvent: [GetBattery()],
                CachedMapInfoEvent: [GetCachedMapInfo()],
                CarpetAutoFanBoostEvent: [GetCarpetAutoFanBoost()],
                CleanCountEvent: [GetCleanCount()],
                CleanLogEvent: [GetCleanLogs()],
                CleanPreferenceEvent: [GetCleanPreference()],
                ContinuousCleaningEvent: [GetContinuousCleaning()],
                CustomCommandEvent: [],
                ErrorEvent: [GetError()],
                FanSpeedEvent: [GetFanSpeed()],
                LifeSpanEvent: [
                    GetLifeSpan([LifeSpan.BRUSH, LifeSpan.FILTER, LifeSpan.SIDE_BRUSH])
                ],
                MapChangedEvent: [],
                MajorMapEvent: [GetMajorMap()],
                MapTraceEvent: [GetMapTrace()],
                MultimapStateEvent: [GetMultimapState()],
                NetworkInfoEvent: [GetNetInfo()],
                PositionsEvent: [GetPos()],
                ReportStatsEvent: [],
                RoomsEvent: [GetCachedMapInfo()],
                StateEvent: [GetChargeState(), GetCleanInfo()],
                StatsEvent: [GetStats()],
                TotalStatsEvent: [GetTotalStats()],
                TrueDetectEvent: [GetTrueDetect()],
                VolumeEvent: [GetVolume()],
                WaterInfoEvent: [GetWaterInfo()],
            },
        ),
        (
            "yna5xi",
            {
                AdvancedModeEvent: [GetAdvancedMode()],
                AvailabilityEvent: [GetBattery(is_available_check=True)],
                BatteryEvent: [GetBattery()],
                CachedMapInfoEvent: [GetCachedMapInfo()],
                CarpetAutoFanBoostEvent: [GetCarpetAutoFanBoost()],
                CleanLogEvent: [GetCleanLogs()],
                ContinuousCleaningEvent: [GetContinuousCleaning()],
                CustomCommandEvent: [],
                ErrorEvent: [GetError()],
                FanSpeedEvent: [GetFanSpeed()],
                LifeSpanEvent: [
                    GetLifeSpan([LifeSpan.BRUSH, LifeSpan.FILTER, LifeSpan.SIDE_BRUSH])
                ],
                MapChangedEvent: [],
                MajorMapEvent: [GetMajorMap()],
                MapTraceEvent: [GetMapTrace()],
                MultimapStateEvent: [GetMultimapState()],
                NetworkInfoEvent: [GetNetInfo()],
                OtaEvent: [GetOta()],
                PositionsEvent: [GetPos()],
                ReportStatsEvent: [],
                RoomsEvent: [GetCachedMapInfo()],
                StateEvent: [GetChargeState(), GetCleanInfo()],
                StatsEvent: [GetStats()],
                TotalStatsEvent: [GetTotalStats()],
                VolumeEvent: [GetVolume()],
                WaterInfoEvent: [GetWaterInfo()],
            },
        ),
        (
            "p95mgv",
            {
                AdvancedModeEvent: [GetAdvancedMode()],
                AvailabilityEvent: [GetBattery(is_available_check=True)],
                BatteryEvent: [GetBattery()],
                CachedMapInfoEvent: [GetCachedMapInfo()],
                CarpetAutoFanBoostEvent: [GetCarpetAutoFanBoost()],
                CleanCountEvent: [GetCleanCount()],
                CleanPreferenceEvent: [GetCleanPreference()],
                ContinuousCleaningEvent: [GetContinuousCleaning()],
                CustomCommandEvent: [],
                EfficiencyModeEvent: [GetEfficiencyMode()],
                ErrorEvent: [GetError()],
                FanSpeedEvent: [GetFanSpeed()],
                LifeSpanEvent: [
                    GetLifeSpan(
                        [
                            LifeSpan.BRUSH,
                            LifeSpan.FILTER,
                            LifeSpan.SIDE_BRUSH,
                            LifeSpan.UNIT_CARE,
                        ]
                    )
                ],
                MajorMapEvent: [GetMajorMap()],
                MapChangedEvent: [],
                MapTraceEvent: [GetMapTrace()],
                MultimapStateEvent: [GetMultimapState()],
                NetworkInfoEvent: [GetNetInfo()],
                OtaEvent: [GetOta()],
                PositionsEvent: [GetPos()],
                ReportStatsEvent: [],
                RoomsEvent: [GetCachedMapInfo()],
                StateEvent: [GetChargeState(), GetCleanInfo()],
                StatsEvent: [GetStats()],
                TotalStatsEvent: [GetTotalStats()],
                TrueDetectEvent: [GetTrueDetect()],
                VoiceAssistantStateEvent: [GetVoiceAssistantState()],
                VolumeEvent: [GetVolume()],
                WaterInfoEvent: [GetWaterInfo()],
            },
        ),
    ],
)
def test_capabilities_event_extraction(
    class_: str, expected: dict[type[Event], list[Command]]
) -> None:
    capabilities = get_static_device_info(class_).capabilities
    assert capabilities._events.keys() == expected.keys()
    for event, expected_commands in expected.items():
        assert capabilities.get_refresh_commands(event) == expected_commands


def test_all_models_loaded() -> None:
    """Test that all models are loaded."""
    _load()
    assert list(DEVICES) == [
        "2o4lnm",
        "55aiho",
        "626v6g",
        "85nbtp",
        "9ku8nu",
        "clojes",
        "fallback",
        "lx3j7m",
        "p1jij8",
        "p95mgv",
        "rss8xk",
        "umwv6z",
        "vi829v",
        "x5d34r",
        "yna5xi",
        "zjavof",
    ]
