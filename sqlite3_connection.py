from tortoise import Tortoise


async def init_sqlite():
    await Tortoise.init(
        db_url="sqlite://sqlite.db",
        modules={"models": ["currency_model"]}
    )
    await Tortoise.generate_schemas()
