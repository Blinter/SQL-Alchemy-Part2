"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone, UTC
import tzlocal
db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Post(db.Model):
    """User"""

    __tablename__ = "posts"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    title = db.Column(db.String(128),
                      nullable=False,
                      default='Lorem Ipsum')

    content = db.Column(db.String(65535),
                        nullable=False,
                        default='Lorem Ipsum')

    created_at = db.Column(db.TIMESTAMP,
                           nullable=False,
                           default=datetime.now(UTC))

    modified_on = db.Column(db.TIMESTAMP,
                            nullable=True,
                            default=datetime.now(UTC))

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.id'))

    user = db.relationship("User", backref="posts")

    @staticmethod
    def get_friendly(timediff):
        seconds = timediff.total_seconds()
        minutes = int(seconds / 60)
        hours = int(minutes / 60)
        days = int(hours / 24)
        if days > 0:
            return f"{days} day{'s' if days > 1 else ''} ago"
        elif hours > 0:
            return f"{hours} hour{'s' if hours > 1 else ''} ago"
        elif minutes > 0:
            return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
        else:
            return "Just now"

    @property
    def friendly_created_at(self):
        return Post.get_friendly(datetime.now(UTC) -
                                 datetime.fromisoformat(
                                     self.created_at.replace(
                                         tzinfo=tzlocal.get_localzone())
                                     .isoformat()))

    @property
    def friendly_modified_on(self):
        return Post.get_friendly(datetime.now(UTC) -
                                 datetime.fromisoformat(
                                     self.modified_on.replace(
                                         tzinfo=tzlocal.get_localzone())
                                     .isoformat()))

    @property
    def homepage_content(self):
        return ((f"{self.content[:252]}" if len(self.content) > 255 else
                 self.content))

    @property
    def homepage_minified(self):
        return len(self.content) > 252

    def __repr__(self):
        """Show info about user."""

        return (f"<Post ID={self.id} " +
                f"Title={self.title[:32]} " +
                f"Content=" +
                ("[truncated]" if len(self.content) > 32 else "") +
                f"{self.content[:32]} " +
                f"Created At={self.created_at}>")


class User(db.Model):
    """User"""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.String(50),
                           nullable=False)

    middle_name = db.Column(db.String(50),
                            nullable=True)

    last_name = db.Column(db.String(50),
                          nullable=False)

    image_url = db.Column(db.String(255),
                          nullable=False,
                          default='https://via.placeholder.com/30')

    created_posts = db.relationship('Post', backref='created_posts',
                                    cascade="all, delete")

    def get_full_name(self):
        return self.first_name + \
            (" " + self.middle_name if self.middle_name is
                not None and len(self.middle_name) > 0
                else "") + \
            " " + self.last_name

    @property
    def full_name(self):
        return self.get_full_name()

    def __repr__(self):
        """Show info about user."""

        return (f"<User ID={self.id} " +
                f"First Name={self.first_name} " +
                (f"Middle Name={self.middle_name} " if self.middle_name is
                    not None and len(self.middle_name) > 0 else "") +
                f"Last Name={self.last_name} " +
                f"Image URL={self.image_url}>")
