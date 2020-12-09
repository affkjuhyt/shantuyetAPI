import os

FRONTEND_ROOT_URL = os.environ.get("APPS_ENVIRONMENT_ROOT_URL")

REST_REGISTRATION = {
    'RESET_PASSWORD_VERIFICATION_URL': '{}/forgot'.format(FRONTEND_ROOT_URL),
    'USER_VERIFICATION_FLAG_FIELD': 'is_active',
}
