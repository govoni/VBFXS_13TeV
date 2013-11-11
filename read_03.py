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


# takes int as input
# alpha strong given times 1000: 0.119 is given as 119
# energy given in GeV: 13000, 13500, 14000
def buildFileName (alphaS, energy):
    filename = '../pietro/results-HE/output_m125.5-alphaNNPDF21_'
    if alphaS != 119 :
        filename += 'as_0' + str (alphaS) + '_'
    filename += '100.LHgrid-' + str (energy)
    filename += '/outputfile-nnpdf-alphaNNPDF21_'
    if alphaS != 119 :
        filename += 'as_0' + str (alphaS) + '_'
    filename += '100.LHgrid-m125.5'
    return filename
    

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----


def findSets (lines) :
    startReading = 'n'
    values = []
    for line in lines :
        if startReading != 'n' :
            if 'complete cross section' in line :
                values.append (float (line.split ()[3]))
                startReading = 'n'
        elif 'PDF set:' in line : 
            startReading = 'y'
    return values


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----


if __name__ == '__main__':

    energy = int (13000)
    alphaS = int (116)
    
    for j in range (0, 3):
        ensemble = []
        for i in range (0, 7) :
            filename = buildFileName (alphaS + i, energy + 500 * j)
            lines = open (filename, 'r').read ().split ('\n')
#            print filename
#            print findXS (lines)
#            print '--> ', findSets (lines)
#            print alphaS + i, len (findSets (lines))
            ensemble.extend (findSets (lines))
        print len (ensemble)
        ave = float (0)
        for i in range (len (ensemble)) :
            ave += ensemble[i]
        ave /= len (ensemble)
        err = float (0)
        for i in range (len (ensemble)) :
            err += (ensemble[i] - ave) * (ensemble[i] - ave)
        err /= (len (ensemble) - 1)
        err = sqrt (err)
        print energy + 500 * j, ':', ave, '+-', err

