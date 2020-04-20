# SPDX-License-Identifier: BSD-2-Clause

import os
import sys
from .lang_aux import Const, ConstModule

def env_bool(x):
   return Const(os.environ.get(x, '0') == '1')

def env_int(x, val):
   return Const(int(os.environ.get(x, str(val))))

VM_MEMORY_SIZE_IN_MB = env_int('TILCK_VM_MEM', 128)
GEN_TEST_DATA = env_bool('GEN_TEST_DATA')

in_travis = env_bool('TRAVIS')
in_circleci = env_bool('CIRCLECI')
in_azure = env_bool('AZURE_HTTP_USER_AGENT')
dump_coverage = env_bool('DUMP_COV')
report_coverage = env_bool('REPORT_COV')
verbose = env_bool('VERBOSE')
in_any_ci = Const(in_travis.val or in_circleci.val or in_azure.val)

sys.modules[__name__] = ConstModule(__name__)
