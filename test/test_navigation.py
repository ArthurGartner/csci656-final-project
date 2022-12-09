import pytest
import django.test.client

def test_with_index_page(client):
    response = client.get('/')
    text = b'Tracking multiple job applications can be difficult and time-consuming'
    assert text in response.content


def test_with_about_page(client):
    response = client.get('/about/')
    text = b'About Page'
    assert text in response.content


def test_with_checklist_page(client):
    response = client.get('/checklist/')
    text = b'Checklist Page'
    assert text in response.content


def test_with_checklist_page(client):
    response = client.get('/futurework/')
    text = b'Future Work Page'
    assert text in response.content


def test_with_login_page(client):
    response = client.get('/login/')
    text = b'Login'
    assert text in response.content


def test_with_signup_page(client):
    response = client.get('/signup/')
    text = b'Sign Up'
    assert text in response.content


def test_unauthorized_redirect(client):
    response = client.get('/myjobs/')
    text = b'Login'
    assert text in response.content

