# -*- coding: utf-8 -*

db.define_table(
    'thread',
    Field('name', notnull = True),
    format = '%(name)s'
)

db.define_table(
   'post',
   Field('post_text', notnull = True),
   Field('post_user'),
   Field('post_time', default=request.now),
   Field('thread_id','references thread'),
   format = '%(name)s'
)
