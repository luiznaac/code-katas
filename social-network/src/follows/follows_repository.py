from src.follows.follow import Follow


class FollowsRepository:

    def save_follow(self, follow: Follow):
        pass

    def get_user_follows(self, user):
        pass


class InMemoryFollowsRepository(FollowsRepository):

    saved_follows = []

    def save_follow(self, follow: Follow):
        self.saved_follows.append(follow)

    def get_user_follows(self, user):
        return list(filter(lambda follow: follow.user == user, self.saved_follows))


def resolve() -> FollowsRepository:
    return InMemoryFollowsRepository()


def reset():
    InMemoryFollowsRepository.saved_follows = []
