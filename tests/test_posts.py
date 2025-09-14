import pytest
import pytest_check as check
from consts import mocks


@pytest.mark.params
@pytest.mark.parametrize('post_id', mocks.SAMPLE_POST_IDS)
def test_get_post_basic_shape(posts_service, post_id):
    post = posts_service.get_post(post_id)
    check.equal(set(post.keys()), mocks.EXPECTED_POST_KEYS)
    check.is_instance(post['id'], int)
    check.is_instance(post['userId'], int)




@pytest.mark.smoke
def test_get_posts_by_user(posts_service):
    for user_id in mocks.SAMPLE_USER_IDS:
        posts = posts_service.get_posts_by_user(user_id)
        assert isinstance(posts, list)
        assert all(p['userId'] == user_id for p in posts)