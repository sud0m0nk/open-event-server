"""empty message

Revision ID: c8561d8684da
Revises: 24da7df1e00e
Create Date: 2017-06-29 23:49:10.172941

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'c8561d8684da'
down_revision = '1d4ae4569284'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sessions', 'slides', new_column_name='slides_url')
    op.alter_column('sessions', 'audio', new_column_name='audio_url')
    op.alter_column('sessions', 'video', new_column_name='video_url')

    op.alter_column('sessions_version', 'slides', new_column_name='slides_url')
    op.alter_column('sessions_version', 'audio', new_column_name='audio_url')
    op.alter_column('sessions_version', 'video', new_column_name='video_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sessions', 'video_url', new_column_name='video')
    op.alter_column('sessions', 'audio_url', new_column_name='audio')
    op.alter_column('sessions', 'slides_url', new_column_name='slides')

    op.alter_column('sessions_version', 'video_url', new_column_name='video')
    op.alter_column('sessions_version', 'slides_url', new_column_name='slides')
    op.alter_column('sessions_version', 'audio_url', new_column_name='audio')
    # ### end Alembic commands ###
