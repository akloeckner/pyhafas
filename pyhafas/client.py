from __future__ import annotations

import datetime
import json
from typing import (TYPE_CHECKING, Any, Awaitable, Dict, List, Optional, Tuple,
                    Union)

from .fptf import Journey, Station
from .profile import DBProfile, Profile, StationBoardRequestType


class HafasClient:
    def __init__(
            self,
            profile: Profile = DBProfile(),
            ua: str = "pyhafas",
            debug: bool = False):

        self.profile = profile
        self.useragent = ua
        self.debug = debug

    def departures(self, station):
        if not isinstance(station, Station):
            station = Station(station)

        body = self.profile.formatStationBoardRequest(
            station, StationBoardRequestType.DEPARTURE)
        res = self.profile.request(body)

        return self.profile.parseStationBoardRequest(res.text)

    def arrivals(self, station):
        if not isinstance(station, Station):
            station = Station(station)

        body = self.profile.formatStationBoardRequest(
            station, StationBoardRequestType.ARRIVAL)
        res = self.profile.request(body)

        return self.profile.parseStationBoardRequest(res.text)

    def journeys(
            self,
            origin,
            destination,
            date: datetime.datetime,
            via: List = [],
            min_change_time: int = 0,
            max_changes: int = -1
    ) -> List[Journey]:
        if not isinstance(origin, Station):
            origin = Station(origin)
        if not isinstance(destination, Station):
            destination = Station(destination)
        for via_station in via:
            if not isinstance(via_station, Station):
                via[via.index(via_station)] = Station(via_station)

        body = self.profile.formatJourneysRequest(
            origin,
            destination,
            via,
            date,
            min_change_time,
            max_changes
        )
        res = self.profile.request(body)

        return self.profile.parseJourneysRequest(res.text)

    def journey(self, journey) -> Journey:
        if not isinstance(journey, Station):
            journey = Journey(journey)

        body = self.profile.formatJourneyRequest(journey)
        res = self.profile.request(body)

        return self.profile.parseJourneyRequest(res.text)

    def locations(self, term: str) -> List[Station]:
        body = self.profile.formatLocationRequest(term)
        res = self.profile.request(body)

        return self.profile.parseLocationRequest(res.text)

    def stop(self, stop):
        pass

    def nearby(self, location):
        pass

    def trip(self, id, name):
        pass

    def radar(self, north, west, south, east):
        pass