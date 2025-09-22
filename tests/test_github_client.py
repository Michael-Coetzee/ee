import pytest
from app.github_client import get_user_gists


@pytest.mark.asyncio
async def test_get_user_gists_octocat():
    gists = await get_user_gists("octocat")
    assert isinstance(gists, list)
    assert len(gists) > 0
