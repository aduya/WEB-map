from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
case = Table('case', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('markerxy', String(length=64)),
    Column('place', String(length=64)),
    Column('Casetype', String(length=64)),
    Column('Casework', String(length=64)),
    Column('Casenote', String(length=64)),
    Column('Showpic', String(length=64), default=ColumnDefault('default.png')),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['case'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['case'].drop()
