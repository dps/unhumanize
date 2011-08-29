"""
unhumanize is a simple python library to convert humanized time intervals
(e.g. 'an hour ago') into timedeltas
======================================================

unhumanize is released under the Simplified BSD License:

Copyright (c) 2011, David Singleton
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list
      of conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR IMPLIED
WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those of the
authors and should not be interpreted as representing official policies, either expressed
or implied, of the author.
"""

import re
from datetime import timedelta

DELTAS = {
  'now': timedelta(seconds=0),
  'moment': timedelta(seconds=1),
  'second': timedelta(seconds=1),
  'minute': timedelta(minutes=1),
  'hour': timedelta(hours=1),
  'day': timedelta(days=1),
  'week': timedelta(weeks=1),
  # months and years are approximate.
  'month': timedelta(days=30),
  'year': timedelta(days=365)
}

SINGULARS = ['a ', 'an ', 'just ']

def unhumanize(human_time_interval):
  """Converts human_time_interval (e.g. 'an hour ago') into a datetime.timedelta.
  """
  munged = human_time_interval.strip()
  for needle in SINGULARS:
    munged = munged.replace(needle, '1 ')
  interval_re = '|'.join(DELTAS.keys())
  sre = re.match(r'[. ]*([0-9]*)[ ]*(' + interval_re + r')s?( ago)?',
                 munged)
  if sre:
    ago = sre.groups(1)[2] == ' ago'
    mul = int(sre.groups(1)[0])
    if ago:
      mul = mul * -1
    delta = DELTAS[sre.groups(1)[1]]
    return delta * mul
  else:
    return None
