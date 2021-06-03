from src.posts import posts_repository
from src.posts.post import Post
from src.wall.wall_service import WallService
from src.follows import follows_repository
from src.follows.follow import Follow

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
    if ' follows ' in user_action:
        follow(*user_action.split(' follows '))
        return
    print_user_posts(user_action)


def post_message(user, message):
    posts_repository.resolve().save_post(Post(user, message))


def print_wall(user):
    posts = WallService(user).build_wall()
    for post in posts:
        printer('{} - {}'.format(post.user, post.text))


def follow(user, followed_user):
    follows_repository.resolve().save_follow(Follow(user, followed_user))


def print_user_posts(user):
    posts = posts_repository.resolve().get_user_posts(user)
    for post in posts:
        printer(post.text)


if __name__ == '__main__':
    run()
