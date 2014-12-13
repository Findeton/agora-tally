from __future__ import unicode_literals

from .base_stv import *

class MeekSTV(BaseSTV):
    '''
    Meek STV voting system
    '''

    @staticmethod
    def get_id():
        '''
        Returns the identifier of the voting system, used internally to
        discriminate  the voting system used in an election
        '''
        return 'meek-stv'

    @staticmethod
    def get_description():
        return 'Multi-seat ranked voting - Meek STV (Single Transferable Vote)'

    @staticmethod
    def create_tally(election, question_num):
        '''
        Create object that helps to compute the tally
        '''
        tally = BaseSTVTally(election, question_num)
        tally.method_name = "MeekSTV"
        return tally
