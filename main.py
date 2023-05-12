from fastapi import FastAPI
from schemas import Vote, Voter, Influencer

app = FastAPI()


@app.get("/votes")
def get_votes(voter_id):
    return [{}]


@app.post("/votes")
def vote(vote: Vote):
    return vote


@app.post("/voters")
def sign_up_voter(voter: Voter):
    return voter


@app.put("/voters/${voter_id}")
def update_influencer(voter_id: int, influencer: Influencer):
    return influencer
