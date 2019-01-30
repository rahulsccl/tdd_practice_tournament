from django.test import TestCase


class TestCreateTournament(TestCase):
    from ib_tournament.constants.general import TournamentStatus

    name = 'Tournament 1'
    status = TournamentStatus.CAN_JOIN.value

    @staticmethod
    def get_next_day_datetime():
        from ib_common.date_time_utils.get_current_local_date_time import \
            get_current_local_date_time
        from ib_common.date_time_utils.convert_datetime_to_local_string import \
            convert_datetime_to_local_string
        from ib_tournament.constants.general import DEFAULT_DATE_TIME_FORMAT
        from datetime import timedelta

        next_day_datetime = get_current_local_date_time() + timedelta(days=1)
        return convert_datetime_to_local_string(
            next_day_datetime, DEFAULT_DATE_TIME_FORMAT)

    def test_create_tournament(self):
        from ib_tournament.models import Tournament

        total_rounds = 3
        start_datetime_str = self.get_next_day_datetime()
        initial_tournaments_count = Tournament.objects.count()
        Tournament.create_tournament(
            total_rounds, start_datetime_str, self.name)
        tournaments_count = Tournament.objects.count()

        self.assertEqual(tournaments_count - initial_tournaments_count, 1)

    def test_create_tournament_by_user(self):
        from ib_tournament.models import Tournament

        username = 'user1'
        total_rounds = 3
        start_datetime_str = self.get_next_day_datetime()
        initial_tournaments_count = Tournament.objects.count()

        tournament_details = {
            'name': self.name,
            'total_rounds': total_rounds,
            'start_datetime_str': start_datetime_str
        }
        from ib_tournament.models import Player
        Player.create_player(username)
        player = Player.get_player(username)
        Tournament.create_tournament_by_player(
            player_id=player.id, tournament_details=tournament_details)
        tournaments_count = Tournament.objects.count()

        self.assertEqual(tournaments_count - initial_tournaments_count, 1)

    def test_invalid_datetime(self):
        from ib_common.date_time_utils.get_current_local_date_time import \
            get_current_local_date_time
        from ib_common.date_time_utils.convert_datetime_to_local_string import \
            convert_datetime_to_local_string
        from ib_tournament.constants.general import DEFAULT_DATE_TIME_FORMAT

        start_datetime_str = convert_datetime_to_local_string(
            get_current_local_date_time(), DEFAULT_DATE_TIME_FORMAT)
        total_rounds = 3

        from ib_tournament.models import Tournament
        from django_swagger_utils.drf_server.exceptions import BadRequest
        with self.assertRaisesMessage(BadRequest, "Invalid Datetime"):
            Tournament.create_tournament(
                total_rounds, start_datetime_str, self.name)

    def test_invalid_total_rounds(self):
        from ib_tournament.models import Tournament

        total_rounds = -1
        start_datetime_str = self.get_next_day_datetime()

        from django_swagger_utils.drf_server.exceptions import BadRequest
        with self.assertRaisesMessage(BadRequest, "Invalid total rounds"):
            Tournament.create_tournament(
                total_rounds, start_datetime_str, self.name)

    def test_invalid_user(self):
        from ib_tournament.models import Tournament

        total_rounds = 3
        start_datetime_str = self.get_next_day_datetime()

        tournament_details = {
            'name': self.name,
            'total_rounds': total_rounds,
            'start_datetime_str': start_datetime_str
        }
        from django_swagger_utils.drf_server.exceptions import BadRequest
        with self.assertRaisesMessage(BadRequest, "Invalid User"):
            Tournament.create_tournament_by_player(
                player_id=2324, tournament_details=tournament_details)