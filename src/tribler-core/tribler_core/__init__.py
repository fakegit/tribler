"""
Tribler is a privacy enhanced BitTorrent client with P2P content discovery.
"""
import os
import sys

from tribler_core.utilities.path_util import Path

dir_path = Path(__file__).parent.parent.parent

# Make sure AnyDex can be imported
sys.path.append(os.path.join(dir_path, "anydex"))

# Make sure IPv8 can be imported
sys.path.insert(0, os.path.join(dir_path, "pyipv8"))
