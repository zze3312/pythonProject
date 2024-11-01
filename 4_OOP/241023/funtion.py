import json

class user:
    def __init__(self):

        pass

    def join(self, id, pwd, tel):
        user_info_form = {}
        user_info_form["id"] = id
        user_info_form["pwd"] = pwd
        user_info_form["tel"] = tel

        with open("../../project/data/member.json", "r") as f:
            memberList = json.load(f)
        print(memberList)
        # for user in memberList:
        #     if user["id"] == id:
        #         return False
        #
        # memberList.append(user_info_form)
        # f = open("member.json", 'w')
        # json.dump(memberList, f)
        # f.close()

        return True

    def search(self, id, tel):
        pwd = ""

        f = open("../../project/data/member.json", "r")
        memberList = f.readlines()
        f.close()

        print(memberList)

        #memberList = dict(memberList)
        #print(memberList)

        return True, id, pwd

