# MIT License
#
# Copyright (c) 2022 Clivern
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import argparse
import logging
import sys
import time

from ghbot import __version__
from .bot import Bot


__author__ = "Clivern"
__copyright__ = "Clivern"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


def follow(access_token, followers_count, interval):
    bot = Bot(access_token)

    for username in bot.get_random_users(followers_count):
        _logger.info("follow {}".format(username))
        bot.follow_username(username)
        time.sleep(interval)


def clean(access_token, interval):
    bot = Bot(access_token)

    followrs = [bot.client.get_user("clivern")]

    for username in bot.get_followers():
        followrs.append(username)

    following = bot.get_following()

    for username in bot.get_following():
        if username not in followrs:
            _logger.info("unfollow {}".format(username))
            bot.unfollow_username(username)
        else:
            _logger.info("{} is one of your followers".format(username))
        time.sleep(interval)


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Just a Github Bot")
    parser.add_argument(
        "--version",
        action="version",
        version="ghbot {ver}".format(ver=__version__),
    )

    parser.add_argument(
        dest="operation",
        help="The command to execute",
        type=str, metavar="STR"
    )

    parser.add_argument(
        dest="access_token",
        help="The github access token",
        type=str,
        metavar="STR"
    )
    parser.add_argument(
        "--c",
        dest="followers_count",
        help="The number of followers",
        type=int,
        metavar="INT",
        default=1000
    )

    parser.add_argument(
        "--i",
        dest="interval",
        help="Time interval in seconds",
        type=int,
        metavar="INT",
        default=2
    )

    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args):
    args = parse_args(args)
    setup_logging(args.loglevel)

    _logger.info("Bot started")

    if args.operation == "follow":
        while True:
            try:
                follow(args.access_token, args.followers_count, args.interval)
                break
            except Exception:
                _logger.info("Rate limit reached, hold on for a while")
                time.sleep(args.interval + 60)

    elif args.operation == "clean":
        while True:
            try:
                clean(args.access_token, args.interval)
                break
            except Exception:
                _logger.info("Rate limit reached, hold on for a while")
                time.sleep(args.interval + 60)

    _logger.info("Bot finished")


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
