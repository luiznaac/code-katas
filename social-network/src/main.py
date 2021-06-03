from src.posts import posts_repository
from src.posts.post import Post


def run():
    while True:
        user_action = input()
        perform_action(user_action)


def perform_action(user_action: str):
    if ' -> ' in user_action:
        post_message(*user_action.split(' -> '))
        return


def post_message(user, message):
    posts_repository.resolve().save_post(Post(user, message))


if __name__ == '__main__':
    run()
