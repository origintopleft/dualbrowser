#!/usr/bin/env python

# DualBrowser
# by Nicholas "Lavacano" O'Connor
# Purpose: I like both Firefox and Chrome.

import sys
import subprocess
import win32pdh
import string
import win32api

if len(sys.argv) == 1:
    import Tkinter
    import configUtil

    cfgutil = configUtil.ConfigUtility()
    cfgutil.master.title("DualBrowser Configuration Utility")
    cfgutil.mainloop() # The config utility will exit the program there.

def procids():
    #each instance is a process, you can have multiple processes w/same name
    junk, instances = win32pdh.EnumObjectItems(None,None,'process', win32pdh.PERF_DETAIL_WIZARD)
    proc_ids=[]
    proc_dict={}
    for instance in instances:
        if instance in proc_dict:
            proc_dict[instance] = proc_dict[instance] + 1
        else:
            proc_dict[instance]=0
    for instance, max_instances in proc_dict.items():
        for inum in xrange(max_instances+1):
            hq = win32pdh.OpenQuery() # initializes the query handle
            path = win32pdh.MakeCounterPath( (None,'process',instance, None, inum,'ID Process') )
            counter_handle=win32pdh.AddCounter(hq, path)
            win32pdh.CollectQueryData(hq) #collects data for the counter
            type, val = win32pdh.GetFormattedCounterValue(counter_handle, win32pdh.PDH_FMT_LONG)
            proc_ids.append((instance,str(val)))
            win32pdh.CloseQuery(hq)

    return proc_ids

processList = procids()

BrowserIsRunning = False

for item in processList:
    if item[0].lower() == "chrome":
        BrowserIsRunning = True
        subprocess.Popen(["C:\\Users\\lavacano201014\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe", "--enable-aero-peek-tabs", sys.argv[1]])
        break
    elif item[0].lower() == "firefox":
        BrowserIsRunning = True
        subprocess.Popen(["D:\\Firefox\\firefox.exe", sys.argv[1]])
        break

if BrowserIsRunning == False:
    prefer = None
    choice = ""
    try:
        with open("dualbrowser.cfg") as cfg:
            for line in cfg:
                config = line.split("=")
                if config[0] == "prefer":
                    if config[1] == "1":
                        prefer = True
                    else:
                        prefer = False
                elif config[0] == "choice":
                    choice = config[1]
    except IOError:
        prefer = False
    if prefer == True:
        if choice == "firefox":
            subprocess.Popen(["D:\\Firefox\\firefox.exe", sys.argv[1]])
        elif choice == "chrome":
            subprocess.Popen(["C:\\Users\\lavacano201014\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe", "--enable-aero-peek-tabs", sys.argv[1]])
    else:
        from random import randint
        selection = randint(1,2)
        if selection == 1:
            subprocess.Popen(["C:\\Users\\lavacano201014\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe", "--enable-aero-peek-tabs", sys.argv[1]])
        elif selection == 2:
            subprocess.Popen(["D:\\Firefox\\firefox.exe", sys.argv[1]])