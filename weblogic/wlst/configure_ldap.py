connect('${USER}','${PASS}','t3://${URI}')

edit()
startEdit()
cd('/SecurityConfiguration/${DOMAIN_NAME}/Realms/myrealm')

cmo.createAuthenticationProvider('${PROVIDER_NAME}', 'weblogic.security.providers.authentication.OracleUnifiedDirectoryAuthenticator')

cd('/SecurityConfiguration/${DOMAIN_NAME}/Realms/myrealm/AuthenticationProviders/DefaultAuthenticator')
cmo.setControlFlag('SUFFICIENT')

cd('/SecurityConfiguration/${DOMAIN_NAME}/Realms/myrealm/AuthenticationProviders/${PROVIDER_NAME}')
cmo.setControlFlag('SUFFICIENT')
cmo.setUseRetrievedUserNameAsPrincipal(true)

save()
activate()

edit()
startEdit()

cmo.setPrincipal('${LDAP_USER}')
cmo.setCredential('${LDAP_PASS}')
cmo.setHost('${LDAP_HOST}')
cmo.setPort(${LDAP_PORT})
cmo.setSSLEnabled(false)

cmo.setUserBaseDN('${USER_BASE}')
cmo.setAllUsersFilter('(&(uid=*)(objectclass=${USER_CLASS}))')
cmo.setUserFromNameFilter('(&(uid=%u)(objectclass=${USER_CLASS}))')
cmo.setUserNameAttribute('uid')
cmo.setUserObjectClass('${USER_CLASS}')

cmo.setAllGroupsFilter('(&(cn=*)(|(objectclass=groupofUniqueNames)(objectclass=${GROUP_CLASS})))')
cmo.setGroupFromNameFilter('(|(&(cn=%g)(objectclass=groupofUniqueNames))(&(cn=%g)(objectclass=groupOfURLs)))')
cmo.setGroupBaseDN('${GROUP_BASE}')

cmo.setStaticGroupObjectClass('${OBJECT_CLASS}')
cmo.setGroupMembershipSearching('limited')
cmo.setMaxGroupMembershipSearchLevel(1)

save()
activate()

edit()
startEdit()

cd('/SecurityConfiguration/${DOMAIN_NAME}/Realms/myrealm')
set('AuthenticationProviders',jarray.array([ObjectName('Security:Name=myrealm${PROVIDER_NAME}'), ObjectName('Security:Name=myrealmDefaultAuthenticator'), ObjectName('Security:Name=myrealmDefaultIdentityAsserter')], ObjectName))
save()
activate()

serverConfig()
cd('/SecurityConfiguration/${DOMAIN_NAME}/Realms/myrealm/RoleMappers/XACMLRoleMapper')
cmo.setRoleExpression("",'Admin','Grp(${LDAP_GROUP})|Grp(Administrators)')
