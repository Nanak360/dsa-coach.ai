import asyncio
from app.db.database import engine
from app.db.models.user import User
from app.db.models.onboarding_questioner import OnboardingQuestionerDbSchema
# from app.db.models.syllabus_item import SyllabusItem
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy import text

async def init_db():
    async with engine.begin() as conn:
        # Create tables only if they do not exist
        await conn.run_sync(lambda sync_conn: User.metadata.create_all(sync_conn, checkfirst=True))
        await conn.run_sync(lambda sync_conn: OnboardingQuestionerDbSchema.metadata.create_all(sync_conn, checkfirst=True))
        # await conn.run_sync(lambda sync_conn: SyllabusItem.metadata.create_all(sync_conn, checkfirst=True))
