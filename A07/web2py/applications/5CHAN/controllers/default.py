# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    threads = db(db.thread).select()
    records = SQLFORM.grid(db.thread, db.thread(), deletable=True)
    form = SQLFORM(db.thread).process()
    form.element(_type='submit')['_value'] = T("Thread erstellen")
    posts = db().select(db.post.ALL)
    if form.accepted:
        redirect(URL("index.html"), client_side=True)
        response.flash = T("Neuer Thread wurde erstellt")
    return dict(threads=threads, records=records,form=form, posts=posts)

def delete():
    pass

def create_post():
    thread = request.args[0]
    back_button = A(T('Back'), _href=URL('default', 'index', user_signature=True), _class='btn')
    form=SQLFORM(db.post, fields=['post_text','post_user'])
    form.vars.thread_id = thread
    form.process()
    return dict(form=form,thread=thread,back_button=back_button)

def delete_post():
    post = request.args[0]
    db(db.post.id==post).delete()
    redirect(URL("index.html"), client_side=True)
    
def update_post():
    post = request.args[0]
    record = db.post(post)
    form=SQLFORM(db.post, record, fields=['post_text'])
    form.vars.thread_id = request.args[2]
    form.vars.post_user = request.args[1]
    form.process()
    db(db.post.id==request.args[3]).delete()
    back_button = A(T('Back'), _href=URL('default', 'index', user_signature=True), _class='btn')
    return dict(form=form, back_button=back_button)

def delete_thread():
    thread = request.args[0]
    db(db.thread.id==thread).delete()
    redirect(URL("index.html"), client_side=True)
