"""init

Revision ID: f9c634db477d
Revises: 
Create Date: 2023-01-25 22:54:54.612371

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'f9c634db477d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # TODO FIX error for postgis install
    # op.execute("CREATE EXTENSION IF NOT EXISTS postgis")
    
    peak_table = op.create_table(
        'peak',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('lat', sa.Float(), nullable=False),
        sa.Column('lon', sa.Float(), nullable=False),
        sa.Column('altitude', sa.Float(), nullable=False),
        sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_peak_id'), 'peak', ['id'], unique=False)
    op.create_index(op.f('ix_peak_lat'), 'peak', ['lat'], unique=False)
    op.create_index(op.f('ix_peak_lon'), 'peak', ['lon'], unique=False)
    op.create_index(op.f('ix_peak_altitude'), 'peak', ['altitude'], unique=False)
    op.create_index(op.f('ix_peak_name'), 'peak', ['name'], unique=False)
    # op.add_column('peak', sa.Column('location', sa.dialects.postgresql.POINT(), nullable=True))

    data = [
        {"lat": 45.22, "lon": -121.83, "altitude": 543.2, "name": "Mt. Hood"},
        {"lat": 37.737636, "lon": -119.572033, "altitude": 4200.1, "name": "Half Dome"},
        {"lat": 20.005039, "lon": -155.824615, "altitude": 4205.2, "name": "Mauna Kea"},
        {"lat": 40.748817, "lon": -73.985428, "altitude": 8.8, "name": "Mount Everest"}
    ]

    op.bulk_insert(peak_table, data)

def downgrade():
    op.drop_table('peak')
    # op.execute("DROP EXTENSION IF EXISTS postgis")
