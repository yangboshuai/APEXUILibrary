from _user import _USERKeywords

user=_USERKeywords()

user.openBrowser()
user.login('admin','1234a*')
user.createUser()
user.logout()