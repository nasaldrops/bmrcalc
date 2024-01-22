import sys, os

INTERP = "/home/eirtime/bmrcalc/bmr/bin/python"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

from main import app as application