import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello World")


# 1) create a VE - py (-3 -m venv [command] myvenv [name of the environment]) (pc)
# python3 -m venv (command) myvenv (name of the environment)
# 2) activate your (VE myvenv/scripts/activate) (pc)
# 3) install 3rd party library/module (source my venv/bin/activate)
# have powershell on in security settings
# pip3 install matplotlib to install