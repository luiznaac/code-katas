import unittest
from src import main
from src.posts import posts_repository


class TestMain(unittest.TestCase):

    def test_post_message(self):
        main.perform_action('Rafaelfo -> e ai meus consagrados')
        main.perform_action('Morales -> jesus me salva')
        posts_repo = posts_repository.resolve()

        posts_1 = posts_repo.get_user_posts('Rafaelfo')
        posts_2 = posts_repo.get_user_posts('Morales')

        self.assertEqual('e ai meus consagrados', posts_1[0].text)
        self.assertEqual('jesus me salva', posts_2[0].text)


if __name__ == '__main__':
    unittest.main()
