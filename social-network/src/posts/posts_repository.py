from src.posts.post import Post
from datetime import datetime


class PostsRepository:

    def save_post(self, post: Post):
        pass

    def get_user_posts(self, user):
        pass


class InMemoryPostsRepository(PostsRepository):

    saved_posts = []

    def save_post(self, post: Post):
        post.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.saved_posts.append(post)

    def get_user_posts(self, user):
        return list(filter(lambda post: post.user == user, self.saved_posts))


def resolve() -> PostsRepository:
    return InMemoryPostsRepository()
