import datetime
from django.test import TestCase

from tournament.utils.date_time_utils import get_current_date_time


class TestSubscribeToTournament(TestCase):

    def setUp(self):
        from tournament.models import KoTournament, User

        now = get_current_date_time()
        KoTournament.objects.create(
            created_user_id='User',
            name='Tournament1',
            no_of_rounds=3,
            start_datetime=now + datetime.timedelta(days=1)
        )

        User.objects.create(
            user_id='User2'
        )

    def test_subscribe_to_tournament(self):
        from tournament.models import TournamentUser

        tournament_users_before = TournamentUser.objects.all()
        TournamentUser.subscribe_to_tournament(user_id='User2', tournament_id=1)
        tournament_users_after = TournamentUser.objects.all()

        newly_added_objs = [each for each in tournament_users_after if each not in tournament_users_before]
        self.assertEqual(len(newly_added_objs), 1)
        newly_added_obj = newly_added_objs[0]
        self.assertEqual(newly_added_obj.user.user_id, 'User2')
        self.assertEqual(newly_added_obj.tournament.id, 1)
