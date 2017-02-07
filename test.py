from _global import _GlobalKeywords
from orgization import _ORGKeyswords


glo=_GlobalKeywords()
glo.openBrowser()
glo.login('admin','1234a*')
orgz=_ORGKeyswords()
orgz.enterOrg()
orgz.createOrg()
glo.logout()


