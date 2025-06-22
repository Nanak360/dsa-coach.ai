from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError
from app.services.user_onboarding.questions import questions
from app.services.user_onboarding.types import UserDetails, OnboardingQuestioner
from app.db.models.user import User
from app.db.models.onboarding_questioner import OnboardingQuestionerDbSchema
from datetime import datetime


async def create_user(answers: UserDetails, db: AsyncSession):
    """
    This function creates a new user with the provided details and saves it to the database.
    
    :param answers: UserDetails object containing information about the user
    :type answers: UserDetails
    :param db: AsyncSession object from SQLAlchemy, used to interact with the database asynchronously
    :type db: AsyncSession
    """
    print("Creating user with answers:", answers, type(answers), answers.email)
    if not answers.email or not answers.phone:
        raise ValueError("Email and phone are required fields.")
    if not answers.first_name:
        raise ValueError("First name is a required field.")

    try:
        # check if user already exists
        result = await db.execute(
            select(User).where((User.email == answers.email) | (User.phone == answers.phone))
        )
        existing_user = result.scalars().first()
        if existing_user:
            raise ValueError("User with this email or phone already exists.")

        # create new user
        user = User(
            email=answers.email,
            phone=answers.phone,
            first_name=answers.first_name,
            middle_name=answers.middle_name,
            last_name=answers.last_name,
            gender=answers.gender,
            date_of_birth=datetime.strptime(answers.date_of_birth, "%Y-%m-%d").date() if answers.date_of_birth else None,
            profile_picture=answers.profile_picture,
            bio=answers.bio,
            linkedin_url=answers.linkedin_url,
            github_url=answers.github_url,
            twitter_url=answers.twitter_url,
            website_url=answers.website_url,
            location=answers.location,
            occupation=answers.occupation,
            education=answers.education,
            skills=','.join(answers.skills) if answers.skills else '',
        )
        db.add(user)
        await db.commit()  # commit the transaction to save the user
        return {"message": "user created successfully", "user_email": user.email}
    except SQLAlchemyError as e:
        await db.rollback()
        raise RuntimeError(f"Database error occurred while creating user: {str(e)}")
    except Exception as e:
        await db.rollback()
        raise RuntimeError(f"Unexpected error occurred while creating user: {str(e)}")


async def save_onboarding_questioner(answers: OnboardingQuestioner, db: AsyncSession):
    """
    This function saves the onboarding questionnaire answers for a specific user in a database session.
    
    :param answers: OnboardingQuestioner object containing the user's answers to onboarding questions
    :type answers: OnboardingQuestioner
    :param user_id: The `user_id` parameter is a unique identifier for the user who is completing the
    onboarding questionnaire. It is used to associate the user's answers with their profile or account
    in the database
    :type user_id: str
    :param db: The `db` parameter is typically used to represent a database session object. In this
    context, it seems like you are using SQLAlchemy's `AsyncSession` object for database operations. The
    `AsyncSession` object allows you to interact with the database asynchronously by executing queries, committing
    transactions, and managing database connections.
    :type db: AsyncSession
    """
    try:
        result = await db.execute(select(User).where(User.email == answers.user_email))
        user_exists = result.scalars().first()
        if not user_exists:
            raise ValueError("User ID does not exist in the database.")
        onboardingQuestionerDetails = OnboardingQuestionerDbSchema(
            email=answers.user_email,
            target_company=",".join(answers.target_company) if answers.target_company else None,
            known_topics=",".join(answers.known_topics) if answers.known_topics else None,
            study_time=answers.study_time,
            learning_style=answers.learning_style,
            challenging_topics=",".join(answers.challenging_topics) if answers.challenging_topics else None,
            interview_weeks=answers.interview_weeks,
            mock_experience=answers.mock_experience,
            preferred_platform=answers.preferred_platform,
            current_status=answers.current_status
        )
        db.add(onboardingQuestionerDetails)
        await db.commit()
        return {"message": "Onboarding questioner details saved successfully."}
    except SQLAlchemyError as e:
        await db.rollback()
        raise RuntimeError(f"Database error occurred while saving onboarding questioner: {str(e)}")
    except Exception as e:
        await db.rollback()
        raise RuntimeError(f"Unexpected error occurred while saving onboarding questioner: {str(e)}")