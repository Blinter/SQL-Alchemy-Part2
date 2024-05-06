from random import randint

from models import User, Post, db
from app import app
import sqlalchemy as db2
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime, timezone, UTC, timedelta

def generate_random_datetime_start(start_date=datetime(2021,5,1),
                             end_date=datetime(2022,5,1)):
    time_between_days = end_date - start_date
    days_since_start = randint(0, time_between_days.days)
    random_date = start_date + timedelta(days=days_since_start)
    random_date += timedelta(seconds=randint(0, 24 * 60 * 60))
    return random_date

def generate_random_datetime_end(start_date=datetime(2022,5,2),
                             end_date=datetime(2024,5,1)):
    time_between_days = end_date - start_date
    days_since_start = randint(0, time_between_days.days)
    random_date = start_date + timedelta(days=days_since_start)
    random_date += timedelta(seconds=randint(0, 24 * 60 * 60))
    return random_date

engine = db2.create_engine('postgresql:///blogly_part1')
if not database_exists(engine.url):
    create_database(engine.url, encoding='SQL_ASCII')
with app.app_context():
    db.drop_all()
    db.create_all()
    user1 = User(first_name="Alice", last_name="Smith",
             image_url="https://via.placeholder.com/50")
    user2 = User(first_name="Bob", last_name="Johnson",
             image_url="https://via.placeholder.com/50")
    user3 = User(first_name="Trey", middle_name="M", last_name="Dwight",
             image_url="https://via.placeholder.com/50")
    user4 = User(first_name="Toy", last_name="Darwin",
             image_url="https://via.placeholder.com/50")
    user5 = User(first_name="Paw", last_name="Rox",
             image_url="https://via.placeholder.com/50")
    user6 = User(first_name="Paa", last_name="Roc",
             image_url="https://via.placeholder.com/50")
    user7 = User(first_name="E3s", last_name="E1e",
             image_url="https://via.placeholder.com/50")
    user8 = User(first_name="Aass", last_name="Ewdq",
            image_url="https://via.placeholder.com/50")
    user9 = User(first_name="Ady", last_name="FAs",
             image_url="https://via.placeholder.com/50")
    user10 = User(first_name="ESA", last_name="FSf",
             image_url="https://via.placeholder.com/50")
    db.session.add_all([user1, user2, user3, user4, user5, user6, user7,
                        user8, user9, user10])
    db.session.commit()
    users = User.query.all()
    print(users)
    db.session.add_all([
        Post(title='Mauris cursus mattis molestie',
             created_at=generate_random_datetime_start(),
             modified_on=generate_random_datetime_end(),
             content='Lorem ipsum dolor sit amet',
             user_id=users[-1].id),
        Post(title='Mauris cursus mattis molestie',
             created_at=generate_random_datetime_start(),
             modified_on=generate_random_datetime_end(),
             content='Lorem ipsum dolor sit amet, consectetur adipiscing elit, '
                     'sed do eiusmod tempor incididunt ut labore et dolore '
                     'magna aliqua. Fermentum dui faucibus in ornare quam '
                     'viverra orci sagittis. Nisi quis eleifend quam '
                     'adipiscing. Imperdiet dui accumsan sit amet. Praesent '
                     'elementum facilisis leo vel fringilla est ullamcorper '
                     'eget. Magna fringilla urna porttitor rhoncus dolor purus '
                     'non enim praesent. Sit amet porttitor eget dolor morbi. '
                     'Nec feugiat nisl pretium fusce. Blandit libero volutpat '
                     'sed cras. Mi proin sed libero enim sed faucibus turpis. '
                     'Elit sed vulputate mi sit amet mauris commodo quis. In '
                     'hac habitasse platea dictumst quisque sagittis purus sit.'
                     ' Magna sit amet purus gravida quis blandit. Rutrum '
                     'tellus pellentesque eu tincidunt. Fringilla ut morbi '
                     'tincidunt augue interdum velit euismod. Vitae aliquet nec'
                     ' ullamcorper sit. Sit amet consectetur adipiscing elit '
                     'pellentesque habitant morbi tristique. Fringilla ut morbi'
                     ' tincidunt augue interdum velit euismod in pellentesque. '
                     'Amet justo donec enim diam vulputate ut pharetra. '
                     'Pulvinar proin gravida hendrerit lectus a. '
                     '\n\n'
                     'Scelerisque varius morbi enim nunc. Fames ac turpis '
                     'egestas integer eget aliquet nibh praesent tristique. '
                     'Id venenatis a condimentum vitae sapien pellentesque. '
                     'Nibh venenatis cras sed felis eget velit. Curabitur vitae'
                     ' nunc sed velit dignissim sodales ut eu sem. Viverra '
                     'justo nec ultrices dui sapien eget mi proin. Facilisi '
                     'nullam vehicula ipsum a arcu cursus vitae congue. Ac '
                     'odio tempor orci dapibus ultrices in iaculis nunc sed. '
                     'Risus pretium quam vulputate dignissim suspendisse. '
                     'Dignissim convallis aenean et tortor at risus. At '
                     'imperdiet dui accumsan sit amet nulla facilisi morbi. '
                     'Maecenas volutpat blandit aliquam etiam erat velit '
                     'scelerisque in. At erat pellentesque adipiscing commodo '
                     'elit at imperdiet dui. Phasellus faucibus scelerisque '
                     'eleifend donec. Elementum nibh tellus molestie nunc non. '
                     'Nam at lectus urna duis convallis convallis. Porttitor '
                     'leo a diam sollicitudin tempor id.',
             user_id=users[-2].id),
        Post(title='Adipiscing enim eu',
             created_at=generate_random_datetime_start(),
             modified_on=generate_random_datetime_end(),
             content='turpis egestas pretium aenean pharetra magna. Nunc '
                     'scelerisque viverra mauris in. Nisl condimentum id '
                     'venenatis a condimentum vitae sapien. Ut etiam sit amet '
                     'nisl purus in mollis. Ut tristique et egestas quis ipsum.'
                     ' Morbi non arcu risus quis varius quam quisque id. Ut eu '
                     'sem integer vitae justo eget magna fermentum iaculis. '
                     'Massa placerat duis ultricies lacus. Id consectetur purus'
                     ' ut faucibus pulvinar elementum integer enim neque.',
             user_id=users[-3].id),
        Post(title='a. Nisi vitae suscipit tellus',
             created_at=generate_random_datetime_start(),
             modified_on=generate_random_datetime_end(),
             content='consectetur adipiscing elit',
             user_id=users[-4].id),
        Post(title='mauris a. Tempus imperdiet',
             created_at=generate_random_datetime_start(),
             modified_on=generate_random_datetime_end(),
             content='sed do eiusmod tempor',
             user_id=users[-5].id),
        Post(title='nulla malesuada pellentesque',
             created_at=generate_random_datetime_start(),
             modified_on=generate_random_datetime_end(),
             content='incididunt ut labore et',
             user_id=users[0].id),
        Post(title='elit eget gravida cum',
             created_at=generate_random_datetime_start(),
             modified_on=generate_random_datetime_end(),
             content='dolore magna aliqua.',
             user_id=users[1].id),
        Post(title='sociis. Eget est lorem',
             created_at=None,
             modified_on=None,
             content='Magna sit amet purus gravida quis blandit turpis cursus '
                     'in. Nisl condimentum id venenatis a condimentum vitae '
                     'sapien pellentesque. Faucibus in ornare quam viverra. '
                     'Elit pellentesque habitant morbi tristique senectus et '
                     'netus et. Duis at consectetur lorem donec massa sapien. '
                     'Sem integer vitae justo eget. Proin sed libero enim sed '
                     'faucibus turpis in eu. Ante metus dictum at tempor '
                     'commodo ullamcorper a. Lacus viverra vitae congue eu '
                     'consequat ac felis. Vitae tortor condimentum lacinia quis'
                     ' vel eros donec. Turpis massa sed elementum tempus '
                     'egestas sed sed risus pretium. Eget aliquet nibh praesent'
                     ' tristique magna sit amet purus gravida.'
                     '\n\n'
                     'Enim blandit volutpat maecenas volutpat blandit aliquam '
                     'etiam. Sed adipiscing diam donec adipiscing. Sit amet '
                     'consectetur adipiscing elit duis tristique sollicitudin '
                     'nibh sit. Aliquam sem fringilla ut morbi tincidunt augue '
                     'interdum velit. Ac feugiat sed lectus vestibulum mattis '
                     'ullamcorper velit sed ullamcorper. In massa tempor nec '
                     'feugiat nisl pretium. Ullamcorper a lacus vestibulum sed '
                     'arcu non odio euismod. Sit amet aliquam id diam maecenas '
                     'ultricies mi eget. Netus et malesuada fames ac turpis '
                     'egestas maecenas pharetra convallis. Nisl condimentum id '
                     'venenatis a condimentum vitae sapien pellentesque.'
                     '\n\n'
                     'Eu scelerisque felis imperdiet proin fermentum leo. Eros '
                     'in cursus turpis massa tincidunt dui ut ornare lectus. '
                     'Tristique risus nec feugiat in fermentum posuere urna nec'
                     ' tincidunt. Orci a scelerisque purus semper eget duis at '
                     'tellus at. Morbi tristique senectus et netus. Praesent '
                     'semper feugiat nibh sed pulvinar proin gravida hendrerit.'
                     ' Ac placerat vestibulum lectus mauris ultrices eros in. '
                     'Cursus euismod quis viverra nibh cras pulvinar mattis '
                     'nunc sed. Id eu nisl nunc mi ipsum. Sodales neque sodales'
                     ' ut etiam sit amet nisl purus in. Dolor sit amet '
                     'consectetur adipiscing elit ut. Turpis egestas sed tempus'
                     ' urna et pharetra pharetra. Dignissim diam quis enim '
                     'lobortis scelerisque fermentum. Rhoncus urna neque '
                     'viverra justo nec ultrices dui sapien. Ultricies lacus '
                     'sed turpis tincidunt id aliquet risus feugiat. Arcu '
                     'cursus euismod quis viverra nibh cras pulvinar mattis '
                     'nunc. Cursus vitae congue mauris rhoncus aenean vel. '
                     'Felis imperdiet proin fermentum leo vel orci porta non '
                     'pulvinar. Vehicula ipsum a arcu cursus vitae. Diam quam '
                     'nulla porttitor massa id.',
             user_id=users[2].id),
        Post(title='ipsum dolor.',
             created_at=None,
             modified_on=None,
             content='quis nostrud exercitation',
             user_id=users[3].id),
        Post(title='Diam sit amet nisl suscipit',
             created_at=None,
             modified_on=None,
             content='ullamco laboris nisi ut',
             user_id=users[4].id),
        Post(title='adipiscing bibendum est ultricies',
             created_at=generate_random_datetime_start(),
             modified_on=generate_random_datetime_end(),
             content='aliquip ex ea commodo',
             user_id=users[0].id),
        Post(title='integer.',
             created_at=None,
             modified_on=None,
             content='Pellentesque nec nam aliquam sem et tortor consequat id.'
                     ' Maecenas sed enim ut sem viverra aliquet. Id venenatis '
                     'a condimentum vitae.',
             user_id=users[1].id),
        Post(title='Nisl nunc mi ipsum',
             created_at=None,
             modified_on=None,
             content='Diam in arcu cursus euismod quis viverra nibh cras. Odio '
                     'ut sem nulla pharetra diam sit amet nisl suscipit. '
                     'Eleifend donec pretium vulputate sapien nec sagittis. '
                     'Nisl suscipit adipiscing bibendum est.',
             user_id=users[2].id),
        Post(title='faucibus vitae aliquet.',
             created_at=generate_random_datetime_start(),
             modified_on=generate_random_datetime_end(),
             content='Sit amet nisl purus in mollis nunc. Lacus sed turpis '
                     'tincidunt id aliquet risus. Dictum fusce ut placerat '
                     'orci nulla pellentesque dignissim enim sit.',
             user_id=users[3].id),
        Post(title='vestibulum lectus mauris.',
             created_at=None,
             modified_on=None,
             content='Non diam phasellus vestibulum lorem. In tellus integer '
                     'feugiat scelerisque varius morbi enim nunc faucibus. Ut '
                     'tellus elementum sagittis vitae et leo duis ut. Orci '
                     'dapibus ultrices in iaculis. Sodales ut etiam sit amet '
                     'nisl purus in mollis. Ac turpis egestas sed tempus urna '
                     'et pharetra pharetra massa. Venenatis cras sed felis eget '
                     'velit aliquet sagittis id. Elementum eu facilisis sed '
                     'odio morbi quis commodo odio. Lacus vel facilisis '
                     'volutpat est velit egestas. Nunc sed velit dignissim '
                     'sodales ut eu sem integer. Morbi tristique senectus et '
                     'netus et malesuada fames ac. Tellus at urna condimentum '
                     'mattis pellentesque id. Rhoncus dolor purus non enim. '
                     'Accumsan lacus vel facilisis volutpat est. Augue neque '
                     'gravida in fermentum et.',
             user_id=users[4].id),
        Post(title='Magna ac placerat',
             created_at=generate_random_datetime_start(),
             modified_on=generate_random_datetime_end(),
             content='Diam quis enim lobortis scelerisque fermentum dui '
                     'faucibus. Amet facilisis magna etiam tempor orci eu '
                     'lobortis elementum nibh. Sit amet massa vitae tortor '
                     'condimentum. Luctus venenatis lectus magna fringilla '
                     'urna porttitor rhoncus dolor. Sed lectus vestibulum '
                     'mattis ullamcorper velit sed ullamcorper morbi. Orci a '
                     'scelerisque purus semper eget duis at. Vitae semper quis '
                     'lectus nulla at volutpat diam ut. Cras ornare arcu dui '
                     'vivamus arcu felis bibendum. Et molestie ac feugiat sed '
                     'lectus vestibulum mattis. Habitant morbi tristique '
                     'senectus et netus et malesuada. In iaculis nunc sed '
                     'augue. Aliquet lectus proin nibh nisl condimentum id '
                     'venenatis a. Nulla at volutpat diam ut venenatis tellus '
                     'in. Nulla pellentesque dignissim enim sit amet venenatis '
                     'urna cursus. Molestie a iaculis at erat pellentesque '
                     'adipiscing commodo elit. Sagittis nisl rhoncus mattis '
                     'rhoncus urna neque viverra justo. Curabitur vitae nunc '
                     'sed velit dignissim sodales. Sollicitudin tempor id eu '
                     'nisl nunc.',
             user_id=users[-1].id),
    ])
    try:
        db.session.commit()
        print("Database seeded successfully!")
    except Exception as e:
        print(f"Error committing data: {e}")