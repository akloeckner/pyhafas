from typing import Dict, List

from pyhafas.profile import ProfileInterface
from pyhafas.profile.base import BaseJourneysRequest
from pyhafas.profile.interfaces.requests.journeys import JourneysRequestInterface

from pyhafas.types.fptf import Station


class DBJourneysRequest(BaseJourneysRequest, JourneysRequestInterface):
    """
    Class for the DB Journeys requests, because of some customization
    """

    def format_journeys_request(
            self: ProfileInterface,
            origin: Station,
            destination: Station,
            via: List[Station],
            date: datetime.datetime,
            min_change_time: int,
            max_changes: int,
            products: Dict[str, bool],
            max_journeys: int
    ) -> dict:
        base = super().format_journeys_request(
            origin, destination, via, date,min_change_time, max_changes, products, max_journeys)
        if not isinstance(base['cfg'], dict):
            base['cfg'] = {}
        base['cfg']['rtMode'] = 'HYBRID'
        return base
