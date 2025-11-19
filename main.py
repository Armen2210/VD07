from app import app, db
from app.models import User   # важно импортировать модели, чтобы таблицы создались

# создаём БД и таблицы, если их ещё нет
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
