import pytest
import pytest_check as check
from consts import mocks


@pytest.mark.params
@pytest.mark.parametrize('comment_id', mocks.SAMPLE_COMMENT_IDS)
def test_get_comment_basic_shape(comments_service, comment_id):
    comment = comments_service.get_comment(comment_id)
    check.equal(set(comment.keys()), mocks.EXPECTED_COMMENT_KEYS)
    check.is_instance(comment['id'], int)



@pytest.mark.smoke
def test_get_comments_for_post(comments_service):
    # pick a small sample post id
    post_id = 1
    comments = comments_service.get_comments_for_post(post_id)
    assert isinstance(comments, list)
    assert all(c['postId'] == post_id for c in comments)