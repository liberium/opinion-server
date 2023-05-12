from sqlalchemy.orm import Session
from . import models, schemas


def create_voter(session: Session, voter: schemas.Voter):
    fake_hashed_password = voter.password + "notreallyhashed"
    db_user = models.Voter(email=voter.email, hashed_password=fake_hashed_password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
