from flask import current_app
from flask.ext.principal import Permission, RoleNeed, UserNeed, identity_loaded
from flask.ext.login import current_user

admin_permission = Permission(RoleNeed('admin'))
editor_permission = Permission(RoleNeed('editor'))
author_permission = Permission(RoleNeed('author'))
reader_permission = Permission(RoleNeed('reader'))


# @identity_loaded.connect # Both of this and the following works
@identity_loaded.connect_via(current_app)
def on_identity_loaded(sender, identity):
    # Set the identity user object
    identity.user = current_user

    # Add the UserNeed to the identity
    if hasattr(current_user, 'username'):
        identity.provides.add(UserNeed(current_user.username))

    # Assuming the User model has a list of roles, update the
    # identity with the roles that the user provides
    if hasattr(current_user, 'role'):
        # for role in current_user.roles:
        identity.provides.add(RoleNeed(current_user.role))