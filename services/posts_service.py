from utils.http_client import HTTPClient
from consts import urls


class PostsService:
    def __init__(self, client: HTTPClient):
        self.client = client

    def get_post(self, post_id: int) -> dict:
        u = urls.posts_url(f"posts/{post_id}")
        return self.client.get(u)

    def get_posts_by_user(self, user_id: int) -> list:
        u = urls.posts_url('posts')
        return self.client.get(u, params={"userId": user_id})