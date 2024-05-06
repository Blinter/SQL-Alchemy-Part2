from unittest import TestCase
from app import app
from models import db, User, Post
from seed import generate_random_datetime_start, generate_random_datetime_end

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sqla_intro_test'
app.config['SQLALCHEMY_ECHO'] = False


class UserModelTestCase(TestCase):
    """Tests for model for User."""

    def setUp(self):
        """Clean up any existing Users."""

        with app.app_context():
            db.drop_all()
            db.create_all()
            self.client = app.test_client()

    def tearDown(self):
        """Clean up any fouled transaction."""
        with app.app_context():
            db.session.rollback()

    def test_no_middle_name(self):
        user = User(first_name="Tracy", middle_name="", last_name="Rera",
             image_url="https://via.placeholder.com/50")
        self.assertEqual(user.full_name, "Tracy Rera")

    def test_middle_name(self):
        user = User(first_name="Tracy", middle_name="A", last_name="Rera",
             image_url="https://via.placeholder.com/50")
        self.assertEqual(user.full_name, "Tracy A Rera")

    def test_repl(self):
        user = User(first_name="Tracy", middle_name="A", last_name="Rera",
             image_url="https://via.placeholder.com/50")
        self.assertEqual(str(user),
                         "<User ID=None First Name=Tracy Middle Name=A "
                         "Last Name=Rera Image URL="
                         "https://via.placeholder.com/50>")

    def test_create_user(self):
        user1 = User(first_name="Alice", last_name="Smith")
        with app.app_context():
            db.session.add(user1)
            self.assertEqual(str(User.query.first()),
                         "<User ID=1 First Name=Alice Last Name="
                         "Smith Image URL=https://via.placeholder.com/30>")
    def test_create_user_delete(self):
        user1 = User(first_name="Alice", last_name="Smith")
        with app.app_context():
            db.session.add(user1)
            db.session.commit()
            self.assertEqual(str(User.query.first()),
                         "<User ID=1 First Name=Alice Last Name="
                         "Smith Image URL=https://via.placeholder.com/30>")
            db.session.delete(User.query.first())
            db.session.commit()
            self.assertFalse(bool(User.query.first()))

    def test_serial_user_delete(self):
        with app.app_context():
            user1 = User(first_name="Alice", last_name="Smith")
            db.session.add(user1)
            db.session.commit()
            self.assertEqual(str(User.query.first()),
                         "<User ID=1 First Name=Alice Last Name="
                         "Smith Image URL=https://via.placeholder.com/30>")
            db.session.delete(User.query.first())
            db.session.commit()
            self.assertFalse(bool(User.query.first()))
            user1 = User(first_name="Alice", last_name="Smith")
            db.session.add(user1)
            db.session.commit()
            self.assertEqual(str(User.query.first()),
                         "<User ID=2 First Name=Alice Last Name="
                         "Smith Image URL=https://via.placeholder.com/30>")
            db.session.delete(User.query.first())
            db.session.commit()
            self.assertFalse(bool(User.query.first()))


class PostModelTestCase(TestCase):
    """Tests for model for Post."""

    def setUp(self):
        """Clean up any existing Post."""

        with app.app_context():
            db.drop_all()
            db.create_all()
            self.client = app.test_client()

    def tearDown(self):
        """Clean up any fouled transaction."""
        with app.app_context():
            db.session.rollback()

    def test_repl(self):
        with app.app_context():
            user1 = User(first_name="Alice", last_name="Smith")
            db.session.add(user1)
            db.session.commit()
            self.assertEqual(str(User.query.first()),
                         "<User ID=1 First Name=Alice Last Name="
                         "Smith Image URL=https://via.placeholder.com/30>")
            newUser = User.query.first()
            db.session.add(Post(title='Mauris cursus mattis molestie',
                                created_at="2022-01-30 04:47:04",
                                content='Lorem ipsum dolor sit amet',
                                user_id=newUser.id))
            db.session.commit()
            post = Post.query.first()
            self.assertTrue(bool(post))
            self.assertEquals(str(post), "<Post ID=1 Title=Mauris "
                                         "cursus mattis molestie Content=Lorem "
                                         "ipsum dolor sit amet Created At="
                                         "2022-01-30 04:47:04>")

    def test_cascade_post_delete(self):
        with app.app_context():
            user1 = User(first_name="Alice", last_name="Smith")
            db.session.add(user1)
            db.session.commit()
            self.assertEqual(str(User.query.first()),
                         "<User ID=1 First Name=Alice Last Name="
                         "Smith Image URL=https://via.placeholder.com/30>")
            newUser = User.query.first()
            db.session.add(Post(title='Mauris cursus mattis molestie',
                                created_at=generate_random_datetime_start(),
                                modified_on=generate_random_datetime_end(),
                                content='Lorem ipsum dolor sit amet',
                                user_id=newUser.id))
            db.session.commit()
            self.assertTrue(bool(Post.query.first()))
            db.session.delete(User.query.first())
            db.session.commit()
            self.assertFalse(bool(User.query.first()))
            self.assertFalse(bool(Post.query.first()))

            def test_serial_user_delete(self):
                with app.app_context():
                    user1 = User(first_name="Alice", last_name="Smith")
                    db.session.add(user1)
                    db.session.commit()
                    self.assertEqual(str(User.query.first()),
                                     "<User ID=1 First Name=Alice Last Name="
                                     "Smith Image URL=https://via.placeholder.com/30>")
                    db.session.delete(User.query.first())
                    db.session.commit()
                    self.assertFalse(bool(User.query.first()))
                    user1 = User(first_name="Alice", last_name="Smith")
                    db.session.add(user1)
                    db.session.commit()
                    self.assertEqual(str(User.query.first()),
                                     "<User ID=2 First Name=Alice Last Name="
                                     "Smith Image URL=https://via.placeholder.com/30>")
                    db.session.delete(User.query.first())
                    db.session.commit()
                    self.assertFalse(bool(User.query.first()))

    def test_serial_post_delete(self):
        with app.app_context():
            user1 = User(first_name="Alice", last_name="Smith")
            db.session.add(user1)
            db.session.commit()
            self.assertEqual(str(User.query.first()),
                         "<User ID=1 First Name=Alice Last Name="
                         "Smith Image URL=https://via.placeholder.com/30>")
            newUser = User.query.first()
            db.session.add(Post(title='Mauris cursus mattis molestie',
                                created_at="2022-01-30 04:47:04",
                                content='Lorem ipsum dolor sit amet',
                                user_id=newUser.id))
            db.session.commit()
            post = Post.query.first()
            self.assertTrue(bool(post))
            self.assertEquals(str(post), "<Post ID=1 Title=Mauris "
                                         "cursus mattis molestie Content=Lorem "
                                         "ipsum dolor sit amet Created At="
                                         "2022-01-30 04:47:04>")
            db.session.delete(Post.query.first())
            db.session.commit()
            self.assertFalse(bool(Post.query.first()))
            db.session.add(Post(title='Mauris cursus mattis molestie',
                                created_at="2022-01-30 04:47:04",
                                content='Lorem ipsum dolor sit amet',
                                user_id=newUser.id))
            db.session.commit()
            post = Post.query.first()
            self.assertTrue(bool(post))
            self.assertEquals(str(post), "<Post ID=2 Title=Mauris "
                                         "cursus mattis molestie Content=Lorem "
                                         "ipsum dolor sit amet Created At="
                                         "2022-01-30 04:47:04>")