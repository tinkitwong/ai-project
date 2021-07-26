from flask import Flask, request, jsonify
from submissions import boilergoose, crazy_goose, greedy, risk_adverse_greedy, simple_bfs, simple_toward, straightforward_bfs
import os

# pubhrl_latest.py has issues on line 95.

app = Flask(__name__)

agent_dict = {
    "boilergoose": boilergoose,
    "crazy_goose": crazy_goose,
    "greedy": greedy,
    # "pubhrl": pubhrl,
    # "pubhrl_latest": pubhrl_latest,
    "risk_adverse_greedy": risk_adverse_greedy,
    "simple_bfs": simple_bfs,
    "simple_toward": simple_toward,
    "straightforward_bfs": straightforward_bfs
}

@app.route("/")
def index():
    return "Hello World! This is version IV."

@app.route("/agent", methods=["POST"])
def getNextMove():
    try:
        data = request.json 
        specified_agents_arr = data['agents']
        obs = data['obs']
        conf = data['conf']
        nextMoves = []
        print(not specified_agents_arr)
        if not specified_agents_arr: return jsonify({"err": "Please provide a list of agents"})
        for agent in specified_agents_arr:
            if agent in agent_dict:
                nextMoves.append(agent_dict[agent].agent(obs, conf))
                
        return jsonify({"nextMoves": nextMoves})    
    except Exception as e:
        print(e)