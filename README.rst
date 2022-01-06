.. image:: https://img.shields.io/pypi/v/ghbot.svg
    :alt: PyPI-Server
    :target: https://pypi.org/project/ghbot/
.. image:: https://github.com/Clivern/ghbot/actions/workflows/ci.yml/badge.svg
    :alt: Build Status
    :target: https://github.com/Clivern/ghbot/actions/workflows/ci.yml

|

==========
Github Bot
==========

    Github Follow Bot to Get More Followers in Python


To Use the bot, follow the following steps

1. Create a Python virtual environment

```
$ python3 -m venv venv
$ source venv/bin/activate
```

2. Install ghbot package with pip

```
$ pip install ghbot
```

3. Create access token https://github.com/settings/tokens/new with user permissions (read:user, user:email, user:follow)

4. Run the bot with the access token and the number of followers.

```
$ python -m ghbot.cli $access-token-here 1000 -v
```

5. Then wait or run as a background process
