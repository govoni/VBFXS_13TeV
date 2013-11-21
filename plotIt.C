TGraphAsymmErrors * getGraph (float val, float eplus, float eminus, float height)
  {
    TGraphAsymmErrors * dummy = new TGraphAsymmErrors (1) ; 
    dummy->SetPoint (0, val, height) ;
    dummy->SetPointError (0, eminus, eplus, 0, 0) ;  
    dummy->SetMarkerStyle (24) ;
    dummy->SetMarkerSize (0.5) ;
    dummy->SetLineWidth (2) ;
    dummy->SetLineColor (kBlue) ;
    dummy->SetMarkerColor (kBlue) ;
  
    return dummy ;
  }

void changeYaxis (TAxis * yaxis)
  {
    float binlimits[] = {-0.5, 0.5, 1.5, 2.5, 3.5} ;
    yaxis->Set (4, binlimits) ;
    TString labels[] = {"env", "ct10", "mstw", "nnpdf"} ;
    for (int i = 0 ; i < 5 ; ++i)
      yaxis->SetBinLabel (i+1, labels[i]) ;  
  }


int plotIt ()
{
  // ct10
  TGraphAsymmErrors * g_ct10_130_pdf = getGraph (3726.529417, 118.578004458, 116.129000604, 1) ;
  TGraphAsymmErrors * g_ct10_130_tot = getGraph (3726.529417, 118.876594761, 116.455757574, 1) ;
  TGraphAsymmErrors * g_ct10_135_pdf = getGraph (3975.2151  , 126.727388919, 124.013568896, 1) ;
  TGraphAsymmErrors * g_ct10_135_tot = getGraph (3975.2151  , 126.800781376, 124.413730384, 1) ;
  TGraphAsymmErrors * g_ct10_140_pdf = getGraph (4224.701359, 135.016252881, 132.032247696, 1) ;
  TGraphAsymmErrors * g_ct10_140_tot = getGraph (4224.701359, 135.149233221, 132.49244773 , 1) ;

  g_ct10_130_pdf->SetLineColor (kRed) ;
  g_ct10_135_pdf->SetLineColor (kRed) ;
  g_ct10_140_pdf->SetLineColor (kRed) ;

  // mstw 
  TGraphAsymmErrors * g_mstw_130_pdf = getGraph (3770.936488, 82.0712882333, 58.7022283414, 2) ;
  TGraphAsymmErrors * g_mstw_130_tot = getGraph (3770.936488, 109.449437295, 96.3212866863, 2) ;
  TGraphAsymmErrors * g_mstw_135_pdf = getGraph (4021.901263, 87.0628604531, 62.2624259067, 2) ;
  TGraphAsymmErrors * g_mstw_135_tot = getGraph (4021.901263, 118.535610017, 104.360060331, 2) ;
  TGraphAsymmErrors * g_mstw_140_pdf = getGraph (4276.162449, 92.1982859432, 65.9283059104, 2) ;
  TGraphAsymmErrors * g_mstw_140_tot = getGraph (4276.162449, 126.859840139, 111.320700098, 2) ;
  
  g_mstw_130_pdf->SetLineColor (kRed) ;
  g_mstw_135_pdf->SetLineColor (kRed) ;
  g_mstw_140_pdf->SetLineColor (kRed) ;

  // nnpdf
  TGraphAsymmErrors * g_nnpdf_130_tot = getGraph (3634.0146785 , 64.2007511973, 64.2007511973, 3) ;
  TGraphAsymmErrors * g_nnpdf_135_tot = getGraph (3871.10603812, 67.846790844 , 67.846790844 , 3) ;
  TGraphAsymmErrors * g_nnpdf_140_tot = getGraph (4114.50858684, 72.0492350523, 72.0492350523, 3) ;

  //envelope
  
  float val_fr_130_min = 3634.0146785  - 64.2007511973 ;
  float val_fr_135_min = 3871.10603812 - 67.846790844  ;
  float val_fr_140_min = 4114.50858684 - 72.0492350523 ;
  
  float val_fr_130_max = 3770.936488 + 109.449437295 ;
  float val_fr_135_max = 4021.901263 + 118.535610017 ;
  float val_fr_140_max = 4276.162449 + 126.859840139 ;
  
  float val_fr_130_mid = 0.5 * (val_fr_130_min + val_fr_130_max) ;
  float val_fr_135_mid = 0.5 * (val_fr_135_min + val_fr_135_max) ;
  float val_fr_140_mid = 0.5 * (val_fr_140_min + val_fr_140_max) ;

  TGraphAsymmErrors * g_env_130_tot = getGraph (val_fr_130_mid, val_fr_130_max - val_fr_130_mid, val_fr_130_mid - val_fr_130_min, 0) ;
  TGraphAsymmErrors * g_env_135_tot = getGraph (val_fr_135_mid, val_fr_135_max - val_fr_135_mid, val_fr_135_mid - val_fr_135_min, 0) ;
  TGraphAsymmErrors * g_env_140_tot = getGraph (val_fr_140_mid, val_fr_140_max - val_fr_140_mid, val_fr_140_mid - val_fr_140_min, 0) ;

  cout << " XS at 13.0 TeV: " << val_fr_130_mid << " +- " << val_fr_130_max - val_fr_130_mid << endl ;
  cout << " XS at 13.5 TeV: " << val_fr_135_mid << " +- " << val_fr_135_max - val_fr_135_mid << endl ;
  cout << " XS at 14.0 TeV: " << val_fr_140_mid << " +- " << val_fr_140_max - val_fr_140_mid << endl ;


  // plotting

  TCanvas * c1 = new TCanvas ("c1", "c1", 1800, 500) ;
  c1->Divide (3, 1) ;

  c1->cd (1) ;
  TH1F * fr_130 = gPad->DrawFrame (3500, -0.5, 3900, 3.5) ;
  changeYaxis (fr_130->GetYaxis ()) ;
  TLine * l_130 = new TLine (3500, 0.5, 3900, 0.5) ;
  fr_130->SetTitle ("13.0 TeV") ;
  fr_130->GetXaxis ()->SetTitle ("cross-section (pb)") ;
  g_ct10_130_tot->Draw ("P same") ;
  g_ct10_130_pdf->Draw ("P same") ;
  g_mstw_130_tot->Draw ("P same") ;
  g_mstw_130_pdf->Draw ("P same") ;
  g_nnpdf_130_tot->Draw ("P same") ;
  l_130->Draw () ;
  g_env_130_tot->Draw ("P same") ;
  
  c1->cd (2) ;
  TH1F * fr_135 = gPad->DrawFrame (3700, -0.5, 4200, 3.5) ;
  changeYaxis (fr_135->GetYaxis ()) ;
  TLine * l_135 = new TLine (3700, 0.5, 4200, 0.5) ;
  fr_135->SetTitle ("13.5 TeV") ;
  fr_135->GetXaxis ()->SetTitle ("cross-section (pb)") ;
  g_ct10_135_tot->Draw ("P same") ;
  g_ct10_135_pdf->Draw ("P same") ;
  g_mstw_135_tot->Draw ("P same") ;
  g_mstw_135_pdf->Draw ("P same") ;
  g_nnpdf_135_tot->Draw ("P same") ;
  l_135->Draw () ;
  g_env_135_tot->Draw ("P same") ;
   
  c1->cd (3) ;
  TH1F * fr_140 = gPad->DrawFrame (4000, -0.5, 4500, 3.5) ;
  changeYaxis (fr_140->GetYaxis ()) ;
  TLine * l_140 = new TLine (4000, 0.5, 4500, 0.5) ;
  fr_140->SetTitle ("14.0 TeV") ;
  fr_140->GetXaxis ()->SetTitle ("cross-section (pb)") ;
  g_ct10_140_tot->Draw ("P same") ;
  g_ct10_140_pdf->Draw ("P same") ;
  g_mstw_140_tot->Draw ("P same") ;
  g_mstw_140_pdf->Draw ("P same") ;
  g_nnpdf_140_tot->Draw ("P same") ;
  l_140->Draw () ;
  g_env_140_tot->Draw ("P same") ;
  

}




 
 
 



