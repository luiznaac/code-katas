from src.follows import follows_repository
from src.posts import posts_repository


class WallService:

    user = None

    def __init__(self, user):
        self.user = user

    def build_wall(self):
        users = self.get_users_followed()
        users.append(self.user)
        return self.get_all_posts_from_users_ordered_by_created_date(users)

    def get_users_followed(self):
        repository = follows_repository.resolve()
        follows = repository.get_user_follows(self.user)
        return list(map(lambda follow: follow.followed_user, follows))

    def get_all_posts_from_users_ordered_by_created_date(self, users):
        posts_repo = posts_repository.resolve()
        posts = list(map(lambda user: posts_repo.get_user_posts(user), users))
        flattened_posts = [post for user_posts in posts for post in user_posts]
        flattened_posts.sort(key=lambda post: post.created_at, reverse=True)

        return flattened_posts
