"""
Simple Paxos implementation for study.
cf http://fj.hatenablog.jp/entry/2015/10/11/003225
"""

__author__ = 'Seong Yong-ju'
__copyright__ = 'Copyright (c) 2018 Seong Yong-ju.'
__maintainer__ = 'Seong Yong-ju'
__email__ = 'sei40kr@gmail.com'


from typing import List
from collections import Counter


class Proposer:
    def __init__(self, acceptors: List[Acceptor]):
        self.acceptors = acceptors
        self.number = 0
        self.value = 'proposal value'
        self.preparing_acceptors = []

    # TODO This should be refactored not to have acceptors as state.
    def send_prepare_requests(self):
      """
Send preparation requests to all the acceptors.
      """
        print('Start sending preparation requests.')

        # Clear the current preparing acceptors.
        self.preparing_acceptors.clear()

        max_number = -1

        # Send preparation requests to all the acceptors.
        for acceptor in acceptors:
            print('Send a preparation request to ' + str(acceptor) + ': number=' + str(self.number))

            try:
                response = acceptor.prepare(self.number)
            except IOError:
                # Ignore the acceptors that didn't accept the preparation request.
                print('Failed to send a preparation request to ' + str(acceptor) + '.')
                continue

            self.preparing_acceptors.append(acceptor)

            a_number = response[0]
            a_value = response[1]

            if max_number < a_number:
                max_number = a_number
                # Remember the proposal value from the highest numbered acceptor.
                self.value = a_value

          acceptors_count = len(self.acceptors)
          preparing_acceptors_count = len(self.preparing_acceptors)

          print(
              str(preparing_acceptors_count) + ' / ' + str(acceptors_count) +
              ' are preparing.')

          if preparing_acceptors_count < acceptors_count // 2 + 1:
              print(
                  'The acceptors that responded to preparation requests are not majority. Aborting.'
              )
              return

          print('Finish sending preparation requests.')

class Acceptor:
  def prepare(number: int):
    # TODO Implement this
