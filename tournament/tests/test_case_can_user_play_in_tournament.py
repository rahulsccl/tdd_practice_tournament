from django.test import TestCase

from tournament.constants.general import TournamentStatus
from tournament.models import UserTournament
from ib_common.date_time_utils.convert_string_to_local_date_time \
    import convert_string_to_local_date_time


class TestCanUserPlayInTournament(TestCase):
    user_id = 1
    total_rounds = 4
    start_datetime = "2019-12-12 13:00:00"
    user_name = "John"
    user = None
    tournament = None
    date_time_format = '%Y-%m-%d %H:%M:%S'
    start_datetime_obj = convert_string_to_local_date_time(
        start_datetime, date_time_format
    )

    def test_case_successful_case(self):
        from tournament.models import User, Tournament
        user = User.objects.create(name=self.user_name)
        self.user = user

        obj = Tournament.objects.create(
            user_id=self.user_id,
            total_rounds=self.total_rounds,
            start_datetime=self.start_datetime,
            status=TournamentStatus.CAN_JOIN.value
        )
        self.tournament = obj

        UserTournament.objects.create(
            user_id=self.user.id,
            tournament_id=self.tournament.id
        )

        status = UserTournament.can_user_play_in_tournament(
            user_id=self.user.id, tournament_id=self.tournament.id
        )

        self.assertTrue(status)
