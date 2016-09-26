## CASA scripts to reduce L band data in B configuration 
vis='14B-165.sb30142041.eb30465088.57081.464200752314.ms'
split(vis=vis,outputvis='A2255C-14B314.ms',field='3')

visc='A2255C-14B314.ms'
flagmanager(vis=visc,mode='save',versionname='BeforeFirstFlag.ms')
flagdata(vis=visc,action='apply',spw='1,9,14:16~60',mode='manual')
flagdata(vis=visc,action='apply',spw='15:3~28,10:3~4,10:27~55,7:47~48,0:3~10,0:15~25,0:32~60,2:3~15,2:24~60,4:3~37,5:3~6,5:53,5:21~23',mode='manual')
statwt(vis=visc,dorms=False,byantenna=False,spw='',minsamp=2,datacolumn='corrected',timebin='0s')
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B314-0',imsize=[6000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=500,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B314-0',imsize=[6000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=50000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B314-0',imsize=[6000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=1000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)

vis=visc
refant='ea24'
solint='inf'
caltable = 'selfcal-A2255C-B314-0.gcal'
gaincal(vis=visc,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='p', combine='', minblperant=4) 
plotcal(caltable=caltable,
        xaxis='time', yaxis='phase',
        plotrange=[0,0,-50,50],
        iteration='spw', subplot = 221)
# I flaggged a few data points
flagmanager(vis=visc,mode='save',versionname='BeforeFirstgaincal.ms')
applycal(vis=visc,gaintable=caltable,interp='linear',flagbackup=False) 
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B314-1',imsize=[6000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B314-1',imsize=[6000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B314-1',imsize=[6000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.14,gridmode='widefield',wprojplanes=64)
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B314-1',imsize=[6000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.14,gridmode='widefield',wprojplanes=64)

vis=visc
refant='ea24'
solint='inf'
caltable = 'selfcal-A2255C-B314-1.gcal'
gaincal(vis=visc,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='ap', combine='', minblperant=4) 
plotcal(caltable=caltable,
        xaxis='time', yaxis='amp',
        plotrange=[0,0,0,2],
        iteration='spw', subplot = 221)
flagmanager(vis=visc,mode='save',versionname='BeforeFinal.ms')
applycal(vis=visc,gaintable=caltable,interp='linear',flagbackup=False) 
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B314-2',imsize=[6000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B314-2',imsize=[6000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B314-2',imsize=[6000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B314-2',imsize=[6000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.16,gridmode='widefield',wprojplanes=64)
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B314-2',imsize=[6000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.2,gridmode='widefield',wprojplanes=64)
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B314-2',imsize=[6000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.2,gridmode='widefield',wprojplanes=64)
########################################################################
########################################################################
########################################################################
#Now the Northern field=2
########################################################################
vis='14B-165.sb30142041.eb30465088.57081.464200752314.ms'
split(vis=vis,outputvis='A2255N-14B314.ms',field='2')
visn='A2255N-14B314.ms'
flagdata(vis=visn,action='apply',spw='1,9,14:16~60',mode='manual')
flagdata(vis=visn,action='apply',spw='15:3~28,10:3~4,10:27~55,7:47~48,0:3~10,0:15~25,0:32~60,2:3~15,2:24~60,4:3~37,5:3~11,5:53,5:21~23',mode='manual')
flagdata(vis=visn,action='apply',spw='10:57~60,11:36~40,12:37~38,13:35~38,6:7~9,4:38,4:58,0:11~12,5:52~55',mode='manual')
statwt(vis=visn,dorms=False,byantenna=False,spw='',minsamp=2,datacolumn='corrected',timebin='0s')
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255N-14B314-0',imsize=[6000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=0,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',outlierfile='Outlier.txt',imagename='A2255N-14B314-1',imsize=[5000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=30000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)

vis=visn
refant='ea24'
solint='inf'
caltable = 'selfcal-A2255N-B314-0.gcal'
gaincal(vis=visn,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='p', combine='', minblperant=4) 
plotcal(caltable=caltable,
        xaxis='time', yaxis='phase',
        plotrange=[0,0,-50,50],
        iteration='spw', subplot = 221)
# I flagged some of the data with bad calibration
# I completely flagged spw=15
flagmanager(vis=visn,mode='save',versionname='BeforeFirstgaincal.ms')
applycal(vis=visn,gaintable=caltable,interp='linear',flagbackup=False)
flagdata(vis=visn,action='apply',spw='15',mode='manual')
statwt(vis=visn,dorms=False,byantenna=False,spw='',minsamp=2,datacolumn='corrected',timebin='0s')
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',outlierfile='Outlier2.txt',imagename='A2255N-14B314-2',imsize=[5000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=50000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
caltable = 'selfcal-A2255N-B314-1.gcal'
gaincal(vis=visn,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='p', combine='', minblperant=4) 
plotcal(caltable=caltable,
        xaxis='time', yaxis='phase',
        plotrange=[0,0,-50,50],
        iteration='spw', subplot = 221)
# I flagged some of the data with bad calibration
applycal(vis=visn,gaintable=caltable,interp='linear',flagbackup=False)
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',outlierfile='Outlier3.txt',imagename='A2255N-14B314-3',imsize=[5000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',outlierfile='Outlier3.txt',imagename='A2255N-14B314-3',imsize=[5000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',outlierfile='Outlier3.txt',imagename='A2255N-14B314-3',imsize=[5000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.16,gridmode='widefield',wprojplanes=64)
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',outlierfile='Outlier3.txt',imagename='A2255N-14B314-3',imsize=[5000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.2,gridmode='widefield',wprojplanes=64)

caltable = 'selfcal-A2255N-B314-2.gcal'
gaincal(vis=visn,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='ap', combine='', minblperant=4) 
plotcal(caltable=caltable,
        xaxis='time', yaxis='amp',
        plotrange=[0,0,0,2],
        iteration='spw', subplot = 221)
applycal(vis=visn,gaintable=caltable,interp='linear',flagbackup=False)
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',outlierfile='Outlier4.txt',imagename='A2255N-14B314-4',imsize=[5000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',outlierfile='Outlier4.txt',imagename='A2255N-14B314-4',imsize=[5000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.14,gridmode='widefield',wprojplanes=64)
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',outlierfile='Outlier4.txt',imagename='A2255N-14B314-4',imsize=[5000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.16,gridmode='widefield',wprojplanes=64)
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',outlierfile='Outlier4.txt',imagename='A2255N-14B314-4',imsize=[5000,5000],cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.2,gridmode='widefield',wprojplanes=64)

#################################################################
#################################################################
#################################################################
# Polarization calibration
# We first work with the 3C286 calibrator
#2016-04-06 04:29:39     INFO    imager::setjy() Using model image /Applications/CASA.app/Contents/data/nrao/VLA/CalModels/3C286_L.im
#2016-04-06 04:29:39     INFO    imager::setjy() Scaling spw(s) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]'s model image by channel to  I = 17.7836, 14.5337, 12.4339 Jy @(1.00743e+09, 1.51943e+09, 2.03043e+09)Hz (LSRK) for visibility prediction (a few representative values are shown).
# In CASA
#Calculating the Alpha of 3C286 for each spw:
alpha0=log(17.276/17.779)/log(1.072/1.008)
alpha1=log(16.807/17.276)/log(1.136/1.072)
alpha2=log(16.367/16.807)/log(1.2/1.136)
alpha3=log(15.955/16.367)/log(1.264/1.2)
alpha4=log(15.568/15.955)/log(1.328/1.264)
alpha5=log(15.203/15.568)/log(1.392/1.328)
alpha6=log(14.857/15.203)/log(1.456/1.392)
alpha7=log(14.531/14.857)/log(1.52/1.456)
alpha8=log(14.221/14.531)/log(1.584/1.52)
alpha9=log(13.927/14.221)/log(1.648/1.584)
alpha10=log(13.647/13.927)/log(1.712/1.648)
alpha11=log(13.381/13.647)/log(1.776/1.712)
alpha12=log(13.126/13.381)/log(1.84/1.776)
alpha13=log(12.884/13.126)/log(1.904/1.84)
alpha14=log(12.651/12.884)/log(1.968/1.904)
alpha15=log(12.4339/12.884)/log(2.03043/1.904)
# In CASA
i0=17.779 # Stokes I value for spw 0 
c0=0.086 # Fractional polarization=8.6%
d0=33*pi/180 # polarization angle of 33 degrees converted to radians
myset0=setjy(vis='14B-165.sb30142041.eb30465088.57081.464200752314.ms', field='0', standard='manual',
      spw='0', fluxdensity=[i0,0,0,0], spix=[alpha0,0], reffreq='1.008GHz',
      polindex=[c0,0], polangle=[d0,0],
      scalebychan=True, usescratch=False)

plotms(vis='14B-165.sb30142041.eb30465088.57081.464200752314.ms',field='0',spw='0',correlation='RR',
       timerange='',antenna='',
       xaxis='channel',yaxis='amp',ydatacolumn='model',
       plotfile='plotms_3c391-model-amp-RR.png',overwrite=True)

plotms(vis='14B-165.sb30142041.eb30465088.57081.464200752314.ms',field='0',spw='0',correlation='RL',
       timerange='',antenna='',
       xaxis='channel',yaxis='amp',ydatacolumn='model',
       plotfile='plotms_3c391-model-amp-RL.png',overwrite=True)
plotms(vis='14B-165.sb30142041.eb30465088.57081.464200752314.ms',field='0',spw='0',correlation='RL',
       timerange='',antenna='',
       xaxis='channel',yaxis='phase',ydatacolumn='model',
       plotfile='plotms_3c391-model-phase-RL.png',overwrite=True,plotrange=[-1,-1,-180,180])

#Solving for the Cross-Hand delays
# In pipeline calibrations antenna ea09 is used as the refant.
gaincal(vis='14B-165.sb30142041.eb30465088.57081.464200752314.ms', caltable='A2255-spw0_2.Kcross',
        field='0', spw='0:5~58',
        gaintype='KCROSS', solint='inf', combine='scan', refant='ea09',
        gaintable=['14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_3.gc.tbl',
        		   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_4.opac.tbl',
        		   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_5.rq.tbl',
        		   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_6.ants.tbl',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finaldelay.k',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalBPcal.b',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.averagephasegain.g',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalampgaincal.g',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalphasegaincal.g'],
        gainfield=['','','','','','','','0','0'],
        parang=T)
# The delay between L and R is:
# 2016-09-01 20:19:20 INFO gaincal  Time=2015/02/28/11:24:59.4 Spw=0 Global cross-hand delay=-3.76588 nsec

plotcal(caltable='A2255-spw0_2.Kcross',xaxis='antenna',yaxis='delay',
        figfile='plotcal_A2255-Kcross-delay_2.png')

#Solving for the Leakage Terms
#Calculating the Alpha of 3C248 for each spw:
alph0=log(20.371/21.367)/log(1.072/1.008)
alph1=log(19.464/20.371)/log(1.136/1.072)
alph2=log(18.634/19.464)/log(1.2/1.136)
alph3=log(17.873/18.634)/log(1.264/1.2)
alph4=log(17.172/17.873)/log(1.328/1.264)
alph5=log(16.523/17.172)/log(1.392/1.328)
alph6=log(15.922/16.523)/log(1.456/1.392)
alph7=log(15.363/15.922)/log(1.52/1.456)
alph8=log(14.841/15.363)/log(1.584/1.52)
alph9=log(14.354/14.841)/log(1.648/1.584)
alph10=log(13.898/14.354)/log(1.712/1.648)
alph11=log(13.47/13.898)/log(1.776/1.712)
alph12=log(13.067/13.47)/log(1.84/1.776)
alph13=log(12.687/13.067)/log(1.904/1.84)
alph14=log(12.329/12.687)/log(1.968/1.904)
alph15=log(11.9927/12.329)/log(2.03043/1.904)
i00=21.367 # Stokes I value for spw 0 
c00=0.003 # Fractional polarization=0.3%
d00=25*pi/180 # polarization angle of 25 degrees converted to radians
myset1=setjy(vis='14B-165.sb30142041.eb30465088.57081.464200752314.ms', field='4', standard='manual',
      spw='0', fluxdensity=[i00,0,0,0], spix=[alph0,0], reffreq='1.008GHz',
      polindex=[c00,0], polangle=[d00,0],
      scalebychan=True, usescratch=False)

plotms(vis='14B-165.sb30142041.eb30465088.57081.464200752314.ms',field='4',spw='0',correlation='RL',
       timerange='',antenna='',
       xaxis='channel',yaxis='amp',ydatacolumn='model',
       plotfile='plotms_3c48-model-amp-RL.png',overwrite=True)

polcal(vis='14B-165.sb30142041.eb30465088.57081.464200752314.ms',caltable='A2255_spw0.D1_2',
       field='4',spw='0:5~58',
       refant='ea09',poltype='Df',solint='inf',combine='scan',
       gaintable=['14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_3.gc.tbl',
        		   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_4.opac.tbl',
        		   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_5.rq.tbl',
        		   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_6.ants.tbl',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finaldelay.k',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalBPcal.b',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.averagephasegain.g',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalampgaincal.g',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalphasegaincal.g',
                  'A2255-spw0_2.Kcross'],
       gainfield=['','','','','','','','4','4',''])

plotcal(caltable='A2255_spw0.D1_2',xaxis='chan',yaxis='amp', 
        spw='0',field='',iteration='antenna')
plotcal(caltable='A2255_spw0.D1_2',xaxis='chan',yaxis='phase', 
        spw='0',field='',iteration='antenna',plotrange=[-1,-1,-180,180])
plotcal(caltable='A2255_spw0.D1_2',xaxis='antenna',yaxis='amp', 
        figfile='plotcal_A2255-D1_2.png')

# Something is weird in two of the channels!

polcal(vis='14B-165.sb30142041.eb30465088.57081.464200752314.ms',caltable='A2255_spw0.D2_2',
       field='1',spw='0:5~58',
       refant='ea09',poltype='Df+QU',solint='inf',combine='scan',
       gaintable=['14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_3.gc.tbl',
        		   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_4.opac.tbl',
        		   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_5.rq.tbl',
        		   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_6.ants.tbl',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finaldelay.k',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalBPcal.b',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.averagephasegain.g',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalampgaincal.g',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalphasegaincal.g',
                  'A2255-spw0_2.Kcross'],
       gainfield=['','','','','','','','1','1',''])

plotcal(caltable='A2255_spw0.D2_2',xaxis='chan',yaxis='amp', 
        spw='0',field='',iteration='antenna')
plotcal(caltable='A2255_spw0.D2_2',xaxis='chan',yaxis='phase', 
        spw='0',field='',iteration='antenna',plotrange=[-1,-1,-180,180])
plotcal(caltable='A2255_spw0.D2_2',xaxis='antenna',yaxis='amp', 
        figfile='plotcal_A2255-D2_2.png')
# The solutions are quite similar except a couple of channels with strange offset in D1 solutions. I will use D2 tables
#Solving for the R-L polarization angle

polcal(vis='14B-165.sb30142041.eb30465088.57081.464200752314.ms',caltable='A2255_spw0.X1_2',
       field='0',spw='0',combine='scan',
       poltype='Xf',solint='inf',
       gaintable=['14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_3.gc.tbl',
        		   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_4.opac.tbl',
        		   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_5.rq.tbl',
        		   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_6.ants.tbl',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finaldelay.k',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalBPcal.b',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.averagephasegain.g',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalampgaincal.g',
                   '14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalphasegaincal.g',
                  'A2255-spw0_2.Kcross',
                  'A2255_spw0.D2_2'],
       gainfield=['','','','','','','','0','0','',''])

plotcal(caltable='A2255_spw0.X1_2',xaxis='chan',yaxis='phase',
        figfile='plotcal_A2255-X1_2.png')

### Now that I know it works it's time to automate it for all spw
## The routine polcalib.py is placed in the same directory as the MS and is run. As a result we have the polarization calibration tables for each spw separately except spw=3,8 that are already flagged.
### IMPORTANT IMPORTANT IMPORTANT
# The target fields must be split first and then the new polarization calibration tables only should be applied to the split data. This way the products of the pipeline remain untouched.
vis='14B-165.sb30142041.eb30465088.57081.464200752314.ms'
split(vis=vis,outputvis='A2255C-14B314_polcal.ms',field='3')
viscpol='A2255C-14B314_polcal.ms'
split(vis=vis,outputvis='A2255_calibrators_polcal.ms',field='0,1,4')
viscal='A2255_calibrators_polcal.ms'

# Now applying only the polarization calibrations to the calibrators and the central field
sp=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']

for i in sp: 
	applycal(vis=viscal,field='',gaintable=['A2255-spw'+i+'.Kcross','A2255_spw'+i+'.D','A2255_spw'+i+'.X'],gainfield=['','',''], interp=['','',''],calwt=[False],parang=True)
for i in sp: 
	applycal(vis=viscpol,field='',gaintable=['A2255-spw'+i+'.Kcross','A2255_spw'+i+'.D','A2255_spw'+i+'.X'],gainfield=['','',''], interp=['','',''],calwt=[False],parang=True)

# plotting a few standard plots to check up
plotms(vis=viscal,field='0',correlation='',
       timerange='',antenna='',avgtime='60s',
       xaxis='channel',yaxis='amp',ydatacolumn='corrected',
       coloraxis='corr',
       plotfile='plotms_viscal-fld0-corrected-amp.png',overwrite=True)
plotms(vis=viscal,field='0',correlation='',
       timerange='',antenna='',avgtime='60s',
       xaxis='channel',yaxis='phase',ydatacolumn='corrected',
       coloraxis='corr',
       plotfile='plotms_viscal-fld0-corrected-phase.png',overwrite=True,plotrange=[-1,-1,-180,180])
plotms(vis=viscal,field='2',correlation='RR,LL',
       timerange='',antenna='',avgtime='60s',spw='0',
       xaxis='phase',xdatacolumn='corrected',yaxis='amp',ydatacolumn='corrected',
       plotrange=[-180,180,0,24],coloraxis='corr',overwrite=True,
       plotfile='plotms_viscal-fld2-spw0-corrected-ampvsphase.png')

# Now that I am satisfied with the calibrations I will apply previously determined extra steps such as flagging and weighting on the target field. and Self-cal to make full stokes images.
flagmanager(vis=viscpol,mode='save',versionname='Viscpol_BeforeFirstFlag.ms')
flagdata(vis=viscpol,action='apply',spw='1,9,14:16~60',mode='manual')
flagdata(vis=viscpol,action='apply',spw='15:3~28,10:3~4,10:27~55,7:47~48,0:3~10,0:15~25,0:32~60,2:3~15,2:24~60,4:3~37,5:3~6,5:53,5:21~23',mode='manual')
statwt(vis=viscpol,dorms=False,byantenna=False,spw='',minsamp=2,datacolumn='corrected',timebin='0s')
# Making the first clean image 
#Note that apparently, nterms=2 can not be used with multiple stokes.
clean(vis=viscpol,imagename='A2255C-14B314-IQUV-0',
      field='',spw='',
      mode='mfs',
      nterms=1,
      niter=2500,
      gain=0.1,
      psfmode='clarkstokes',
      imagermode='', 
      multiscale=[0, 4, 12, 36], smallscalebias=0.9,
      imsize=[6000,5000], cell=['1.0arcsec'],
      stokes='IQUV',
      weighting='briggs',robust=0.5,
      pbcor=False,
      usescratch=False,
      interactive=False,
      gridmode='widefield',wprojplanes=64)

# Now doing selfcal.
# Self cal must be applied only on Stokes I
# I first remove the model column in the MS to get rid of the polarization models
delmod(viscpol)

clean(vis=viscpol,imagename='A2255C-14B314-I-selcal_0',
      field='',spw='',
      mode='mfs',
      nterms=2,
      niter=2500,
      gain=0.1,
      psfmode='clark',
      imagermode='', 
      multiscale=[0, 4, 12, 36], smallscalebias=0.9,
      imsize=[6000,5000], cell=['1.0arcsec'],
      stokes='I',
      weighting='briggs',robust=0.5,
      pbcor=False,
      usescratch=False,
      interactive=False,
      gridmode='widefield',wprojplanes=64)

refant='ea24'
solint='inf'
caltable = 'selfcal-A2255C-B314-pol-0.gcal'
gaincal(vis=viscpol,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='p', combine='', minblperant=4) 
plotcal(caltable=caltable,
        xaxis='time', yaxis='phase',antenna='',poln='RL',
        plotrange=[0,0,-50,50],
        iteration='spw', subplot = 221)
# flagged a few points
plotcal(caltable=caltable,
        xaxis='time', yaxis='amp',antenna='',poln='RL',
        plotrange=[0,0,0.9,1.1],
        iteration='spw', subplot = 221)
applycal(vis=viscpol,gaintable=caltable,interp='linear',flagbackup=False) 
clean(vis=viscpol,imagename='A2255C-14B314-I-selcal_1',
      field='',spw='',
      mode='mfs',
      nterms=1,
      niter=50000,
      gain=0.1,
      psfmode='clark',
      imagermode='', 
      multiscale=[0, 4, 12, 36], smallscalebias=0.9,
      imsize=[6000,5000], cell=['1.0arcsec'],
      stokes='I',
      weighting='briggs',robust=0.5,
      pbcor=False,
      usescratch=False,
      interactive=False,
      gridmode='widefield',wprojplanes=64)
# It's bad compared to images before polarization calibrations. I don't know if it is due to my calibrations or different CLEAN settings
# Also to make it faster I'm making the field smaller and define outlier objects.
clean(vis=viscpol,imagename='A2255C-14B314-I-selcal_1_2',
	  outlierfile='outlier1.txt',	
      field='',spw='',
      mode='mfs',
      nterms=1,
      niter=50000,
      gain=0.1,
      psfmode='clark',
      imagermode='', 
      multiscale=[0, 4, 12, 36], smallscalebias=0.5,
      imsize=[2304,2800], cell=['1.0arcsec'],
      stokes='I',
      weighting='briggs',robust=0.5,
      pbcor=False,
      usescratch=False,
      interactive=False,
      gridmode='widefield',wprojplanes=64)
# Still bad so I will try the exact same settings as before for CLEAN but a smaller field.
clean(vis=viscpol,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B314-I-selcal_1_3',imsize=[2304,2800],outlierfile='outlier-2.txt',cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=viscpol,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B314-I-selcal_1_3',imsize=[2304,2800],outlierfile='outlier-2.txt',cell='1.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)

