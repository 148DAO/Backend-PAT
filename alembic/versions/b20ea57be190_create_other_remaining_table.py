"""create other remaining table

Revision ID: b20ea57be190
Revises: 9f1fac4f399e
Create Date: 2024-08-05 17:17:28.540332

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b20ea57be190'
down_revision: Union[str, None] = '9f1fac4f399e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=63), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_course_id'), 'course', ['id'], unique=False)
    op.create_table('learning_resource',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=63), nullable=False),
    sa.Column('url', sa.String(length=63), nullable=False),
    sa.Column('description', sa.String(length=511), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_learning_resource_id'), 'learning_resource', ['id'], unique=False)
    op.create_table('learning_resource_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=63), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_learning_resource_type_id'), 'learning_resource_type', ['id'], unique=False)
    op.create_table('ai_query',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ai_query_id'), 'ai_query', ['id'], unique=False)
    op.create_table('notification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=255), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notification_id'), 'notification', ['id'], unique=False)
    op.create_table('reminder',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=255), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reminder_id'), 'reminder', ['id'], unique=False)
    op.create_table('subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=63), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subject_course_id'), 'subject', ['course_id'], unique=False)
    op.create_index(op.f('ix_subject_id'), 'subject', ['id'], unique=False)
    op.create_table('ai_response',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('query_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['query_id'], ['ai_query.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ai_response_id'), 'ai_response', ['id'], unique=False)
    op.create_table('lesson',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=63), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('duration_in_minutes', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lesson_id'), 'lesson', ['id'], unique=False)
    op.create_index(op.f('ix_lesson_subject_id'), 'lesson', ['subject_id'], unique=False)
    op.create_table('ai_response_feedback',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('response_id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['response_id'], ['ai_response.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_ai_response_feedback_id'), 'ai_response_feedback', ['id'], unique=False)
    op.create_table('performance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('feedback', sa.String(length=1023), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.ForeignKeyConstraint(['lesson_id'], ['lesson.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_performance_course_id'), 'performance', ['course_id'], unique=False)
    op.create_index(op.f('ix_performance_id'), 'performance', ['id'], unique=False)
    op.create_index(op.f('ix_performance_lesson_id'), 'performance', ['lesson_id'], unique=False)
    op.create_index(op.f('ix_performance_user_id'), 'performance', ['user_id'], unique=False)
    op.create_table('progress',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('lesson_id', sa.Integer(), nullable=False),
    sa.Column('completition_status', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('completition_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.ForeignKeyConstraint(['lesson_id'], ['lesson.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_progress_course_id'), 'progress', ['course_id'], unique=False)
    op.create_index(op.f('ix_progress_id'), 'progress', ['id'], unique=False)
    op.create_index(op.f('ix_progress_lesson_id'), 'progress', ['lesson_id'], unique=False)
    op.create_index(op.f('ix_progress_user_id'), 'progress', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_progress_user_id'), table_name='progress')
    op.drop_index(op.f('ix_progress_lesson_id'), table_name='progress')
    op.drop_index(op.f('ix_progress_id'), table_name='progress')
    op.drop_index(op.f('ix_progress_course_id'), table_name='progress')
    op.drop_table('progress')
    op.drop_index(op.f('ix_performance_user_id'), table_name='performance')
    op.drop_index(op.f('ix_performance_lesson_id'), table_name='performance')
    op.drop_index(op.f('ix_performance_id'), table_name='performance')
    op.drop_index(op.f('ix_performance_course_id'), table_name='performance')
    op.drop_table('performance')
    op.drop_index(op.f('ix_ai_response_feedback_id'), table_name='ai_response_feedback')
    op.drop_table('ai_response_feedback')
    op.drop_index(op.f('ix_lesson_subject_id'), table_name='lesson')
    op.drop_index(op.f('ix_lesson_id'), table_name='lesson')
    op.drop_table('lesson')
    op.drop_index(op.f('ix_ai_response_id'), table_name='ai_response')
    op.drop_table('ai_response')
    op.drop_index(op.f('ix_subject_id'), table_name='subject')
    op.drop_index(op.f('ix_subject_course_id'), table_name='subject')
    op.drop_table('subject')
    op.drop_index(op.f('ix_reminder_id'), table_name='reminder')
    op.drop_table('reminder')
    op.drop_index(op.f('ix_notification_id'), table_name='notification')
    op.drop_table('notification')
    op.drop_index(op.f('ix_ai_query_id'), table_name='ai_query')
    op.drop_table('ai_query')
    op.drop_index(op.f('ix_learning_resource_type_id'), table_name='learning_resource_type')
    op.drop_table('learning_resource_type')
    op.drop_index(op.f('ix_learning_resource_id'), table_name='learning_resource')
    op.drop_table('learning_resource')
    op.drop_index(op.f('ix_course_id'), table_name='course')
    op.drop_table('course')
    # ### end Alembic commands ###
