from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Dictionary to store vote counts
vote_counts = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user-login')
def user_login():
    return render_template('user_login.html')

@app.route('/election-commission-login')
def election_commission_login():
    return render_template('election_commission_login.html', vote_counts=vote_counts)

@app.route('/vote/<int:candidate_id>', methods=['POST'])
def vote(candidate_id):
    if candidate_id in vote_counts:
        vote_counts[candidate_id] += 1
    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True)
