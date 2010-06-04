#!/usr/bin/env python

import random
import dbg
import debug as log

def randint(a, b):
    def replay(a, b):
        log.debug('Replaying randint', dbg.ic, dbg.sde)
        return dbg.sde[dbg.ic]
    def undo(a, b):
        log.debug('undoing randint')
    def debug(a, b):
        value = random.__orig__randint(a, b)
        dbg.sde[dbg.ic] = value
        log.debug('debugging randint')
        return value
    log.debug('This is the modified randint', a, b)
    if dbg.mode == 'replay':
        return replay(a, b)
    elif dbg.mode == 'normal':
        return debug(a, b)
    elif dbg.mode == 'undo':
        return
   
    
    