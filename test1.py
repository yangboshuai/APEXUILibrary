from _roles import _RolesKeysword
from _global import _GlobalKeywords

glo=_GlobalKeywords()
r=_RolesKeysword()
glo.openBrowser()
glo.login('sysadmin','123456a*')
r.enterRoles()
r.delRoles_BySysadmin()
glo.logout()

