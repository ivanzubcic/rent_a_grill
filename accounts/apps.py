from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class AccountsConfig(AppConfig):
	logger.error('Test logger.....')
    name = 'accounts'
