from sqlalchemy.orm import Session
from schemas import Voter as VoterDTO
from models import Voter


def create_voter(session: Session, voter_dto: VoterDTO):
    voter = Voter()
    session.add(voter)
    session.commit()
    session.refresh(voter)
    return voter
