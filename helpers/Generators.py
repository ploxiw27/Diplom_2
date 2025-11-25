import random
import string

def create_random_email():
    domains = ["example.com", "test.com", "demo.com"]
    email = ''.join(random.choices(string.ascii_lowercase, k=10)) + "@" + random.choice(domains)
    return email

def create_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

def create_random_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))