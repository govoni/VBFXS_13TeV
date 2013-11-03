#!/usr/bin/python

import os
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


if __name__ == '__main__':


    if len (sys.argv) < 2 : 
        print 'usage: ', sys.argv[0], ' output_filename\n'
        exit (1)
        
    fileName = sys.argv[1]

    #PG read filename content
    lines = open (fileName, 'r').read ().split ('\n')

    print '\n---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- '
    print 'READING ', fileName
    print '---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- '
    print lines[23]
    print lines[27]
    print lines[30]
    print lines[31]
    print lines[32]
    print '---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- '
    print lines[209]
    print '---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- '

    totalXS_str = lines[209]
    totalXS = float (totalXS_str.replace (' Total cross section    =', '').replace (' ',''))
#    print totalXS

    values = []
    read = 'n'
    for i in range (210, len (lines)) :
        if read != 'n' :
            if 'complete cross section' in lines[i]:
                tempo = lines[i]
                XS = float (tempo.split ()[3])
                e_XS = float (tempo.split ()[5])
#                print XS, e_XS
                values.append ([XS, e_XS])
        elif 'Results for different PDF sets' in lines[i] : read = 'y'

    print '---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- '
    print len (values)
    print values[0][0]
    print values[1][0]
    print '---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- '
#    for i in range (0, 5) :
    sum_posi = int (0)
    sum_nega = int (0)
    for i in range (0, len (values)/2) :
        val_posi = max ((values[2*i][0] - totalXS), (values[2*i+1][0] - totalXS))
        if val_posi < 0 : val_posi = 0
        sum_posi += val_posi * val_posi
        val_nega = max ((totalXS - values[2*i][0]), (totalXS - values[2*i+1][0]))
        if val_nega < 0 : val_nega = 0
        sum_nega += val_nega * val_nega
        


    
