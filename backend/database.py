from fastapi import Request


async def get_conn(request: Request):
    async with request.app.state.pool.acquire() as conn:
        yield conn
