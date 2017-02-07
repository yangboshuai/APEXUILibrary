from position import _POSITIONKeywords
from _global import _GlobalKeywords

glo=_GlobalKeywords()
pos=_POSITIONKeywords()
glo.openBrowser()
glo.login('admin','1234a*')
pos.enterPosit()
pos._delPosit()
glo.logout()

