from src.posts import posts_repository
from src.posts.post import Post
from src.wall.wall_service import WallService

printer = print


def run():
    while True:
        user_action = input()
        perform_action(user_action)


def perform_action(user_action: str):
    if ' -> ' in user_action:
        post_message(*user_action.split(' -> '))
        return
    if ' wall' in user_action:
        print_wall(user_action.strip(' wall'))
        return


def post_message(user, message):
    posts_repository.resolve().save_post(Post(user, message))


def print_wall(user):
    posts = WallService(user).build_wall()
    for post in posts:
        printer('{} - {}'.format(post.user, post.text))


if __name__ == '__main__':
    run()
