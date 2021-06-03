import unittest
from src import main
from src.posts import posts_repository


class TestMain(unittest.TestCase):

    def setUp(self):
        main.printer = mocked_print

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


printed = []


def mocked_print(text):
    printed.append(text)


if __name__ == '__main__':
    unittest.main()
