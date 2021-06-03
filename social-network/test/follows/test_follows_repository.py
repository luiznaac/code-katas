import unittest
from src.follows.follow import Follow
from src.follows import follows_repository


class TestFollowsRepository(unittest.TestCase):

    def test_save_and_get_user_follows(self):
        user_1 = 'Rafaelfo'
        user_2 = 'Morales'
        follow_1 = Follow(user_1, user_2)
        follow_2 = Follow(user_2, user_1)

        repository = follows_repository.resolve()

        repository.save_follow(follow_1)
        repository.save_follow(follow_2)

        actual_follows_user_1 = repository.get_user_follows(user_1)
        actual_follows_user_2 = repository.get_user_follows(user_2)

        self.assertIn(follow_1, actual_follows_user_1)
        self.assertNotIn(follow_2, actual_follows_user_1)
        self.assertIn(follow_2, actual_follows_user_2)
        self.assertNotIn(follow_1, actual_follows_user_2)


if __name__ == '__main__':
    unittest.main()
