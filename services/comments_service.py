from utils.http_client import HTTPClient
from consts import urls


class CommentsService:
    def __init__(self, client: HTTPClient):
        self.client = client

    def get_comment(self, comment_id: int) -> dict:
        u = urls.comments_url(f"comments/{comment_id}")
        return self.client.get(u)

    def get_comments_for_post(self, post_id: int) -> list:
        u = urls.comments_url('comments')
        return self.client.get(u, params={"postId": post_id})