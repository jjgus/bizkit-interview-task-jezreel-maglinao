from ast import arg
from pickle import TRUE
from flask import Blueprint, request


from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):

    print(args)
    if (bool(args) == False):
        return USERS
    returnUser = []
    for user in USERS:
        for key in args.keys():
            if key == 'id' and user[key] == args[key]:
                returnUser.append(user)
                print(returnUser)
                break
            elif key == 'age' and user[key] >= int(args[key])-1 and user[key] <= int(args[key])+1:
                returnUser.append(user)
                break
            elif key != 'age' and args[key] in user[key]:
                returnUser.append(user)
                break
   
    return returnUser
