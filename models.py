from enum import Enum
from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    String,
    Float,
    DateTime,
    Enum,
    Boolean,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from schemas import MarketSituation
from database import Base


class Vote(Base):
    __tablename__ = "votes"
    id = Column(Integer, primary_key=True)
    voter_id = Column(Integer, ForeignKey("voters.id"), nullable=False)
    market_situation = Column(Enum(MarketSituation), nullable=False)
    value = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    voter = relationship("Voter", back_populates="votes")


class Voter(Base):
    __tablename__ = "voters"
    id = Column(Integer, primary_key=True, index=True)
    telegram_username = Column(String, unique=True, index=True, nullable=False)
    avatar_image_url = Column(String)
    is_influencer = Column(Boolean, default=False)
    first_name = Column(String)
    second_name = Column(String)
    youtube_url = Column(String)
    instagram_url = Column(String)
    telegram_url = Column(String)
    discord_url = Column(String)
    twitter_url = Column(String)
    votes = relationship("Vote", back_populates="voter")
    referrer_voter_id = Column(Integer)
