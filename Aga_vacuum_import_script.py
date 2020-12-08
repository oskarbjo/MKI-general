import pytimber
from pytimber import pagestore
import time, calendar
#from numba import jit
#matplotlib notebook
ldb = pytimber.LoggingDB()

mydbPressureMDB = pagestore.PageStore('lhcPressure.db', './data/LHCpressure_data/')
#mydbPressure = pagestore.PageStore('mydataPressure.db', './../../SPS_Pressure_data')


#===============================================================================
t1 = "2012-07-01 00:00:00"
t2 = "2012-07-01 23:59:59"
#===============================================================================
#t1 = "2018-05-18 00:00:00"
#t2 = "2018-05-20 11:59:59"
# t1 = '2017-10-11 00:00:00' #(input("Start date? (ex.2017-07-25 10:15:00.000)\n"))
# t2 = '2017-10-11 06:00:00' #(input("End date? (ex.2017-07-25 10:15:00.000)\n"))

# subtract 0s to keep in UTC time.
# subtract 2 * 3600s to convert from Local time to UTC time
ts1 = calendar.timegm(time.strptime(t1,"%Y-%m-%d %H:%M:%S")) - 0 * 3600
ts2 = calendar.timegm(time.strptime(t2,"%Y-%m-%d %H:%M:%S")) - 0 * 3600

# Note: Prior to LS1 VGPB.176.5L2.B.PR & VGPB.176.5R8.R.PR did NOT exist, only .192
keys_beam1 = ['MKI.D5L2.B1:PRESSURE', 'VGPB.118.5L2.C.PR', 'MKI.B5L2.B1:PRESSURE', 'MKI.A5L2.B1:PRESSURE', 'VGPB.137.5L2.B.PR', 'VGPB.14.5L2.B.PR', 'VGPB.176.5L2.B.PR', 'VGPB.192.5L2.B.PR', 'VGPB.59.5L2.B.PR', 'VGPB.98.5L2.B.PR', 'LHC.BCTFR.A6R4.B1:BEAM_INTENSITY', 'MKI.A5L2.B1:PRESSURE_INT', 'MKI.B5L2.B1:PRESSURE_INT', 'MKI.C5L2.B1:PRESSURE_INT', 'MKI.D5L2.B1:PRESSURE_INT']
keys_beam2 = ['MKI.D5R8.B2:PRESSURE', 'MKI.C5R8.B2:PRESSURE', 'MKI.B5R8.B2:PRESSURE', 'MKI.A5R8.B2:PRESSURE', 'VGPB.138.5R8.R.PR', 'VGPB.14.5R8.R.PR', 'VGPB.176.5R8.R.PR', 'VGPB.192.5R8.R.PR', 'VGPB.59.5R8.R.PR', 'VGPB.98.5R8.R.PR', 'LHC.BCTFR.A6R4.B2:BEAM_INTENSITY', 'MKI.A5R8.B2:PRESSURE_INT', 'MKI.B5R8.B2:PRESSURE_INT', 'MKI.C5R8.B2:PRESSURE_INT', 'MKI.D5R8.B2:PRESSURE_INT']

# keys_beam1 = ['MKI.D5L2.B1:PRESSURE', 'VGPB.176.5L2.B.PR']
# keys_beam2 = ['MKI.D5R8.B2:PRESSURE', 'VGPB.176.5R8.R.PR']


#print('Start time =',start_time)
#@jit
def Store_data(keys):
    print('Start of getting aligned data')
    start_time = time.time()
    timber_data = ldb.getAligned(keys, ts1, ts2)
    print('End of getting aligned data')
    end_time = time.time()
    print('Time to extract and align data',end_time-start_time)
    print('Length of timber_data vector =',len(timber_data['timestamps']))
    for key in keys:
        mydbPressureMDB.store_variable(key, timber_data['timestamps'], timber_data[key]);

start_time = time.time()
print('Aligning and storing data from ',t1,' to ',t2)

Store_data(keys_beam1+keys_beam2)

storing_aligned_time = time.time()-start_time
print("Aligning and storing data: %0.3f seconds." %storing_aligned_time)
print('Finished storing local data for ',t1,' to ',t2)

