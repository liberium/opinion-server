from fastapi import FastAPI
from schemas import Vote as VoteDTO, Voter as VoterDTO, Influencer as InfluencerDTO

app = FastAPI()


@app.get("/votes")
def get_votes(voter_id):
    return voter_id


@app.post("/votes")
def vote(vote_dto: VoteDTO):
    return vote_dto


@app.post("/voters")
def sign_up_voter(voter_dto: VoterDTO):
    return voter_dto


@app.put("/influencers/${influencer_id}")
def update_influencer(influencer_id: int, influencer_dto: InfluencerDTO):
    return influencer_dto
