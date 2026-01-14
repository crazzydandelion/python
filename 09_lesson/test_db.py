from sqlalchemy import create_engine, inspect, text
import pytest
db_connection_string = "postgresql://postgres:123@localhost/postgres"
db = create_engine(db_connection_string)

# проверяем соединение
def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[7] == 'group_student'

def test_insert_new_subject():
    connection = db.connect()
    transaction = connection.begin()
    # запрашиваем количество строк до теста
    initial_count = connection.execute(text("SELECT COUNT(*) FROM subject")).scalar()

    # создаем новый предмет с номером и названием
    sql = text("insert into subject (subject_id, subject_title) values (:new_id, :new_title)")
    connection.execute(sql, {'new_id': 17,'new_title': 'Latin'})

    # удаляем за собой новый предмет
    sql = text("DELETE FROM subject WHERE subject_id = :new_id")
    connection.execute(sql, {"new_id": 17})
    # запрашиваем количество строк после теста
    final_count = connection.execute(text("SELECT COUNT(*) FROM subject")).scalar()
    # сравниваем, что строка действительно исчезла
    assert initial_count == final_count
    transaction.commit()
    connection.close()

def test_insert_and_update():
    connection = db.connect()
    transaction = connection.begin()
    # запрашиваем количество строк до теста
    initial_count = connection.execute(text("SELECT COUNT(*) FROM subject")).scalar()
    # создаем новый предмет с номером и названием
    sql = text("insert into subject (subject_id, subject_title) values (:new_id, :new_title)")
    connection.execute(sql, {'new_id': 17, 'new_title': 'Latin'})

    # меняем предмету название
    sql = text("update subject set subject_title =:new_title where subject_id =:new_id")
    connection.execute(sql, {'new_title': 'Greek', 'new_id':17})

    # удаляем за собой новый предмет
    sql = text("DELETE FROM subject WHERE subject_id = :new_id")
    connection.execute(sql, {"new_id": 17})
    # запрашиваем количество строк после теста
    final_count = connection.execute(text("SELECT COUNT(*) FROM subject")).scalar()
    transaction.commit()
    connection.close()
    # сравниваем, что строка действительно исчезла
    assert initial_count == final_count

def test_delete_subject():
    connection = db.connect()
    transaction = connection.begin()
    connection = db.connect()
    transaction = connection.begin()
    # запрашиваем количество строк до теста
    initial_count = connection.execute(text("SELECT COUNT(*) FROM subject")).scalar()

    # создаем новый предмет с номером и названием
    sql = text("insert into subject (subject_id, subject_title) values (:new_id, :new_title)")
    connection.execute(sql, {'new_id': 17, 'new_title': 'Latin'})

    # удаляем за собой новый предмет
    sql = text("DELETE FROM subject WHERE subject_id = :new_id")
    connection.execute(sql, {"new_id": 17})

    # проверяем, что такого id действительно больше нет
    rows = connection.execute(text("select * from subject where subject_id = 17")).scalar()
    assert rows == None

    # запрашиваем количество строк после теста
    final_count = connection.execute(text("SELECT COUNT(*) FROM subject")).scalar()
    # сравниваем, что строка действительно исчезла
    assert initial_count == final_count
    transaction.commit()
    connection.close()