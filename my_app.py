from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from db_design import User, Answers
import uuid
# token: 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
db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///datab.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.app = app
db.init_app(app)


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


@app.route('/stata')
def hi():
    max_age = db.session.query(func.max(User.age)).scalar()
    min_age = db.session.query(func.min(User.age)).scalar()

    right_percentage_1 = (db.session.query(Answers).filter(Answers.ask1 == 'right').count())
    right_percentage_1 = right_percentage_1*100/db.session.query(Answers).count()
    right_percentage_2 = (db.session.query(Answers).filter(Answers.ask2 == 'right').count())
    right_percentage_2 = right_percentage_2*100/db.session.query(Answers).count()

    return render_template('stata.html', max_age=max_age, min_age=min_age,
                           right_per_1=round(right_percentage_1, 2),
                           right_per_2=round(right_percentage_2, 2))


@app.route('/data', methods=['get'])
def data():
    if not request.args:
        return redirect(url_for('quiz'))
    name = request.args.get('name')
    age = request.args.get('age')
    user = User(
        user_id=uuid.uuid4().__str__(),
        name=name,
        age=age
    )

    db.session.add(user)
    db.session.commit()
    db.session.refresh(user)

    ask1 = request.args.get('ask1')
    ask2 = request.args.get('ask2')

    answer = Answers(user_id=user.user_id, ask1=ask1, ask2=ask2)
    db.session.add(answer)
    db.session.commit()

    return redirect(url_for('hi'))


if __name__ == '__main__':
    app.run(debug=True)
