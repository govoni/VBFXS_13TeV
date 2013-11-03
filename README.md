calculate VBF Higgs XS at 13 TeV
=======

read the central value and eigenvector variation output
----

- read_01.py: 
   - show some file lines to cross-check the parameters with the file name
   - read the total cross-section from input file
   - read the cross-section for each variation of eigenvector
   - calculate the total positive and negative uncertainties due to the eigenvectors variation
   - usage: 
      python read_01.py ../results-HE/m125.5-13500-job1/outputfile-ct10-m125.5