import numpy as np

def polcalib(vis,calfield,calfield2,I,alpha,pi,angle,sp,freq,ref_ant,tables,gainfields):
	for i in range(len(sp)):
		print 'Calibrating SPW ', sp[i]
		tables=['14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_3.gc.tbl','14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_4.opac.tbl','14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_5.rq.tbl','14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_6.ants.tbl','14B-165.sb30142041.eb30465088.57081.464200752314.ms.finaldelay.k','14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalBPcal.b','14B-165.sb30142041.eb30465088.57081.464200752314.ms.averagephasegain.g','14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalampgaincal.g','14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalphasegaincal.g']
		myset=setjy(vis=vis, field=calfield, standard='manual',spw=sp[i], fluxdensity=[I[i],0,0,0], spix=[alpha[i],0], reffreq=freq[i],polindex=[pi[i],0], polangle=[angle,0],scalebychan=True, usescratch=False)
		plotms(vis=vis,field=calfield,spw=sp[i],correlation='RR',timerange='',antenna='',xaxis='channel',yaxis='amp',ydatacolumn='model',plotfile='plotms-Field'+calfield+'-spw'+sp[i]+'-model-amp-RR.png',overwrite=True,showgui=False)
		plotms(vis=vis,field=calfield,spw=sp[i],correlation='RL',xaxis='channel',yaxis='amp',ydatacolumn='model',plotfile='plotms-Field'+calfield+'-spw'+sp[i]+'-model-amp-RL.png',overwrite=True,showgui=False)
		plotms(vis=vis,field=calfield,spw=sp[i],correlation='RL',xaxis='channel',yaxis='phase',ydatacolumn='model',plotfile='plotms-Field'+calfield+'-spw'+sp[i]+'-model-phase-RL.png',overwrite=True,plotrange=[-1,-1,-180,180],showgui=False)	
		#Solving for the Cross-Hand delays
		# In pipeline calibrations antenna ea09 is used as the refant.
		gaincal(vis=vis, caltable='A2255-spw'+sp[i]+'.Kcross',field=calfield, spw=sp[i]+':5~58',gaintype='KCROSS', solint='inf', combine='scan', refant=ref_ant,gaintable=tables,gainfield=gainfields,parang=T)
		plotcal(caltable='A2255-spw'+sp[i]+'.Kcross',xaxis='antenna',yaxis='delay',figfile='plotcal_A2255-Kcross-delay_spw'+sp[i]+'.png',showgui=False)
		newtables=tables
		newtables.append('A2255-spw'+sp[i]+'.Kcross')
		polcal(vis=vis,caltable='A2255_spw'+sp[i]+'.D',field=calfield2,spw=sp[i]+':5~58',refant=ref_ant,poltype='Df+QU',solint='inf',combine='scan',gaintable=newtables,gainfield=['','','','','','','',calfield2,calfield2,''])
		#plotcal(caltable='A2255_spw'+sp[i]+'.D',xaxis='chan',yaxis='amp',spw=sp[i],iteration='antenna')
		#plotcal(caltable='A2255_spw'+sp[i]+'.D',xaxis='chan',yaxis='phase',spw=sp[i],field='',iteration='antenna',plotrange=[-1,-1,-180,180])
		plotcal(caltable='A2255_spw'+sp[i]+'.D',xaxis='antenna',yaxis='amp',figfile='plotcal_A2255-D-spw'+sp[i]+'.png',showgui=False)
		#Solving for the R-L polarization angle
		newtables.append('A2255_spw'+sp[i]+'.D')
		polcal(vis=vis,caltable='A2255_spw'+sp[i]+'.X',field=calfield,spw=sp[i],combine='scan',poltype='Xf',solint='inf',gaintable=newtables,gainfield=['','','','','','','',calfield,calfield,'',''])
		plotcal(caltable='A2255_spw'+sp[i]+'.X',xaxis='chan',yaxis='phase',figfile='plotcal_A2255-X-spw'+sp[i]+'.png',showgui=False)
	return 'All polarization calibrations are done.'

# Example of running the polcalib function 
# execfile 'polcalib.py' can be used to run this script from CASA terminal.
Lfreq=['1.008GHz','1.072GHz','1.136GHz','1.2GHz','1.264GHz','1.328GHz','1.392GHz','1.456GHz','1.52GHz','1.584GHz','1.648GHz','1.712GHz','1.776GHz','1.84GHz','1.904GHz','1.968GHz']
I286=np.array([17.779,17.276,16.807,16.367,15.955,15.568,15.203,14.857,14.531,14.221,13.927,13.647,13.381,13.126,12.884,12.651])
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
A286=np.array([alpha0,alpha1,alpha2,alpha3,alpha4,alpha5,alpha6,alpha7,alpha8,alpha9,alpha10,alpha11,alpha12,alpha13,alpha14,alpha15])
c286=np.array([0.086,0.087,0.089,0.09,0.092,0.093,0.094,0.095,0.0963,0.0976,0.099,0.099,0.0995,0.1,0.1005,0.101])
vis='14B-165.sb30142041.eb30465088.57081.464200752314.ms'
sp=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
calfield='0' #for 3C286
calfield2='1' # for 3C343 which has a good parallactic angle coverage
ref_ant='ea09'
tables=['14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_3.gc.tbl','14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_4.opac.tbl','14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_5.rq.tbl','14B-165.sb30142041.eb30465088.57081.464200752314.ms.hifv_priorcals.s5_6.ants.tbl','14B-165.sb30142041.eb30465088.57081.464200752314.ms.finaldelay.k','14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalBPcal.b','14B-165.sb30142041.eb30465088.57081.464200752314.ms.averagephasegain.g','14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalampgaincal.g','14B-165.sb30142041.eb30465088.57081.464200752314.ms.finalphasegaincal.g']
gainfields=['','','','','','','',calfield,calfield]
angle=33*pi/180 # polarization angle of 33 degrees converted to radians for 3C286
polcalib(vis=vis,calfield=calfield,calfield2=calfield2,I=I286,alpha=A286,pi=c286,angle=angle,sp=sp,freq=Lfreq,ref_ant=ref_ant,tables=tables,gainfields=gainfields)