## CASA scripts to reduce L band data in C configuration 
vis='14B-165.sb29637172.eb29985563.56972.85897636574.ms'
split(vis=vis,outputvis='A2255C-14B574.ms',field='3')
visc='A2255C-14B574.ms'
flagmanager(vis=visc,mode='save',versionname='BeforeFirstFlag.ms')
flagdata(vis=visc,action='apply',spw='3',scan='58',mode='manual')
flagdata(vis=visc,action='apply',spw='3',mode='manual')
flagdata(vis=visc,action='apply',spw='1',mode='manual')
flagdata(vis=visc,action='apply',spw='2',mode='manual')
flagdata(vis=visc,action='apply',spw='4:3~29',scan='7~46',mode='manual')
flagdata(vis=visc,action='apply',spw='0',mode='manual')
flagdata(vis=visc,action='apply',spw='14:16~60',mode='manual')
flagdata(vis=visc,action='apply',spw='15:3~18,15:21~28',mode='manual')
flagdata(vis=visc,action='apply',spw='10:33~34,10:36~39,10:42~47',mode='manual')

statwt(vis=visc,dorms=False,byantenna=False,spw='',minsamp=2,datacolumn='corrected',timebin='0s')
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B574-0',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=30000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
flagmanager(vis=visc,mode='save',versionname='BeforeFirstgaincal.ms')
flagdata(vis=visc,action='apply',spw='7:47~48',mode='manual')
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B574-0',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=300,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)

visc='A2255C-14B574.ms'
vis=visc
refant='ea24'
solint='inf'
caltable = 'selfcal-A2255C-C-0.gcal'
gaincal(vis=visc,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='p', combine='', minblperant=4) 
plotcal(caltable=caltable,
        xaxis='time', yaxis='phase',
        plotrange=[0,0,-50,50],
        iteration='spw', subplot = 221)
applycal(vis=visc,gaintable=caltable,interp='linear',flagbackup=False) 

clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B574-1',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=80000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B574-1',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=80000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B574-1',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.15,gridmode='widefield',wprojplanes=64)

refant='ea24'
solint='180'
caltable = 'selfcal-A2255C-C-1.gcal'
gaincal(vis=visc,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='ap', combine='', minblperant=4) 
plotcal(caltable=caltable,
        xaxis='time', yaxis='amp',
        plotrange=[0,0,0,2],
        iteration='spw', subplot = 221)
flagmanager(vis=visc,mode='save',versionname='BeforeLastgaincal.ms')
applycal(vis=visc,gaintable=caltable,interp='linear',flagbackup=False) 
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B574-2',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B574-2',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.15,gridmode='widefield',wprojplanes=64)
clean(vis=visc,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255C-14B574-2',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.15,gridmode='widefield',wprojplanes=64)
### I think We are done with field 3
### Now lets do field 2
#############
#############
split(vis=vis,outputvis='A2255N-14B574.ms',field='2')
visn='A2255N-14B574.ms'
flagmanager(vis=visn,mode='save',versionname='BeforeFirstFlag-visn.ms')
flagdata(vis=visn,action='apply',spw='3',mode='manual')
flagdata(vis=visn,action='apply',spw='1',mode='manual')
flagdata(vis=visn,action='apply',spw='14:16~60',mode='manual')
flagdata(vis=visn,action='apply',spw='15:3~18,15:21~28',mode='manual')
flagdata(vis=visn,action='apply',spw='10:27~47,10:3~5',mode='manual')
flagdata(vis=visn,action='apply',spw='4:3~38',scan='6~48',mode='manual')
flagdata(vis=visn,action='apply',spw='2:3~4,2:7~9,2:12~14,2:33~47',scan='35~47,59~61',mode='manual')
flagdata(vis=visn,action='apply',spw='2:3~4,2:7~9,2:12~14,2:33~47',mode='manual')
flagdata(vis=visn,action='apply',spw='2:3~15,2:24~64',scan='6~12,35~61',mode='manual')
flagdata(vis=visn,action='apply',spw='0:16,0:19~25,0:31~42,0:54~63',mode='manual')
flagdata(vis=visn,action='apply',spw='7:47',mode='manual')
flagmanager(vis=visn,mode='save',versionname='BeforeFirstCal-visn.ms')

statwt(vis=visn,dorms=False,byantenna=False,spw='',minsamp=2,datacolumn='corrected',timebin='0s')
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255N-14B574-0',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=30000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)


refant='ea24'
solint='inf'
caltable = 'selfcal-A2255N-C-0.gcal'
gaincal(vis=visn,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='p', combine='', minblperant=4) 
plotcal(caltable=caltable,
        xaxis='time', yaxis='phase',
        plotrange=[0,0,-50,50],
        iteration='spw', subplot = 221)
# Half of the spw 14 and 15 have really bad solutions. Maybe I want to flag them later.
applycal(vis=visn,gaintable=caltable,interp='linear',flagbackup=False) 
flagdata(vis=visn,action='apply',spw='15:19~20',mode='manual')

clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255N-14B574-1',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
flagdata(vis=visn,action='apply',spw='0,2',mode='manual')
statwt(vis=visn,dorms=False,byantenna=False,spw='',minsamp=2,datacolumn='corrected',timebin='0s')
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255N-14B574-2',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)

flagdata(vis=visn,action='apply',spw='7:48,13:34~35',mode='manual')
flagdata(vis=visn,action='apply',antenna='ea01',spw='15:60,10:54~59,4:4~11,5:52~55',mode='manual')
flagdata(vis=visn,action='apply',antenna='ea02',spw='10:52~60,4:3~14,5:52~56',mode='manual')
flagdata(vis=visn,action='apply',antenna='ea03',spw='4:3~11,4:32,5:52~56,5:3~6,5:10~11,5:21~22,10:49~59',mode='manual')
flagdata(vis=visn,action='apply',antenna='ea05',spw='4:3~15,5:21~23',mode='manual')
flagdata(vis=visn,action='apply',antenna='ea06',spw='4:3~15,5:21~23',mode='manual')
flagdata(vis=visn,action='apply',spw='4:3~15',mode='manual')
flagdata(vis=visn,action='apply',antenna='ea10',spw='5:51~55',mode='manual')
flagdata(vis=visn,action='apply',antenna='ea10',spw='10:57~60',scan='33',mode='manual')
flagdata(vis=visn,action='apply',antenna='ea10',spw='10:53~57',scan='41',mode='manual')
flagdata(vis=visn,action='apply',antenna='ea13',spw='4:16~22,4:33~37,5:21~22,5:47,6:7~9,6:57~59,10:49~51,10:53~60',mode='manual')
flagdata(vis=visn,action='apply',antenna='ea16',spw='4:17~27,10:48~59,10:26',mode='manual')
flagdata(vis=visn,action='apply',antenna='ea19',spw='5:46~48,13:36,15:32~33',mode='manual')
flagdata(vis=visn,action='apply',antenna='ea21',spw='5:9~11,5:51~53',mode='manual')
flagdata(vis=visn,action='apply',antenna='ea24',spw='5:46~48,13:36,15:32',mode='manual')
flagdata(vis=visn,action='apply',antenna='ea25',spw='5:46~48,13:36,15:32',mode='manual')
flagdata(vis=visn,action='apply',antenna='ea28',spw='4:39~60',mode='manual')

statwt(vis=visn,dorms=False,byantenna=False,spw='',minsamp=2,datacolumn='corrected',timebin='0s')
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255N-14B574-3',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)

# Antenna 4 and 11 are bad
flagmanager(vis=visn,mode='save',versionname='Afterall-visn.ms')
flagdata(vis=visn,action='apply',spw='15:59~60',scan='6',mode='manual')
flagdata(vis=visn,action='apply',spw='15:59~60',scan='45',mode='manual')

flagdata(vis=visn,action='apply',spw='14:3~6',mode='manual')


refant='ea19'
solint='inf'
caltable = 'selfcal-A2255N-C-1.gcal'
gaincal(vis=visn,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='p', combine='', minblperant=4) 
### It's bad
refant='ea19'
solint='60s'
caltable = 'selfcal-A2255N-C-2.gcal'
gaincal(vis=visn,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='p', combine='', minblperant=4) 
#Awfullll
flagdata(vis=visn,action='apply',spw='15',mode='manual')
statwt(vis=visn,dorms=False,byantenna=False,spw='',minsamp=2,datacolumn='corrected',timebin='0s')
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255N-14B574-4',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)

refant='ea19'
solint='inf'
caltable = 'selfcal-A2255N-C-3.gcal'

gaincal(vis=visn,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='p', combine='', minblperant=4) 
applycal(vis=visn,gaintable=caltable,interp='linear',flagbackup=False) 
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255N-14B574-5',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255N-14B574-5',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)

caltable = 'selfcal-A2255N-C-4.gcal'
gaincal(vis=visn,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='p', combine='', minblperant=4) 
plotcal(caltable=caltable,
        xaxis='time', yaxis='phase',
        plotrange=[0,0,-50,50],
        iteration='spw', subplot = 221)
flagmanager(vis=visn,mode='save',versionname='Beforebaseline-visn.ms')
flagdata(vis=visn,action='apply',spw='14',antenna='ea08&ea25;ea05&ea25;ea04&ea28;ea08&ea26',mode='manual')
flagdata(vis=visn,action='apply',spw='14',antenna='ea14&ea08;ea13&ea28;ea13&ea16;ea17&ea28;ea13&ea20;ea20&ea28;ea04&ea17;ea06&ea20;ea17&ea20;ea14&ea15;ea08&ea13',mode='manual')

caltable = 'selfcal-A2255N-C-5.gcal'
gaincal(vis=visn,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='p', combine='', minblperant=4) 
flagdata(vis=visn,action='apply',spw='14',scan='48~80',mode='manual')
caltable = 'selfcal-A2255N-C-6.gcal'
gaincal(vis=visn,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='p', combine='', minblperant=4) 
applycal(vis=visn,gaintable=caltable,interp='linear',flagbackup=False) 
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255N-14B574-6',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255N-14B574-6',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)

caltable = 'selfcal-A2255N-C-7.gcal'
gaincal(vis=visn,field='', caltable=caltable, spw='', solint=solint, refant=refant, calmode='ap', combine='', minblperant=4) 
applycal(vis=visn,gaintable=caltable,interp='linear',flagbackup=False) 
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255N-14B574-7',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255N-14B574-7',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.1,gridmode='widefield',wprojplanes=64)
clean(vis=visn,mode='mfs',nterms=2,field='',spw='',antenna='',imagename='A2255N-14B574-7',imsize=[2400,2400],cell='3.0arcsec',interactive=False,usescratch=False,niter=100000,weighting='briggs',robust=0.5,gain=0.12,gridmode='widefield',wprojplanes=64)
##################################### DDDDDOOOOONNNNEEEEEE
# Now removing extra files and directories
rm -r A2255N-14B574-1.*
rm -r A2255N-14B574-2.*
rm -r A2255N-14B574-3.*
rm -r A2255N-14B574-4.*
rm -r A2255N-14B574-5.*
rm -r A2255N-14B574-6.*
rm -r selfcal-A2255N-C-1.gcal
rm -r selfcal-A2255N-C-2.gcal
rm -r selfcal-A2255N-C-3.gcal
rm -r selfcal-A2255N-C-4.gcal
rm -r selfcal-A2255N-C-6.gcal

