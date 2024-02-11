from xrayutilities.io.rigaku_ras import RASFile
import matplotlib.pyplot as plt
from pathlib import Path

DATADIR = '/home/martin/Documents/Lea_DRX/'

# load custom matplotlib plotting style     
plt.style.use('plotstyle.mplstyle')

# loop over all .ras files in the current directory
for path in Path(DATADIR).rglob('*.ras'):

    # print progress
    print(path.name)
    
    # parse RAS file
    file = RASFile(str(path.resolve())) 
    
    # get scan axis 
    axis = file.scan.scan_axis # e.g. phi, omega, ...
    
    # compute intensity corrected by attenuation
    intensities = file.scan.data['int']*file.scan.data['att']

    # do the plotting
    f = plt.figure()
    plt.plot(file.scan.data[axis], intensities)
    plt.xlabel(axis)
    plt.ylabel('Intensity')
    plt.yscale('log') # use log scale for the Y axis
    plt.title(path.name)
    plt.savefig(path.with_suffix('.svg').name)
