import unittest
from src.posts.post import Post
from src.posts import posts_repository
from datetime import datetime


class TestPostsRepository(unittest.TestCase):

    def test_save_should_fill_created_at(self):
        user = 'Rafaelfo'
        post = Post(user, 'fala galerinha')

        repository = posts_repository.resolve()

        repository.save_post(post)
        actual_post = repository.get_user_posts(user)[0]

        datetime_format = '%Y-%m-%d %H:%M:%S'
        self.assertEqual(datetime.now().strftime(datetime_format), actual_post.created_at.strftime(datetime_format))

    def test_save_and_get_user_posts(self):
        user_1 = 'Rafaelfo'
        user_2 = 'Morales'
        post_1_user_1 = Post(user_1, 'fala galerinha')
        post_2_user_1 = Post(user_1, 'de buenas?')
        post_1_user_2 = Post(user_2, 'e ai cara')
        post_2_user_2 = Post(user_2, 'suave e vc?')

        repository = posts_repository.resolve()

        repository.save_post(post_1_user_1)
        repository.save_post(post_2_user_1)
        repository.save_post(post_1_user_2)
        repository.save_post(post_2_user_2)

        actual_posts_user_1 = repository.get_user_posts(user_1)
        actual_posts_user_2 = repository.get_user_posts(user_2)

        self.assertIn(post_1_user_1, actual_posts_user_1)
        self.assertIn(post_2_user_1, actual_posts_user_1)
        self.assertNotIn(post_1_user_2, actual_posts_user_1)
        self.assertNotIn(post_2_user_2, actual_posts_user_1)
        self.assertIn(post_1_user_2, actual_posts_user_2)
        self.assertIn(post_2_user_2, actual_posts_user_2)
        self.assertNotIn(post_1_user_1, actual_posts_user_2)
        self.assertNotIn(post_2_user_1, actual_posts_user_2)


if __name__ == '__main__':
    unittest.main()
