from flask import Flask, render_template, redirect, url_for, request
from models import db, Mission
from forms import MissionForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///missions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Substitua por uma chave secreta

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    missions = Mission.query.order_by(Mission.launch_date.desc()).all()
    return render_template('index.html', missions=missions)

@app.route('/mission/new', methods=['GET', 'POST'])
def create_mission():
    form = MissionForm()
    if form.validate_on_submit():
        mission = Mission(
            name=form.name.data,
            launch_date=form.launch_date.data,
            destination=form.destination.data,
            state=form.state.data,
            crew=form.crew.data,
            payload=form.payload.data,
            duration=form.duration.data,
            cost=form.cost.data,
            status=form.status.data
        )
        db.session.add(mission)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html', form=form)

@app.route('/mission/<int:id>/edit', methods=['GET', 'POST'])
def update_mission(id):
    mission = Mission.query.get_or_404(id)
    form = MissionForm(obj=mission)
    if form.validate_on_submit():
        mission.name = form.name.data
        mission.destination = form.destination.data
        mission.crew = form.crew.data
        mission.payload = form.payload.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', form=form)

@app.route('/mission/<int:id>/delete', methods=['POST'])
def delete_mission(id):
    mission = Mission.query.get_or_404(id)
    db.session.delete(mission)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
