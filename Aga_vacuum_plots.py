import matplotlib.pyplot as plt
import pytimber
from pytimber import pagestore
import calendar, time
import math
#%matplotlib notebook
#####COMBINING SCRIPTS FOR MKI2 AND MKI8#####


# DEFINING FUNCTIONS

# sorting by the length of the array
def sort(x):
    return sorted(x, key=lambda time: time[1], reverse=True)


# choosing second magnet(in array length) for alignment
def get_magnet(x):
    return x[1]


# calculating elapsed time
elapb1 = []

elapb2 = []

def elapsed(ts, ts0):
    return (ts - ts0) / 3600

# new script for beam elapsed time
beam_elapb1 = []
beam_elap_running_totalb1=0

beam_elapb2 = []
beam_elap_running_totalb2=0

beam_intb1 = []
beam_chargeb1=0
beam_intb2 = []
beam_chargeb2=0

def beam_elapsedb1(tsOne, tsZero, bi, counti):
    global beam_elap_running_totalb1
    #print(counti)
    if bi >= 10 ** 12 and counti>0:
        beam_elap_running_totalb1=beam_elap_running_totalb1+(tsOne - tsZero) / 3600
        #print(beam_elap_running_total, tsOne, tsZero, counti)
        return beam_elap_running_totalb1
    
    else: 
        return beam_elap_running_totalb1+10 ** (-12)
    
def beam_elapsedb2(tsOne, tsZero, bi, counti):
    global beam_elap_running_totalb2
    #print(counti)
    if bi >= 10 ** 12 and counti>0:
        beam_elap_running_totalb2=beam_elap_running_totalb2+(tsOne - tsZero) / 3600
        #print(beam_elap_running_total, tsOne, tsZero, counti)
        return beam_elap_running_totalb2
    
    else: 
        return beam_elap_running_totalb2+10 ** (-12)    

def beam_integralb1(tsOne, TsZero, Ione, Izero, counti):
    global beam_chargeb1
    if Ione >= 10 ** 12 and counti>0:
        if math.isnan(Izero): 
            Izero=0
        beam_chargeb1 = beam_chargeb1+((tsOne-TsZero)*(Ione+Izero)*1.602176*10**(-19))/2
        #print(tsOne, (tsOne-TsZero),'Izero=',Izero,Ione,(Ione+Izero)*1.602176*10**(-19), beam_chargeb1, counti)
        return beam_chargeb1
    
    else:
        return beam_chargeb1
    
def beam_integralb2(tsOne, TsZero, Ione, Izero, counti):
    global beam_chargeb2
    if Ione >= 10 ** 12 and counti>0:
        if math.isnan(Izero): 
            Izero=0
        beam_chargeb2 = beam_chargeb2+((tsOne-TsZero)*(Ione+Izero)*1.602176*10**(-19))/2
        #print((tsOne-TsZero),(Ione+Izero)*1.602176*10**(-19), beam_chargeb2, counti)
        return beam_chargeb2
    
    else:
        return beam_chargeb2
# calculating normalized pressure MKI2
normAb1 = []
normBb1 = []
normCb1 = []
normDb1 = []
normDCb1 = []
normAQ4b1 = []
normQ5Db1 = []
normBAb1 = []
normCBb1 = []

# calculating normalized pressure MKI8
normAb2 = []
normBb2 = []
normCb2 = []
normDb2 = []
normDCb2 = []
normAQ4b2 = []
normQ5Db2 = []
normBAb2 = []
normCBb2 = []



def normalization(p, bi):
    if bi >= 10 ** 12:
        return p / bi
    else:
        return 10 ** -99

# RUNNING THE COD
xupperlim = 100 #Charge Coloumbs
# xupperlim = 1550 for the whole of 2017 Run
#defining the time window
#MKI2 time
# 29/4/2017: LHC circulating protons for 1st time in 2017 https://home.cern/news/news/accelerators/lhc-has-restarted-its-2017-run
# 30/3/2018: LHC circulating protons for 1st time in 2018  https://home.cern/news/news/accelerators/beams-are-back-lhc

t1b1 = "2012-07-01 00:00:00"
t2b1 = "2012-07-01 23:59:59"
t1b2 = "2012-07-01 00:00:00"
t2b2 = "2012-07-01 23:59:59"

# t1b1 = "2015-06-01 00:00:00" # was 2017-04-29
# t2b1 = "2015-07-30 23:59:59"

# t1b2 = "2015-06-01 00:00:00" # was 2018-03-30
# t2b2 = "2015-07-30 23:59:59" # was 2018-10-01
PlotVsTime = "N" # Y or N
PlotBothMagD_Interconnects = "N"
PlotBothInterconnects = "N"

#===============================================================================
# #===============================================================================
# t1b1 = "2018-04-20 00:00:00"
# t2b1 = "2018-05-29 23:59:59"
# # 
# t1b2 = "2018-04-20 00:00:00"
# t2b2 = "2018-05-29 23:59:59"
# #===============================================================================
#===============================================================================

t0_beam2_elap_running_total_start_counter = "2012-07-01 00:00:00"
#t0_beam2_elap_running_total_start_counter = "2018-04-16 00:00:00"
#t1b2 = "2018-04-20 00:00:00"
#t1b2 = "2018-05-11 00:00:00"
#t2b2 = "2018-05-29 23:59:59"

# subtract 0s to keep in UTC time.
# subtract 2 * 3600s to convert from Local time to UTC time
t1sb1= calendar.timegm(time.strptime(t1b1,"%Y-%m-%d %H:%M:%S")) - 0 * 3600
t2sb1= calendar.timegm(time.strptime(t2b1,"%Y-%m-%d %H:%M:%S")) - 0 * 3600
beam1_elap_running_total=0
t0_beam1_elap_running_total_start_counter = "2012-07-01 00:00:00"

t0b1=beam1_elap_running_total

titletextb1="Start time (MKI2) = ",t1b1,"  End time (MKI2) = ",t2b1," Start beam1 elapsed time counter = ",int(t0b1*10)/10,"hrs, since:",t0_beam1_elap_running_total_start_counter
print(titletextb1)

#MKI8 time

t1sb2 = calendar.timegm(time.strptime(t1b2,"%Y-%m-%d %H:%M:%S")) - 0 * 3600
t2sb2 = calendar.timegm(time.strptime(t2b2,"%Y-%m-%d %H:%M:%S")) - 0 * 3600
beam2_elap_running_total=0


t0b2=beam2_elap_running_total

titletextb2="Start time (MKI8) = ",t1b2,"  End time (MKI8) = ",t2b2," Start beam1 elapsed time counter = ",int(t0b2*10)/10,"hrs, since:",t0_beam2_elap_running_total_start_counter
print(titletextb2)

# now = time.time()

# opening the connection to the database
start_time = time.time()
#pageStore = pagestore.PageStore('lhcPressure.db', '/eos/project/l/lhc-injection-kickers/public/vacuum_data/LHC_PRESSURE/02')
pageStore = pagestore.PageStore('lhcPressure.db', './data/LHCpressure_data/')

parameters0b1=["MKI.A5L2.B1:PRESSURE", "MKI.B5L2.B1:PRESSURE", "MKI.C5L2.B1:PRESSURE", "MKI.D5L2.B1:PRESSURE"]
parameters0b2= ["MKI.A5R8.B2:PRESSURE", "MKI.B5R8.B2:PRESSURE", "MKI.C5R8.B2:PRESSURE", "MKI.D5R8.B2:PRESSURE"]

# extracting aligned data MKI2
parametersb1 = parameters0b1 + ["VGPB.137.5L2.B.PR", "VGPB.14.5L2.B.PR", "VGPB.176.5L2.B.PR", "VGPB.59.5L2.B.PR",
                            "VGPB.98.5L2.B.PR", "LHC.BCTFR.A6R4.B1:BEAM_INTENSITY", "MKI.A5L2.B1:PRESSURE_INT", 
                            "MKI.B5L2.B1:PRESSURE_INT", "MKI.C5L2.B1:PRESSURE_INT", "MKI.D5L2.B1:PRESSURE_INT"]
# extracting aligned data MKI8
parametersb2 = parameters0b2 + ["VGPB.138.5R8.R.PR", "VGPB.14.5R8.R.PR", "VGPB.176.5R8.R.PR", "VGPB.59.5R8.R.PR",
                            "VGPB.98.5R8.R.PR", "LHC.BCTFR.A6R4.B2:BEAM_INTENSITY", "MKI.A5R8.B2:PRESSURE_INT", 
                            "MKI.B5R8.B2:PRESSURE_INT", "MKI.C5R8.B2:PRESSURE_INT", "MKI.D5R8.B2:PRESSURE_INT"]
#parameters = parameters0 + ("VGPB.138.5R8.R.PR", "VGPB.176.5R8.R.PR", 
#                            "LHC.BCTFR.A6R4.B2:BEAM_INTENSITY")

datab1 = pageStore.get(parametersb1, t1sb1, t2sb1)
datab2 = pageStore.get(parametersb2, t1sb2 ,t2sb2 )



# the dictionary returned contains one list of timestamps and one entry per variable with a list of values.
# all parameters are aligned with the first one

# separating time data from pressure/intensity data MKI2
aligned_timeb1 = datab1['MKI.A5L2.B1:PRESSURE'][0]
pressureAb1 = datab1['MKI.A5L2.B1:PRESSURE'][1]
pressureBb1 = datab1['MKI.B5L2.B1:PRESSURE'][1]
pressureCb1 = datab1['MKI.C5L2.B1:PRESSURE'][1]
#pressureCb1 = datab1['VGPB.118.5L2.C.PR'][1] 
# Note: MKI.C5L2.B1:PRESSURE valid from 20/6/2018 @ 13:40hrs
# Note: VGPB.118.5L2.C.PR is much lower time resolution than MKI.C5L2.B1:PRESSURE
pressureDb1 = datab1['MKI.D5L2.B1:PRESSURE'][1]
pressureDCb1 = datab1['VGPB.137.5L2.B.PR'][1]
pressureAQ4b1 = datab1['VGPB.14.5L2.B.PR'][1]
pressureQ5Db1 = datab1['VGPB.176.5L2.B.PR'][1]
pressureBAb1 = datab1['VGPB.59.5L2.B.PR'][1]
pressureCBb1 = datab1['VGPB.98.5L2.B.PR'][1]
intensityb1 = datab1['LHC.BCTFR.A6R4.B1:BEAM_INTENSITY'][1]
pressureA_intb1 = datab1['MKI.A5L2.B1:PRESSURE_INT'][1]
pressureB_intb1 = datab1['MKI.B5L2.B1:PRESSURE_INT'][1]
pressureC_intb1 = datab1['MKI.C5L2.B1:PRESSURE_INT'][1]
pressureD_intb1 = datab1['MKI.D5L2.B1:PRESSURE_INT'][1]

# separating time data from pressure/intensity data MKI8
aligned_timeb2 = datab2['MKI.A5R8.B2:PRESSURE'][0]
pressureAb2 = datab2['MKI.A5R8.B2:PRESSURE'][1]
pressureBb2 = datab2['MKI.B5R8.B2:PRESSURE'][1]
pressureCb2 = datab2['MKI.C5R8.B2:PRESSURE'][1]
pressureDb2 = datab2['MKI.D5R8.B2:PRESSURE'][1]
pressureDCb2 = datab2['VGPB.138.5R8.R.PR'][1]
pressureAQ4b2 = datab2['VGPB.14.5R8.R.PR'][1]
pressureQ5Db2 = datab2['VGPB.176.5R8.R.PR'][1]
pressureBAb2 = datab2['VGPB.59.5R8.R.PR'][1]
pressureCBb2 = datab2['VGPB.98.5R8.R.PR'][1]
intensityb2 = datab2['LHC.BCTFR.A6R4.B2:BEAM_INTENSITY'][1]
pressureA_intb2 = datab2['MKI.A5R8.B2:PRESSURE_INT'][1]
pressureB_intb2 = datab2['MKI.B5R8.B2:PRESSURE_INT'][1]
pressureC_intb2 = datab2['MKI.C5R8.B2:PRESSURE_INT'][1]
pressureD_intb2 = datab2['MKI.D5R8.B2:PRESSURE_INT'][1]

print("*** Number of entries for aligned_time (MKI2) = ", len(aligned_timeb1))
print("*** Number of entries for aligned_time (MKI8) = ", len(aligned_timeb2))






# calculating elapsed time, normalized pressure and beam elapsed time and pressure/normalized pressure
start_time = time.time()
#MKI2
for i in range(len(aligned_timeb1)):
    elapb1.append(elapsed(aligned_timeb1[i], aligned_timeb1[0]))
    beam_elapb1.append(beam_elapsedb1(aligned_timeb1[i], aligned_timeb1[i-1], intensityb1[i], i))    
    normAb1.append(normalization(pressureAb1[i], intensityb1[i]))
    normBb1.append(normalization(pressureBb1[i], intensityb1[i]))
    #normCb1.append(normalization(pressureCb1[i], intensityb1[i]))
    normDb1.append(normalization(pressureDb1[i], intensityb1[i]))
    normDCb1.append(normalization(pressureDCb1[i], intensityb1[i]))
    normAQ4b1.append(normalization(pressureAQ4b1[i], intensityb1[i]))
    normQ5Db1.append(normalization(pressureQ5Db1[i], intensityb1[i]))
    normBAb1.append(normalization(pressureBAb1[i], intensityb1[i]))
    normCBb1.append(normalization(pressureCBb1[i], intensityb1[i]))
    ## problem on following line??
    beam_intb1.append(beam_integralb1(aligned_timeb1[i], aligned_timeb1[i-1], intensityb1[i], intensityb1[i-1],i))
calculation_time = time.time()-start_time
print("Execution time for B1: calculating normalized data, elapsed time and integral: %0.3f seconds." % calculation_time)
start_time = time.time()
#MKI8
for i in range(len(aligned_timeb2)):
    elapb2.append(elapsed(aligned_timeb2[i], aligned_timeb2[0]))
    beam_elapb2.append(beam_elapsedb2(aligned_timeb2[i], aligned_timeb2[i-1], intensityb2[i], i))    
    normAb2.append(normalization(pressureAb2[i], intensityb2[i]))
    normBb2.append(normalization(pressureBb2[i], intensityb2[i]))
    normCb2.append(normalization(pressureCb2[i], intensityb2[i]))
    normDb2.append(normalization(pressureDb2[i], intensityb2[i]))
    normDCb2.append(normalization(pressureDCb2[i], intensityb2[i]))
    normAQ4b2.append(normalization(pressureAQ4b2[i], intensityb2[i]))
    normQ5Db2.append(normalization(pressureQ5Db2[i], intensityb2[i]))
    normBAb2.append(normalization(pressureBAb2[i], intensityb2[i]))
    normCBb2.append(normalization(pressureCBb2[i], intensityb2[i]))
    beam_intb2.append(beam_integralb2(aligned_timeb2[i], aligned_timeb2[i-1], intensityb2[i], intensityb2[i-1],i))
    #print(aligned_timeb2[i], aligned_timeb2[i-1], intensityb2[i], intensityb2[i-1],i)
calculation_time = time.time()-start_time
print("Execution time for B2: calculating normalized data and elapsed time: %0.3f seconds." % calculation_time)

titletextb1='         MKI2: Start time = ' +  str(t1b1) + ', End time = ' + str(t2b1) + ', Start/End beam1 elapsed time = ' + str(int(t0b1*10)/10) + '/' + str(int(10*beam_elap_running_totalb1)/10) + 'hrs (' + str(int(beam_chargeb1*10)/10) + 'C), since ' + t0_beam1_elap_running_total_start_counter
print(titletextb1)
print('MKI8: Start time = ' +  str(t1b2) + ', End time = ' + str(t2b2) + ', Start/End beam2 elapsed time = ' + str(int(t0b2*10)/10))
##print(str(int(10*beam_elap_running_totalb2)/10) + 'hrs (')
##print(beam_chargeb2)
##print(str(int(beam_chargeb2*10)/10) + 'C), since ')
##print(t0_beam2_elap_running_total_start_counter)
titletextb2='MKI8: Start time = ' +  str(t1b2) + ', End time = ' + str(t2b2) + ', Start/End beam2 elapsed time = ' + str(int(t0b2*10)/10) + '/' + str(int(10*beam_elap_running_totalb2)/10) + 'hrs (' + str(int(beam_chargeb2*10)/10) + 'C), since ' + t0_beam2_elap_running_total_start_counter
print(titletextb2)



print("Plot: Beam1 Integral & Beam Intensity vs. Aligned Time")
fig, ax1 = plt.subplots(figsize=(18,6))
plt.suptitle(titletextb1, fontsize=11,y=0.98)
plt.title(titletextb2, fontsize=11, y=1.03)
#ax1.plot(aligned_timeb1, beam_intb1, 'o-', color='blue', linewidth=1, markersize=0, label='Beam 1 Integral')
#ax1.plot(aligned_timeb2, beam_intb2, 'o-', color='red', linewidth=1, markersize=0, label='Beam 2 Integral')
ax1.plot(aligned_timeb1, beam_intb1, 'o-', color='blue', linewidth=1, markersize=0, label='Beam 1 Integral')
ax1.set_ylabel(r'Beam Integral (C)')
ax1.set_ylim(0, )
#ax1.plt.xticks(fontsize=12.5)#ax1.plt.yticks(fontsize=13)
ax1.xaxis.label.set_size(13.5)
ax1.yaxis.label.set_size(13.5)
#ax1.set_ylim(10 ** -25, 2*10 ** -20)
ax1.set_xlabel(r'Date & (UTC) time')
pytimber.set_xaxis_date(bins=7)
plt.legend(loc=2, prop={'size':11.5})
ax2 = ax1.twinx()
#ax2.plot(aligned_timeb1, intensityb1, 'o-', color='blue', markersize=1, label='Beam intensity B1')
#ax2.plot(aligned_timeb2, intensityb2, 'o-', color='red', markersize=1, label='Beam intensity B2')
#ax2.plot(aligned_timeb1, intensityb1, 'o-', color='blue', markersize=1, label='Beam intensity B1')
ax2.plot(aligned_timeb1, normQ5Db1, 'o-', color='blue', markersize=1, label='Beam intensity B1')
ax2.set_ylabel(r'Normalized pressure (mbar/p)')
#ax2.yaxis.label.set_size(13.5)
ax2.tick_params(axis='y', colors='green')
ax2.yaxis.label.set_color('green')
ax2.semilogy()
ax2.set_ylim(10 ** -25, 1*10 ** -21)
#ax2.set_ylim(0, 3.5*10 ** 14)
plt.legend(prop={'size':11.5})
plt.show()

print("Plot: Beam2 Integral & Beam Intensity vs. Aligned Time")
fig, ax1 = plt.subplots(figsize=(18,6))
plt.suptitle(titletextb1, fontsize=11,y=0.98)
plt.title(titletextb2, fontsize=11, y=1.03)
#ax1.plot(aligned_timeb1, beam_intb1, 'o-', color='blue', linewidth=1, markersize=0, label='Beam 1 Integral')
ax1.plot(aligned_timeb2, beam_intb2, 'o-', color='red', linewidth=1, markersize=0, label='Beam 2 Integral')
#ax1.plot(aligned_timeb1, beam_intb1, 'o-', color='blue', linewidth=1, markersize=0, label='Beam 1 Integral')
ax1.set_ylabel(r'Beam Integral (C)')
ax1.set_ylim(0, )
#ax1.plt.xticks(fontsize=12.5)#ax1.plt.yticks(fontsize=13)
ax1.xaxis.label.set_size(13.5)
ax1.yaxis.label.set_size(13.5)
#ax1.set_ylim(10 ** -25, 2*10 ** -20)
ax1.set_xlabel(r'Date & (UTC) time')
pytimber.set_xaxis_date(bins=7)
plt.legend(loc=2, prop={'size':11.5})
ax2 = ax1.twinx()
#ax2.plot(aligned_timeb1, intensityb1, 'o-', color='blue', markersize=1, label='Beam intensity B1')
ax2.plot(aligned_timeb2, intensityb2, 'o-', color='red', markersize=1, label='Beam intensity B2')
#ax2.plot(aligned_timeb1, intensityb1, 'o-', color='blue', markersize=1, label='Beam intensity B1')
ax2.set_ylabel(r'Beam intensity (p)')
#ax2.yaxis.label.set_size(13.5)
ax2.tick_params(axis='y', colors='green')
ax2.yaxis.label.set_color('green')
ax2.set_ylim(0, 3.5*10 ** 14)
plt.legend(prop={'size':11.5})
plt.show()

if PlotVsTime == "N":
    print("Plot: Beam Integral & Beam Intensity vs. Elapsed Beam Time")
    fig, ax1 = plt.subplots(figsize=(18,6))
    plt.suptitle(titletextb1, fontsize=11,y=0.98)
    plt.title(titletextb2, fontsize=11, y=1.03)
    ax1.plot(beam_elapb1, beam_intb1, 'o-', color='blue', linewidth=1, markersize=0, label='Beam 1 Integral')
    ax1.plot(beam_elapb2, beam_intb2, 'o-', color='red', linewidth=1, markersize=0, label='Beam 2 Integral')
    ax1.set_ylabel(r'Beam Integral (C)')
    ax1.set_ylim(0, )
    #ax1.plt.xticks(fontsize=12.5)
    #ax1.plt.yticks(fontsize=13)
    ax1.xaxis.label.set_size(13.5)
    ax1.yaxis.label.set_size(13.5)
    #ax1.set_ylim(10 ** -25, 2*10 ** -20)
    ax1.set_xlabel(r'Beam Elapsed Time (>10**12 p)')
    #pytimber.set_xaxis_date(bins=7)
    plt.legend(loc=2, prop={'size':11.5})
    ax2 = ax1.twinx()
    ax2.plot(beam_elapb1, intensityb1, 'o-', color='blue', markersize=1, label='Beam intensity B1')
    ax2.plot(beam_elapb2, intensityb2, 'o-', color='red', markersize=1, label='Beam intensity B2')
    ax2.set_ylabel(r'Beam intensity (p)')
    #ax2.yaxis.label.set_size(13.5)
    ax2.tick_params(axis='y', colors='green')
    ax2.yaxis.label.set_color('green')
    ax2.set_ylim(0, 3.5*10 ** 14)
    plt.legend(prop={'size':11.5})
    plt.show()

if PlotVsTime == "Y":
    print("Plot: Beam Integral & Beam Intensity vs. Aligned Time")
    fig, ax1 = plt.subplots(figsize=(18,6))
    plt.suptitle(titletextb1, fontsize=11,y=0.98)
    plt.title(titletextb2, fontsize=11, y=1.03)
    ax1.plot(aligned_timeb1, beam_intb1, 'o-', color='blue', linewidth=1, markersize=0, label='Beam 1 Integral')
    ax1.plot(aligned_timeb2, beam_intb2, 'o-', color='red', linewidth=1, markersize=0, label='Beam 2 Integral')
    ax1.set_ylabel(r'Beam Integral (C)')
    ax1.set_ylim(0, )
    #ax1.plt.xticks(fontsize=12.5)
    #ax1.plt.yticks(fontsize=13)
    ax1.xaxis.label.set_size(13.5)
    ax1.yaxis.label.set_size(13.5)
    #ax1.set_ylim(10 ** -25, 2*10 ** -20)
    ax1.set_xlabel(r'Date & (UTC) time')
    pytimber.set_xaxis_date(bins=7)
    plt.legend(loc=2, prop={'size':11.5})
    ax2 = ax1.twinx()
    ax2.plot(aligned_timeb1, intensityb1, 'o-', color='blue', markersize=1, label='Beam intensity B1')
    ax2.plot(aligned_timeb2, intensityb2, 'o-', color='red', markersize=1, label='Beam intensity B1')
    ax2.set_ylabel(r'Beam intensity (p)')
    #ax2.yaxis.label.set_size(13.5)
    ax2.tick_params(axis='y', colors='green')
    ax2.yaxis.label.set_color('green')
    ax2.set_ylim(0, 3.5*10 ** 14)
    plt.legend(prop={'size':11.5})
    plt.show()

print("Plot: Magnet Norm Pressure vs. Beam Integral")
plt.figure(figsize=(18,6))
plt.suptitle(titletextb1, fontsize=11,y=0.98)
plt.title(titletextb2, fontsize=11, y=1.03)
#plt.suptitle(titletextb2, fontsize=11, y=0.94)
plt.plot(beam_intb1, normDb1, 'o-', color='blue', markersize=2,  label='MKI2D')
plt.plot(beam_intb2, normDb2, 'o-', color='red', markersize=2,  label='MKI8D')
ax=plt.gca()
plt.xticks(fontsize=12.5)
plt.yticks(fontsize=13)
ax.yaxis.grid(linestyle='--') # plot horizontal lines
ax.xaxis.label.set_size(13.5)
ax.yaxis.label.set_size(13.5)
ax.set_xlim(0, xupperlim)
ax.set_ylabel(r'Normalized pressure (mbar/p)')
ax.semilogy()
ax.set_ylim(10 ** -25, 1*10 ** -21)
ax.set_xlabel(r'Beam Integral (C)')
plt.legend(prop={'size':11.5})
plt.show()

if PlotVsTime == "Y":
    # Beam intensity
    print("Plot: Beam Intensity vs. Time")
    plt.figure(figsize=(18,6))
    plt.suptitle(titletextb1, fontsize=11,y=0.98)
    plt.title(titletextb2, fontsize=11, y=1.03)
    #plt.plot(beam_elapb1, normDb1, 'o-', color='blue', markersize=2,  label='MKI2D')
    plt.plot(aligned_timeb1, intensityb1, 'o-', color='blue', markersize=2,  label='Beam intensity B1')
    plt.plot(aligned_timeb2, intensityb2, 'o-', color='red', markersize=2,  label='Beam intensity B2')
    #plt.plot(beam_elapb2, normDb2, 'o-', color='red', markersize=2,  label='MKI8D')
    ax=plt.gca()
    plt.xticks(fontsize=12.5)
    plt.yticks(fontsize=13)
    ax.xaxis.label.set_size(13.5)
    ax.yaxis.label.set_size(13.5)
    #ax.set_xlim(0, xupperlim)
    ax.set_ylabel(r'Beam intensity (p)')
    #ax.semilogy()
    ax.set_ylim(0, 3.5*10 ** 14)
    ax1.set_xlabel(r'Date & (UTC) time')
    pytimber.set_xaxis_date(bins=7)
    plt.legend(prop={'size':11.5})
    plt.show()


if PlotBothMagD_Interconnects == "Y":
    print("Plot: MKI2D+Interconnects & MKI8D+Interconnects")
    plt.figure(figsize=(18,6))
    plt.suptitle(titletextb1, fontsize=11,y=0.98)
    plt.title(titletextb2, fontsize=11, y=1.03)
    plt.plot(beam_intb1, normDb1, 'o-', color='blue', markersize=2,  label='MKI2D')
    plt.plot(beam_intb1, normDCb1, 'o-', color='green', markersize=2,  label='Interconnect MKI2D-MKI2C')
    plt.plot(beam_intb1, normQ5Db1, 'o-', color='purple', markersize=2,  label='Interconnect Q5-MKI2D')
    plt.plot(beam_intb2, normDb2, 'o-', color='red', markersize=2,  label='MKI8D')
    plt.plot(beam_intb2, normDCb2, 'o-', color='black', markersize=2,  label='Interconnect MKI8D-MKI8C')
    plt.plot(beam_intb2, normQ5Db2, 'o-', color='orange', markersize=2,  label='Interconnect Q5-MKI8D')
    ax=plt.gca()
    plt.xticks(fontsize=12.5)
    plt.yticks(fontsize=13)
    ax.xaxis.label.set_size(13.5)
    ax.yaxis.label.set_size(13.5)
    ax.set_xlim(0, xupperlim)
    ax.set_ylabel(r'Normalized pressure (mbar/p)')
    ax.semilogy()
    ax.set_ylim(10 ** -25, 1*10 ** -20)
    ax.set_xlabel(r'Beam Integral (C)')
    plt.legend(prop={'size':11.5})
    plt.show()


if PlotBothInterconnects == "Y":
    print("Plot 4")
    plt.figure(figsize=(18,6))
    plt.suptitle(titletextb1, fontsize=11,y=0.98)
    plt.title(titletextb2, fontsize=11, y=1.03)
    #plt.plot(beam_elapb1, normDb1, 'o-', color='blue', markersize=2,  label='MKI2D')
    plt.plot(beam_intb1, normDCb1, 'o-', color='green', markersize=2,  label='Interconnect MKI2D-MKI2C')
    plt.plot(beam_intb1, normQ5Db1, 'o-', color='purple', markersize=2,  label='Interconnect Q5-MKI2D')
    #plt.plot(beam_elapb2, normDb2, 'o-', color='red', markersize=2,  label='MKI8D')
    plt.plot(beam_intb2, normDCb2, 'o-', color='black', markersize=2,  label='Interconnect MKI8D-MKI8C')
    plt.plot(beam_intb2, normQ5Db2, 'o-', color='orange', markersize=2,  label='Interconnect Q5-MKI8D')
    ax=plt.gca()
    plt.xticks(fontsize=12.5)
    plt.yticks(fontsize=13)
    ax.xaxis.label.set_size(13.5)
    ax.yaxis.label.set_size(13.5)
    ax.set_xlim(0, xupperlim)
    ax.set_ylabel(r'Normalized pressure (mbar/p)')
    ax.semilogy()
    ax.set_ylim(5 * 10 ** -25, 2*10 ** -21)
    ax.set_xlabel(r'Beam Integral (C)')
    plt.legend(prop={'size':11.5})
    plt.show()

print("Plot 4a: Interconnect C-D norm pressure versus Beam Integral")
plt.figure(figsize=(18,6))
plt.suptitle(titletextb1, fontsize=11,y=0.98)
plt.title(titletextb2, fontsize=11, y=1.03)
#plt.plot(beam_elapb1, normDb1, 'o-', color='blue', markersize=2,  label='MKI2D')
plt.plot(beam_intb1, normDCb1, 'o-', color='green', markersize=2,  label='Interconnect MKI2D-MKI2C')
#plt.plot(beam_elapb1, normQ5Db1, 'o-', color='purple', markersize=2,  label='Interconnect Q5-MKI2D')
#plt.plot(beam_elapb2, normDb2, 'o-', color='red', markersize=2,  label='MKI8D')
plt.plot(beam_intb2, normDCb2, 'o-', color='black', markersize=2,  label='Interconnect MKI8D-MKI8C')
#plt.plot(beam_elapb2, normQ5Db2, 'o-', color='orange', markersize=2,  label='Interconnect MKI8D-Q5')
ax=plt.gca()
plt.xticks(fontsize=12.5)
plt.yticks(fontsize=13)
ax.yaxis.grid(linestyle='--') # plot horizontal lines
ax.xaxis.label.set_size(13.5)
ax.yaxis.label.set_size(13.5)
ax.set_xlim(0, xupperlim)
ax.set_ylabel(r'Normalized pressure (mbar/p)')
ax.semilogy()
ax.set_ylim(5 * 10 ** -25, 2*10 ** -21)
ax.set_xlabel(r'Beam Integral (C)')
plt.legend(prop={'size':11.5})
plt.show()

print("Plot 4b: Interconnect Q5-D norm pressure versus Beam Integral")
plt.figure(figsize=(18,6))
plt.suptitle(titletextb1, fontsize=11,y=0.98)
plt.title(titletextb2, fontsize=11, y=1.03)
#plt.plot(beam_elapb1, normDb1, 'o-', color='blue', markersize=2,  label='MKI2D')
#plt.plot(beam_elapb1, normDCb1, 'o-', color='green', markersize=2,  label='Interconnect MKI2D-MKI2C')
plt.plot(beam_intb1, normQ5Db1, 'o-', color='purple', markersize=2,  label='Interconnect Q5-MKI2D')
#plt.plot(beam_elapb2, normDb2, 'o-', color='red', markersize=2,  label='MKI8D')
#plt.plot(beam_elapb2, normDCb2, 'o-', color='black', markersize=2,  label='Interconnect MKI8D-MKI8C')
plt.plot(beam_intb2, normQ5Db2, 'o-', color='orange', markersize=2,  label='Interconnect Q5-MKI8D')
ax=plt.gca()
plt.xticks(fontsize=12.5)
plt.yticks(fontsize=13)
ax.yaxis.grid(linestyle='--') # plot horizontal lines
ax.xaxis.label.set_size(13.5)
ax.yaxis.label.set_size(13.5)
ax.set_xlim(0, xupperlim)
ax.set_ylabel(r'Normalized pressure (mbar/p)')
ax.semilogy()
ax.set_ylim(5 * 10 ** -25, 2*10 ** -21)
ax.set_xlabel(r'Beam Integral (C)')
plt.legend(prop={'size':11.5})
plt.show()

if PlotVsTime == "Y":
    ##PLOT 3 B1 - MKI2 Pressure on various points and beam intensity 
    print("Plot 5")
    fig, ax1 = plt.subplots(figsize=(18,6))
    fig.suptitle(titletextb1)
    ax1.plot(aligned_timeb1, pressureDb1, 'o-', color='red', markersize=2, label='MKI2D')
    ax1.plot(aligned_timeb1, pressureDCb1, 'o-', color='magenta', markersize=2, label='Interconnect MKI2D-MKI2C')
    ax1.plot(aligned_timeb1, pressureQ5Db1, 'o-', color='blue', markersize=2, label='Interconnect Q5-MKI2D')
    ax1.set_ylabel(r'Pressure (mbar)')
    ax1.set_ylim(0, 1*10 ** -8)
    #ax1.plt.xticks(fontsize=12.5)
    #ax1.plt.yticks(fontsize=13)
    ax1.xaxis.label.set_size(13.5)
    ax1.yaxis.label.set_size(13.5)
    #ax1.set_ylim(10 ** -25, 2*10 ** -20)
    ax1.set_xlabel(r'Date & (UTC) time')
    pytimber.set_xaxis_date(bins=7)
    plt.legend(loc=2, prop={'size':11.5})
    
    ax2 = ax1.twinx()
    ax2.plot(aligned_timeb1, intensityb1, 'o-', color='green', markersize=2, label='Beam intensity B1')
    ax2.set_ylabel(r'Beam intensity (p)')
    #ax2.yaxis.label.set_size(13.5)
    ax2.tick_params(axis='y', colors='green')
    ax2.yaxis.label.set_color('green')
    ax2.set_ylim(0, 3.5*10 ** 14)
    plt.legend(prop={'size':11.5})
    plt.show()


if PlotVsTime == "Y":
    ##PLOT 4 B2 - MKI8 Pressure on various points and beam intensity 
    print("Plot 6")
    fig, ax1 = plt.subplots(figsize=(18,6))
    fig.suptitle(titletextb2)
    ax1.plot(aligned_timeb2, pressureDb2, 'o-', color='red', markersize=2, label='MKI8D')
    ax1.plot(aligned_timeb2, pressureDCb2, 'o-', color='magenta', markersize=2, label='Interconnect MKI8C-MKI8D')
    ax1.plot(aligned_timeb2, pressureQ5Db2, 'o-', color='blue', markersize=2, label='Interconnect MKI8D-Q5')
    ax1.set_ylabel(r'Pressure (mbar)')
    ax1.set_ylim(0, 1*10 ** -8)
    #ax1.set_ylim(10 ** -25, 2*10 ** -20)
    ax1.set_xlabel(r'Date & (UTC) time')
    pytimber.set_xaxis_date(bins=7)
    plt.legend(loc=2, prop={'size':11.5})
    
    ax2 = ax1.twinx()
    ax2.plot(aligned_timeb2, intensityb2, 'o-', color='green', markersize=2, label='Beam intensity B2')
    ax2.set_ylabel(r'Beam intensity (p)')
    ax2.tick_params(axis='y', colors='green')
    ax2.yaxis.label.set_color('green')
    ax2.set_ylim(0, 3.5*10 ** 14)
    plt.legend()
    plt.show()


#Plotting time
plotting_time = time.time()-start_time
print("Execution time: plotting %0.3f seconds." % plotting_time)
