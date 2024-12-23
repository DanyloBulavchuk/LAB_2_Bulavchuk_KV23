import psycopg2
import time
import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    sex = Column(String(1), nullable=False)
    age = Column(Integer, nullable=False)
    weight = Column(Integer, nullable=False)
    achievements = relationship("Achievement", backref="user")

class Achievement(Base):
    __tablename__ = 'Achievement'

    start_time = Column(String(10), primary_key=True)
    ach_time = Column(String(50))
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)

class App(Base):
    __tablename__ = 'App'

    app_id = Column(Integer, primary_key=True)
    version = Column(Integer, nullable=False)
    rate = Column(String)
    price = Column(Integer, nullable=False)
    goals = relationship("Goal", backref="app")

class Goal(Base):
    __tablename__ = 'Goal'

    goal_id = Column(Integer, primary_key=True)
    start_time = Column(String(10), ForeignKey('Achievement.start_time'), nullable=False)
    app_id = Column(Integer, ForeignKey('App.app_id'), nullable=False)
    kind = Column(String(50), nullable=False)
    priority = Column(Integer, nullable=False)
    trackings = relationship("Tracking", backref="goal")

class Tracking(Base):
    __tablename__ = 'Tracking'

    title = Column(String(50), primary_key=True)
    app_id = Column(Integer, ForeignKey('App.app_id'), nullable=False)
    goal_id = Column(Integer, ForeignKey('Goal.goal_id'), nullable=False)
    sleep = Column(String(50), nullable=False)
    calories = Column(String(50), nullable=False)

class Model:
    def __init__(self):
        self.engine = create_engine('postgresql+psycopg2://cirelote:1601@localhost:5432/fitness-tracking-and-health-app')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.conn = psycopg2.connect(
            dbname='fitness-tracking-and-health-app',
            user='postgres',
            password='1234',
            host='localhost',
            port=5432
        )
        
    def add_user(self, name, sex, age, weight):
        session = self.Session()
        user = User(name=name, sex=sex, age=age, weight=weight)
        session.add(user)
        session.commit()
        session.close()

    def get_users(self):
        session = self.Session()
        users = session.query(User).all()
        session.close()
        return [(u.user_id, u.name, u.sex, u.age, u.weight) for u in users]

    def update_user(self, user_id, name, sex, age, weight):
        session = self.Session()
        user = session.query(User).filter(User.user_id == user_id).first()
        if user:
            user.name = name
            user.sex = sex
            user.age = age
            user.weight = weight
            session.commit()
        session.close()

    def delete_user(self, user_id):
        session = self.Session()
        user = session.query(User).filter(User.user_id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
        session.close()

    def add_achievement(self, start_time, ach_time, user_id):
        session = self.Session()
        achievement = Achievement(start_time=start_time, ach_time=ach_time, user_id=user_id)
        session.add(achievement)
        session.commit()
        session.close()

    def get_achievements(self):
        session = self.Session()
        achievements = session.query(Achievement).all()
        session.close()
        return [(a.start_time, a.ach_time, a.user_id) for a in achievements]

    def add_goal(self, goal_id, start_time, app_id, kind, priority):
        session = self.Session()
        goal = Goal(goal_id=goal_id, start_time=start_time, app_id=app_id, kind=kind, priority=priority)
        session.add(goal)
        session.commit()
        session.close()

    def get_goals(self):
        session = self.Session()
        goals = session.query(Goal).all()
        session.close()
        return [(g.goal_id, g.start_time, g.app_id, g.kind, g.priority) for g in goals]

    def add_tracking(self, title, app_id, goal_id, sleep, calories):
        session = self.Session()
        tracking = Tracking(title=title, app_id=app_id, goal_id=goal_id, sleep=sleep, calories=calories)
        session.add(tracking)
        session.commit()
        session.close()

    def get_tracking(self):
        session = self.Session()
        trackings = session.query(Tracking).all()
        session.close()
        return [(t.title, t.app_id, t.goal_id, t.sleep, t.calories) for t in trackings]
    
    def generate_random_data(self, rows):
        c = self.conn.cursor()

        for _ in range(rows):
            try:
                # Ensure User exists
                c.execute('SELECT COALESCE(MAX(user_id), 0) + 1 FROM public."User"')
                next_user_id = c.fetchone()[0]
                c.execute('''
                    INSERT INTO public."User" (user_id, name, sex, age, weight)
                    VALUES (%s,
                            chr(trunc(65 + random()*25)::int) || chr(trunc(65 + random()*25)::int),
                            CASE WHEN random() > 0.5 THEN 'M' ELSE 'F' END,
                            trunc(18 + random()*62)::int,
                            trunc(50 + random()*70)::int)
                ''', (next_user_id,))

                # Ensure Achievement exists (depends on User) with unique start_time
                unique_start_time = datetime.datetime.now().strftime("%H%M%S%f") + str(next_user_id)
                unique_start_time = unique_start_time[-10:]  # Ensure it fits within varchar(10)
                c.execute('''
                    INSERT INTO public."Achievement" (start_time, ach_time, user_id)
                    VALUES (%s,
                            (trunc(random()*100) || ' hours')::varchar,
                            %s)
                ''', (unique_start_time, next_user_id))

                # Ensure App exists
                c.execute('SELECT COALESCE(MAX(app_id), 0) + 1 FROM public."App"')
                next_app_id = c.fetchone()[0]
                c.execute('''
                    INSERT INTO public."App" (app_id, version, rate, price)
                    VALUES (%s,
                            trunc(random()*10 + 1)::int,
                            trunc(random()*5 + 1)::varchar,
                            trunc(random()*100)::int)
                ''', (next_app_id,))

                # Ensure Goal exists (depends on App and Achievement)
                c.execute('SELECT COALESCE(MAX(goal_id), 0) + 1 FROM public."Goal"')
                next_goal_id = c.fetchone()[0]
                c.execute('''
                    INSERT INTO public."Goal" (goal_id, start_time, app_id, kind, priority)
                    VALUES (%s,
                            %s,
                            %s,
                            CASE trunc(random()*3 + 1)::int
                                WHEN 1 THEN 'Fitness'
                                WHEN 2 THEN 'Diet'
                                ELSE 'Mental Health' END,
                            trunc(random()*5 + 1)::int)
                ''', (next_goal_id, unique_start_time, next_app_id))

                # Generate a unique title for Tracking
                while True:
                    c.execute('SELECT chr(trunc(65 + random()*25)::int) || chr(trunc(65 + random()*25)::int)')
                    tracking_title = c.fetchone()[0]
                    c.execute('SELECT COUNT(*) FROM public."Tracking" WHERE title = %s', (tracking_title,))
                    if c.fetchone()[0] == 0:
                        break

                # Ensure Tracking exists (depends on Goal and App)
                c.execute('''
                    INSERT INTO public."Tracking" (title, app_id, goal_id, sleep, calories)
                    VALUES (%s,
                            %s,
                            %s,
                            (trunc(random()*6 + 4) || ' hours')::varchar,
                            (trunc(random()*1800 + 1200) || ' kcal')::varchar)
                ''', (tracking_title, next_app_id, next_goal_id))

            except Exception as e:
                print(f"Error generating data for iteration {_}: {e}")
                self.conn.rollback()
                continue

        self.conn.commit()

    def search_by_user_and_achievement(self, user_name_pattern, min_weight, max_weight):
        c = self.conn.cursor()
        query = '''
            SELECT u.name, u.age, u.weight, a.ach_time
            FROM public."User" u
            INNER JOIN public."Achievement" a ON u.user_id = a.user_id
            WHERE u.name LIKE %s AND u.weight BETWEEN %s AND %s
            GROUP BY u.name, u.age, u.weight, a.ach_time
        '''
        start_time = time.time()
        c.execute(query, (user_name_pattern, min_weight, max_weight))
        results = c.fetchall()
        elapsed_time = (time.time() - start_time) * 1000
        return results, elapsed_time

    def search_by_app_and_goal(self, min_version, max_version, goal_kind):
        c = self.conn.cursor()
        query = '''
            SELECT g.kind, g.priority, a.version, a.rate
            FROM public."Goal" g
            INNER JOIN public."App" a ON g.app_id = a.app_id
            WHERE a.version BETWEEN %s AND %s AND g.kind LIKE %s
            GROUP BY g.kind, g.priority, a.version, a.rate
        '''
        start_time = time.time()
        c.execute(query, (min_version, max_version, goal_kind))
        results = c.fetchall()
        elapsed_time = (time.time() - start_time) * 1000
        return results, elapsed_time

    def search_by_tracking_and_goal(self, sleep_pattern, min_calories, max_calories):
        c = self.conn.cursor()
        query = '''
            SELECT t.title, t.sleep, t.calories, g.kind, g.priority
            FROM public."Tracking" t
            INNER JOIN public."Goal" g ON t.goal_id = g.goal_id
            WHERE t.sleep LIKE %s AND CAST(split_part(t.calories, ' ', 1) AS integer) BETWEEN %s AND %s
            GROUP BY t.title, t.sleep, t.calories, g.kind, g.priority
        '''
        start_time = time.time()
        c.execute(query, (sleep_pattern, min_calories, max_calories))
        results = c.fetchall()
        elapsed_time = (time.time() - start_time) * 1000
        return results, elapsed_time

    def close_connection(self):
        self.conn.close()

    def abort(self):
        self.conn.rollback()
