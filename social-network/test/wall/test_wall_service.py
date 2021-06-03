import unittest
from src.follows.follow import Follow
from src.follows import follows_repository
from src.posts.post import Post
from src.posts import posts_repository
from src.wall.wall_service import WallService


class TestWallService(unittest.TestCase):

    def setUp(self):
        self.prepare_scenario()

    def test_build_wall(self):
        wall_service_1 = WallService('Morales')
        wall_posts_1 = wall_service_1.build_wall()
        wall_service_2 = WallService('Paranaue')
        wall_posts_2 = wall_service_2.build_wall()

        self.assertEqual('ANALISE', wall_posts_1[0].text)
        self.assertEqual('Top d+', wall_posts_1[1].text)
        self.assertEqual('Primeiro post por aqui :)', wall_posts_1[2].text)
        self.assertEqual('E ai galera!', wall_posts_1[3].text)

        self.assertEqual('inhai', wall_posts_2[0].text)
        self.assertEqual('Top d+', wall_posts_2[1].text)

    def prepare_scenario(self):
        user_1 = 'Rafaelfo'
        user_2 = 'Morales'
        user_3 = 'Paranaue'

        post_repo = posts_repository.resolve()

        post_repo.save_post(Post(user_1, 'E ai galera!'))
        post_repo.save_post(Post(user_1, 'Primeiro post por aqui :)'))
        post_repo.save_post(Post(user_2, 'Top d+'))
        post_repo.save_post(Post(user_3, 'inhai'))
        post_repo.save_post(Post(user_1, 'ANALISE'))

        follow_repo = follows_repository.resolve()

        follow_repo.save_follow(Follow(user_1, user_2))
        follow_repo.save_follow(Follow(user_1, user_3))
        follow_repo.save_follow(Follow(user_2, user_1))
        follow_repo.save_follow(Follow(user_3, user_2))


if __name__ == '__main__':
    unittest.main()
