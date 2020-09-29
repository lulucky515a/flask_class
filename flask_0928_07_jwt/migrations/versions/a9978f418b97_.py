"""empty message

Revision ID: a9978f418b97
Revises: 
Create Date: 2020-09-26 16:17:09.023907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9978f418b97'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('envs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True, comment='环境名称'),
    sa.Column('base_url', sa.String(length=200), nullable=True, comment='请求base url'),
    sa.Column('desc', sa.String(length=200), nullable=True, comment='简要描述'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True, comment='项目名称'),
    sa.Column('leader', sa.String(length=50), nullable=True, comment='项目负责人'),
    sa.Column('tester', sa.String(length=50), nullable=True, comment='项目测试人员'),
    sa.Column('programmer', sa.String(length=50), nullable=True, comment='开发人员'),
    sa.Column('publish_app', sa.String(length=100), nullable=True, comment='发布应用'),
    sa.Column('desc', sa.String(length=200), nullable=True, comment='简要描述'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('reports',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True, comment='报告名称'),
    sa.Column('result', sa.SmallInteger(), nullable=True, comment='执行结果'),
    sa.Column('count', sa.Integer(), nullable=True, comment='总用例数'),
    sa.Column('success', sa.Integer(), nullable=True, comment='成功总数'),
    sa.Column('html', sa.Text(), nullable=True, comment='报告HTML源码'),
    sa.Column('summary', sa.Text(), nullable=True, comment='报告详情'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('summary',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('user', sa.String(length=200), nullable=True, comment='用户名称'),
    sa.Column('statistics', sa.Integer(), nullable=True, comment='测试信息'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('username', sa.String(length=20), nullable=False, comment='用户名'),
    sa.Column('password', sa.String(length=512), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('debug_talks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True, comment='debugtalk文件名称'),
    sa.Column('debugtalk', sa.Text(), nullable=True, comment='debugtalk.py文件'),
    sa.Column('project_id', sa.Integer(), nullable=True, comment='所属项目'),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('interfaces',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True, comment='接口名称'),
    sa.Column('tester', sa.String(length=50), nullable=True, comment='测试人员'),
    sa.Column('desc', sa.String(length=200), nullable=True, comment='简要描述'),
    sa.Column('project_id', sa.Integer(), nullable=True, comment='所属项目'),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('testsuits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True, comment='套件名称'),
    sa.Column('project_id', sa.Integer(), nullable=True, comment='所属项目'),
    sa.Column('include', sa.String(length=50), nullable=True, comment='包含的接口'),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('configures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True, comment='配置名称'),
    sa.Column('interface_id', sa.Integer(), nullable=True, comment='所属接口'),
    sa.Column('author', sa.String(length=50), nullable=True, comment='编写人员'),
    sa.Column('request', sa.Text(), nullable=True, comment='请求信息'),
    sa.ForeignKeyConstraint(['interface_id'], ['interfaces.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('testcases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.SmallInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True, comment='用例名称'),
    sa.Column('interface_id', sa.Integer(), nullable=True, comment='所属接口'),
    sa.Column('include', sa.String(length=50), nullable=True, comment='用例执行前置顺序'),
    sa.Column('author', sa.String(length=50), nullable=True, comment='编写人员'),
    sa.Column('request', sa.String(length=50), nullable=True, comment='请求信息'),
    sa.ForeignKeyConstraint(['interface_id'], ['interfaces.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('testcases')
    op.drop_table('configures')
    op.drop_table('testsuits')
    op.drop_table('interfaces')
    op.drop_table('debug_talks')
    op.drop_table('user')
    op.drop_table('summary')
    op.drop_table('reports')
    op.drop_table('projects')
    op.drop_table('envs')
    # ### end Alembic commands ###
