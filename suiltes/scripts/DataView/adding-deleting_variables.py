#!/usr/bin/env python
import os, sys

#==============================================================================
class AddingDeletingVarsTest:

#------------------------------------------------------------------------------
    def __init__(self, argsDict):
        print >>sys.stderr, '    test arguments:'
        for (k, v) in argsDict:
            print >>sys.stderr, '    ', k, ' = ', v

#------------------------------------------------------------------------------
    def Execute(self):
        # this fake test should have FAIL status
        return 1


def newTestObject(argsDict):
    return AddingDeletingVarsTest(argsDict)