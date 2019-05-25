#! /usr/bin/env python

import argparse
import getpass

from sys import exit
from deletefb.tools.login import login
import deletefb.tools.wall as wall
import deletefb.tools.likes as likes

def run_delete():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-M",
        "--mode",
        required=False,
        default="wall",
        dest="mode",
        type=str,
        choices=["wall", "unlike_pages"],
        help="The mode you want to run in. Default is `wall' which deletes wall posts"
    )

    parser.add_argument(
        "-E",
        "--email",
        required=True,
        dest="email",
        type=str,
        help="Your email address associated with the account"
    )

    parser.add_argument(
        "-P",
        "--password",
        required=False,
        dest="password",
        type=str,
        help="Your Facebook password"
    )

    parser.add_argument(
        "-U",
        "--profile-url",
        required=True,
        dest="profile_url",
        type=str,
        help="The link to your Facebook profile, e.g. https://www.facebook.com/your.name"
    )

    parser.add_argument(
        "-F",
        "--two-factor",
        required=False,
        dest="two_factor_token",
        type=str,
        help="The code generated by your 2FA device for Facebook"
    )

    parser.add_argument(
        "-H",
        "--headless",
        action="store_true",
        dest="is_headless",
        default=False,
        help="Run browser in headless mode (no gui)"
    )

    parser.add_argument(
        "-Y",
        "--year",
        required=False,
        dest="year",
        type=str,
        help="The year(s) you want posts deleted."
    )

    args = parser.parse_args()

    args_user_password = args.password or getpass.getpass('Enter your password: ')

    driver = login(
        user_email_address=args.email,
        user_password=args_user_password,
        is_headless=args.is_headless,
        two_factor_token=args.two_factor_token
    )

    if args.mode == "wall":
        wall.delete_posts(driver,
                          args.profile_url,
                          year=args.year)
    elif args.mode == "unlike_pages":
        likes.unlike_pages(driver, args.profile_url)
    else:
        print("Please enter a valid mode")
        exit(1)

if __name__ == "__main__":
    run_delete()
