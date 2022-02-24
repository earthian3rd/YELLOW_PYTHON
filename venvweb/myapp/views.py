from pydoc_data.topics import topics
from turtle import title
from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
import random
from django.views.decorators.csrf import csrf_exempt
from flask import request  # post방식 오류 우회 방법


# Create your views here.
nextId = 4
topics = [
    {'id': 1, 'title': 'create', 'body': 'create is ...'},
    {'id': 2, 'title': 'read', 'body': 'read is ...'},
    {'id': 3, 'title': 'update', 'body': 'update is ...'}
]


def navList():
    global topics
    nav = ''
    for topic in topics:
        id = topic['id']
        title = topic['title']
        nav += f'<li><a href="/read/{id}/">{id}. {title}</a></li>'
    return nav


def creForm():
    return f'''
    <form action="/create/" method="post">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea name="body" placeholder="body"></textarea></p>
        <p><input type="submit"></p>
    </form>
    '''


def HtmlTemplate(article, id=None):
    bottom = f'''
            <a href="/create/">Create</a>
    '''
    if id != None:
        bottom = f'''
        <form action="/delete/" method="post">
                <a href="/create/">Create</a> | <a href="/update/{id}/">Update</a> | 
                    
                        <input type="hidden" name="id" value="{id}">
                        <input type="submit" value="delete">
                    </form>
        '''
    return f'''
    <html>
    <body>
        <p><a href="/">LOGO</a></p>
        {article}
        <p></p>
        <ul>
            {navList()}
        <ul>
        <p></p>
        <ul>
            <li>
                {bottom}
            </li>
        </ul>
    </body>
    </html>
    '''


def index(request):
    article = '''
    <h1>welcome to index</h1>
    <h2>git master</h2>
    '''
    return HttpResponse(HtmlTemplate(article))


def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            title = topic['title']
            body = topic['body']
            article = f'''
            <h1>{title}</h1>
            <h3>{body}</h3>
            '''
    return HttpResponse(HtmlTemplate(article, id))


@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = creForm()
        return HttpResponse(HtmlTemplate(article))
    elif request.method == 'POST':
        id = nextId
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id": id, "title": title, "body": body}
        topics.append(newTopic)
        url = f'/read/{str(id)}'
        nextId = id + 1
        return redirect(url)


@csrf_exempt
def update(request, id):
    global topics
    if request.method == 'GET':
        for topic in topics:
            if topic['id'] == int(id):
                title = topic['title']
                body = topic['body']
        article = f'''
        <form action="/update/{id}/" method="post">
            <p><input type="text" name="title" placeholder="title" value="{title}"></p>
            <p><textarea name="body" placeholder="body">{body}</textarea></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(HtmlTemplate(article, id))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        for topic in topics:
            if topic['id'] == int(id):
                topic['title'] = title
                topic['body'] = body
        return redirect(f'/read/{id}/')


@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')


##추가한 코드##