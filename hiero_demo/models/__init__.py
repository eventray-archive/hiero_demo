from sqlalchemy.ext.declarative import declarative_base
from hiero.models               import GroupMixin
from hiero.models               import UserMixin
from hiero.models               import UserGroupMixin
from hiero.models               import ActivationMixin
from hiero.models               import BaseModel
from hiero.models.blog          import EntryTagMixin
from hiero.models.blog          import TagMixin
from hiero.models.blog          import CategoryMixin
from hiero.models.blog          import EntryMixin
from hiero.models.blog          import SeriesMixin
from zope.sqlalchemy            import ZopeTransactionExtension

from sqlalchemy.orm import (
    scoped_session
    , sessionmaker
)

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

Base = declarative_base(cls=BaseModel)

class User(UserMixin, Base):
    pass

class Group(GroupMixin, Base):
    pass

class UserGroup(UserGroupMixin, Base):
    pass

class Activation(ActivationMixin, Base):
    pass

class EntryTag(EntryTagMixin, Base):
    pass

class Tag(TagMixin, Base):
    pass

class CategoryMixin(CategoryMixin, Base):
    pass

class EntryMixin(EntryMixin, Base):
    pass

class SeriesMixin(SeriesMixin, Base):
    pass
