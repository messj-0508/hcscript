# coding: utf-8

from easydict import EasyDict as edict

__C                             = edict()
# Consumers can get config by: from config import cfg

cfg                             = __C

# Front Fragment Configure
__C.FRONT                       = edict()

__C.FRONT.MINE_TIME             = 5
__C.FRONT.NO_REFRESH_SHOP       = True
__C.FRONT.REFRESH_NUM           = 1


# Behind Fragment Configure
__C.BEHIND                      = edict()

__C.BEHIND.IS_FIRST_TIME        = True
