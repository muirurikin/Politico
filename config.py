import os

class Config(object):
  """
  Common configurations
  """
  pass

class DevelopmentConfig(Config):
  """
  Development configurations
  """

  DEBUG = True


class ProductionConfig(Config):
  """
  Production configurations
  """

  DEBUG = False

app_config = {
  'development': DevelopmentConfig,
  'production': ProductionConfig
}