import asyncio
import anyio
import pytest


async def the_task():
    await asyncio.sleep(99999)


@pytest.fixture
async def agen_fixture():
    async with anyio.create_task_group() as tg:
        tg.start_soon(the_task)
        yield


async def test_aaa(agen_fixture):
    pass
