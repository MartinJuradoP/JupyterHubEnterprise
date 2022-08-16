
c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
c.LDAPAuthenticator.server_address = 'ldap://host'
c.LDAPAuthenticator.server_port=389
c.LDAPAuthenticator.bind_dn_template = ['{username}','{username}']
c.LDAPAuthenticator.lookup_dn = False
c.LDAPAuthenticator.user_search_base = 'OU=User,OU=ASZ,OU=Accounts,DC=domain,DC=domain,DC=domain'
c.LDAPAuthenticator.lookup_dn_search_filter = '(sAMAccountName={login})'
c.LDAPAuthenticator.lookup_dn_user_dn_attribute = 'CN'
c.LDAPAuthenticator.user_attribute = 'sAMAccountName'
c.LDAPAuthenticator.use_ssl = False
c.LDAPAuthenticator.escape_userdn = False
c.LDAPAuthenticator.valid_username_regex="^.*$"
c.Authenticator.admin_users = {'User'}
