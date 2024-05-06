from unittest import TestCase

from app import app
from models import db, User, Post

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sqla_intro_test'
app.config['SQLALCHEMY_ECHO'] = True

with app.app_context():
    db.drop_all()
    db.create_all()


class UserModelTests(TestCase):
    def setUp(self):
        self.user_id = 0
        with app.app_context():
            with app.test_client() as client:
                Post.query.delete()
                User.query.delete()
                user = User(first_name="Tracy", middle_name="", last_name=
                            "Rera", image_url="https://via.placeholder.com/50")
                db.session.add(user)
                db.session.commit()
                post = Post(title='Mauris cursus mattis molestie',
                     created_at="2022-01-30 04:47:04",
                     content='Lorem ipsum dolor sit amet',
                     user_id=user.id)
                db.session.add(post)
                db.session.commit()
                self.post_id = post.id
                self.user_id = user.id

    def tearDown(self):
        """Clean up any fouled transaction."""
        with app.app_context():
            with app.test_client() as client:
                db.session.rollback()

    def test_show_404(self):
        with app.app_context():
            with app.test_client() as client:
                resp = client.get(f"/posts/{self.post_id}ik")
                html = resp.get_data(as_text=True)
                self.assertEqual(resp.status_code, 404)
                self.assertIn("Mauris cursus mattis molestie", html)
                db.session.rollback()

    def test_show_post(self):
        with app.app_context():
            with app.test_client() as client:
                resp = client.get(f"/posts/{self.post_id}")
                html = resp.get_data(as_text=True)
                self.assertEqual(resp.status_code, 200)
                self.assertIn("Mauris cursus mattis molestie", html)
                db.session.rollback()

    def test_new_post_show(self):
        with app.app_context():
            with app.test_client() as client:
                resp = client.get(f"/users/{self.user_id}/posts/new")
                html = resp.get_data(as_text=True)
                self.assertEqual(resp.status_code, 200)
                self.assertIn("NEW POST", html)
                db.session.rollback()

    def test_edit_post(self):
        with app.app_context():
            with app.test_client() as client:
                d = {"title": "MODIFIEDTITLE",
                     "content": "MODIFIEDCONTENT"}
                resp2 = client.post(f"/posts/{self.post_id}/edit", data=d,
                                    follow_redirects=True)
                resp2.get_data(as_text=True)
                html2 = resp2.get_data(as_text=True)

                resp = client.get("/posts")
                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertIn("MODIFIEDTITLE", html2)
                self.assertIn("MODIFIEDCONTENT", html2)
                self.assertIn("MODIFIEDTITLE", html)
                self.assertIn("MODIFIEDCONTENT", html)

    def test_list_users_show(self):
        with app.app_context():
            with app.test_client() as client:
                resp = client.get("/users")
                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertIn('Tracy', html)

    def test_form_adduser_showing(self):
        with app.app_context():
            with app.test_client() as client:
                resp = client.get("/users/new")
                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertIn("ADD USER", html)

    def test_add_user_displayed(self):
        with app.app_context():
            with app.test_client() as client:
                d = {"first_name": "Treyer",
                     "middle_name": "",
                     "last_name": "Darell",
                     "image_url": ""}
                resp2 = client.post("/users/new", data=d, follow_redirects=True)
                resp2.get_data(as_text=True)

                resp = client.get("/users", follow_redirects=True)
                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertIn("Treyer", html)

    def test_show_user_displayed(self):
        with app.app_context():
            with app.test_client() as client:
                resp = client.get(f"/users/{self.user_id}")
                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertIn('<h2>Tracy Rera</h2>', html)

    def test_edit_user_form_displayed(self):
        with app.app_context():
            with app.test_client() as client:
                resp = client.get(f"/users/{self.user_id}/edit")
                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertIn("Tracy", html)

    def test_edit_user_change(self):
        with app.app_context():
            with app.test_client() as client:
                d = {"first_name": "Treyer",
                     "middle_name": None,
                     "last_name": "Darell",
                     "image_url": "https://via.placeholder.com/50"}
                resp2 = client.post(f"/users/{self.user_id}/edit", data=d,
                                    follow_redirects=True)
                resp = client.get("/users", follow_redirects=True)
                resp2.get_data(as_text=True)
                html = resp.get_data(as_text=True)
                self.assertEqual(resp.status_code, 200)
                self.assertIn("Treyer", html)

    def test_delete_post(self):
        with app.app_context():
            with app.test_client() as client:
                resp2 = client.post(f"/posts/{self.post_id}/delete",
                                    follow_redirects=True)
                resp2.get_data(as_text=True)
                html2 = resp2.get_data(as_text=True)

                resp = client.get("/posts")
                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertNotIn("Mauris cursus", html)

    def test_delete_user(self):
        with app.app_context():
            with app.test_client() as client:
                resp = client.post(f"/users/{self.user_id}/delete",
                                   follow_redirects=True)

                resp = client.get("/users")
                html = resp.get_data(as_text=True)

                self.assertEqual(resp.status_code, 200)
                self.assertNotIn("Tracy", html)