import environ

from .base import *
from .apps import *
from .database import *

environ.Env.read_env("environments.env")
