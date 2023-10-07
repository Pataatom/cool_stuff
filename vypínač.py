import os
import time
def pc_shut(cas):
    time.sleep(cas)
    os.system("shutdown /s /t 1")


decision = ""
while decision.upper() not in ("A", "N"):
    decision = input("Chcete vypnout pc? A/N> ")
if decision.upper() == "A":
    cas = int(input("Za jak dlouho se ma pc vypnout? (V min)> "))
    cas = cas * 60
    pc_shut(cas)
else:
    exit()