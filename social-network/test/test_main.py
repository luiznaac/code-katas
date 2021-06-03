import unittest
from src import main
from src.posts import posts_repository
from src.follows import follows_repository


class TestMain(unittest.TestCase):

    def setUp(self):
        main.printer = mocked_print

    def tearDown(self):
        posts_repository.reset()
        follows_repository.reset()
        reset_mocked_printer()

    def test_post_message(self):
        main.perform_action('Rafaelfo -> e ai meus consagrados')
        main.perform_action('Morales -> jesus me salva')
        posts_repo = posts_repository.resolve()

        posts_1 = posts_repo.get_user_posts('Rafaelfo')
        posts_2 = posts_repo.get_user_posts('Morales')

        self.assertEqual('e ai meus consagrados', posts_1[0].text)
        self.assertEqual('jesus me salva', posts_2[0].text)

    def test_print_wall(self):
        main.perform_action('Rafaelfo -> e ai meus consagrados')
        main.perform_action('Morales -> jesus')
        main.perform_action('Morales -> me ajuda')
        main.perform_action('Rafaelfo wall')
        main.perform_action('Morales wall')

        self.assertEqual('Rafaelfo - e ai meus consagrados', printed[0])
        self.assertEqual('Morales - jesus', printed[1])
        self.assertEqual('Morales - me ajuda', printed[2])

    def test_follow(self):
        main.perform_action('Rafaelfo follows Morales')
        main.perform_action('Rafaelfo follows Jakubiaki')
        main.perform_action('Morales follows Jakubiaki')
        follows_repo = follows_repository.resolve()

        follows_1 = follows_repo.get_user_follows('Rafaelfo')
        follows_2 = follows_repo.get_user_follows('Morales')

        self.assertEqual('Morales', follows_1[0].followed_user)
        self.assertEqual('Jakubiaki', follows_1[1].followed_user)
        self.assertEqual('Jakubiaki', follows_2[0].followed_user)

    def test_print_user_posts(self):
        main.perform_action('Rafaelfo -> brilha muito')
        main.perform_action('Morales -> no curintia')

        main.perform_action('Morales')
        main.perform_action('Rafaelfo')

        self.assertEqual('no curintia', printed[0])
        self.assertEqual('brilha muito', printed[1])


printed = []


def mocked_print(text):
    printed.append(text)


def reset_mocked_printer():
    printed.clear()


if __name__ == '__main__':
    unittest.main()
