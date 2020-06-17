from __future__ import absolute_import, unicode_literals

import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent.absolute()

sys.path.insert(0, str(PROJECT_ROOT))
