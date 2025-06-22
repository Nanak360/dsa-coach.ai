# from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
# from sqlalchemy.sql import func
# from app.db.database import Base

# class SyllabusItem(Base):
#     __tablename__ = "syllabus_items"

#     id = Column(Integer, primary_key=True)
#     user_profile_id = Column(Integer, ForeignKey("user_study_profile.id", ondelete="CASCADE"))
#     title = Column(String)
#     description = Column(String)
#     topic_slug = Column(String)
#     status = Column(String, default="pending")  # pending, in_progress, completed
#     due_date = Column(DateTime(timezone=True), nullable=True)