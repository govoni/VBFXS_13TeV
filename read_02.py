#!/usr/bin/python

import os
from math import sqrt
import sys
import subprocess
import operator
from ROOT import TFile, TH1F, TCanvas, gStyle, TLine
from commands import getstatusoutput
from operator import itemgetter


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----


def max (uno, due) :
    if (uno > due) : return uno
    return due


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----


def findXS (lines) :
    startReading = 'n'
    for line in lines :
        if startReading != 'n' :
            if 'Total cross section' in line :
                return float (line.split ()[4])
        elif 'Complete results' in line : 
            startReading = 'y'
    return float (-1)


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----


def readFile (fileName) :
    #PG read filename content
    lines = open (fileName, 'r').read ().split ('\n')

    print '\n---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- '
    print 'READING ', fileName
    print '---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- '
    print lines[25]
    print lines[29]
    print lines[32]
    print lines[33]
    print lines[34]
    print lines[38]
    print lines[207]
    print '---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- '

    totalXS = findXS (lines)
    return totalXS


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----


if __name__ == '__main__':


    if len (sys.argv) < 4 : 
        print 'usage: ', sys.argv[0], ' output_filename_posi output_filename_nega type (ct10, mstw) central_value\n'
        exit (1)

    fileName_posi = sys.argv[1]
    fileName_nega = sys.argv[2]
    gen_type      = sys.argv[3]
    central_value = float (sys.argv[4])

    print '---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- '
    print 'using recipe for ', gen_type, 'with cross-section central value: ',central_value

    XS_posi = readFile (fileName_posi)
    XS_nega = readFile (fileName_nega)
        
    print ' XS_nega:', XS_nega, ', XS_posi:', XS_posi
    
    err_posi = float (0)
    err_nega = float (0)
    if gen_type == 'ct10' :
        err_posi = (XS_posi - central_value) * 6. / 5.
        err_nega = (XS_nega - central_value) * 6. / 5.
    else :
        err_posi = (XS_posi - central_value)
        err_nega = (XS_nega - central_value) * 4. / 5.

    print ' err_nega:', err_nega, ', err_posi:', err_posi
    


