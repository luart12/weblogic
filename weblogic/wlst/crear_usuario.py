var conn_user="admin"
var conn_passwd="ad1m1nL0g1N"
var user="test"
var passwd="Xt3st01X"

var admin_url="t3://adminserver.example.com:7001"
var description="Usuario administrativo"

# CONECTAR
connect(user,passwd,admin_url)

# CREAR USUARIO
from weblogic.management.security.authentication import UserEditorMBean
print "Crear usuario ..."
atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider("DefaultAuthenticator")
atnr.createUser(user,passwd,description)
print "Usuario creado correctamente"

# ASIGNAR GRUPO
from weblogic.management.security.authentication import GroupEditorMBean
print "Agregando usuario ..."
atnr=cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider("DefaultAuthenticator")
atnr.addMemberToGroup('Administrators',user)
print "Se agrego el usuario"
