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
      - for CT10: ``python read_01.py ../results-HE/m125.5-13500-job1/outputfile-ct10-m125.5 ct10``
      - for MSTW: ``python read_01.py ../results-HE/m125.5-13500-job1/outputfile-ct10-m125.5 mstw``
      
calculate positive and negative uncertainty due to variation of alphaS, for CT10 and MSTW
----

- read_02.py
   - show some file lines to cross-check the parameters with the file name
   - read the total cross-section as input parameter
   - read the cross-section for variation plus and minus, calc error according to formulas on the pdf
   - usage example:
   
   ``python read_02.py \``
   ``../results-HE/m125.5-alphaMSTW2008nlo68cl_asmz+68cl.LHgrid-13000/outputfile-mstw-alphaMSTW2008nlo68cl_asmz+68cl.LHgrid-m125.5 \``
   ``../results-HE/m125.5-alphaMSTW2008nlo68cl_asmz-68cl.LHgrid-13000/outputfile-mstw-alphaMSTW2008nlo68cl_asmz-68cl.LHgrid-m125.5 \``
   ``mstw `python read_01.py ../results-HE/m125.5-13000-job8/outputfile-mstw-m125.5 mstw | tail -n 1 | awk '{print $1}'` ``

      