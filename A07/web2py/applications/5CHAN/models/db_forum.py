# -*- coding: utf-8 -*-
db.define_table(
    'forum_user',
    Field('name', unique=True),
    Field('mail', unique=True),
    Field('pw', 'password'),
    lazy_tables = False
)

db.define_table(
    'thread',
    Field('name', notnull = True),
    Field('user_id', 'references forum_user'),
    format = '%(name)s',
    lazy_tables = False
)

db.define_table(
   'post',
   Field('post_text', notnull = True),
   Field('post_time'),
   Field('thread_id','references thread'),
   format = '%(name)s',
   lazy_tables = False
)
