


import glob
from pathlib import Path
from DEEPAK.utils import load_plugins
import logging
from DEEPAK import DEEPAK

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "DEEPAK/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("Successfully Started Bot!")
print("Visit @TheUpdatesChannel")

if __name__ == "__main__":
    DEEPAK.run_until_disconnected()
