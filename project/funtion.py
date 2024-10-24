import json

class user:
    def __init__(self):

        pass

    def join(self, id, pwd, tel):
        user_info_form = {}
        user_info_form["id"] = id
        user_info_form["pwd"] = pwd
        user_info_form["tel"] = tel

        with open("member.json", "r") as f:
            memberList = json.load(f)

        for member in memberList:
            if member["id"] == id:
                return False

        return True

    def search(self, id, tel):
        pwd = ""

        f = open("member.json", "r")
        memberList = f.readlines()
        f.close()

        print(memberList)

        #memberList = dict(memberList)
        #print(memberList)

        return True, id, pwd

