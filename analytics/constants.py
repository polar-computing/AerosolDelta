# Declare all Constants

# MERRA-2 Fields
MERRA2_CATAU_ATTR = {'BCSCATAU', 'OCSCATAU', 'DUSCATAU', 'SSSCATAU', 'SUSCATAU', 'TOTSCATAU'}
MERRA2_MASS_ATTR = {'BCSMASS', 'OCSMASS', 'DUSMASS', 'SSSMASS', 'SO4SMASS', 'SO2SMASS'}
MERRA2_ATTR = MERRA2_CATAU_ATTR | MERRA2_MASS_ATTR

# CALIOP Fields
CALIOP_ATTR = {'AOD_Mean_Dust', 'AOD_Mean_Polluted_Dust', 'AOD_Mean_Smoke', 'AOD_Mean'}

# Operations
OPERATIONS = {'min', 'max', 'median', 'mean', 'std'}

# Other Parameters
TIME = 'time'
REGION = 'region'
FIELD = 'field'
YEAR = 'year'
MONTH = 'month'