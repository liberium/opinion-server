from pydantic import BaseModel, Field
from enum import Enum
from datetime import datetime


class MarketSituation(str, Enum):
    GLOBAL_TREND = "global_trend"
    LOCAL_TREND = "local_trend"
    STABLE_VS_COINS = "stable_vs_coins"
    GLOBAL_PEAK = "global_peak"
    LOCAL_PEAK = "local_peak"
    DOMINATION = "domination"
    GLOBAL_BOTTOM = "global_bottom"
    LOCAL_BOTTOM = "local_bottom"
    PROFIT_VS_DRAWDOWN = "profit_vs_drawdown"
    FEAR_VS_GREED = "fear_vs_greed"


class Vote(BaseModel):
    id: int
    voter_id: int
    market_situation: MarketSituation
    value: float
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        use_enum_values = True
        orm_mode = True


class Voter(BaseModel):
    id: int
    is_influencer: bool = False
    telegram_username: str
    avatar_image_url: str | None

    class Config:
        orm_mode = True


class Influencer(Voter):
    first_name: str | None
    second_name: str | None
    youtube_url: str | None
    instagram_url: str | None
    telegram_url: str | None
    discord_url: str | None
    twitter_url: str | None
