from xrayutilities.io.rigaku_ras import RASFile
import matplotlib.pyplot as plt
from pathlib import Path

# TODO Phi have the greek letter (degree)

# Folder that contains the .ras files
DATADIR = '/home/martin/Documents/Lea_DRX/'

# Folder to store plots as .svg
RESULTDIR = '/home/martin/Documents/Lea_DRX/Plots'

# load custom matplotlib plotting style     
plt.style.use('plotstyle.mplstyle')

# 
# theta: u'\u03B8'
# chi: u'\u03C7'  
# omega: u'\u03A9'

ANGLES = {
    'Phi': u'\u03C6 (\u00b0)',
    'Omega': u'\u03C9 (\u00b0)',
    'TwoThetaOmega': u'2\u03B8\u03C9 (\u00b0)',
    'TwoThetaTheta': u'2\u03B8 (\u00b0)',
    'TwoThetaChiPhi': u'2\u03B8\u03C7\u03C6 (\u00b0)',
    'TwoTheta': u'2\u03B8 (\u00b0)',
    'X': 'X',
    'Y': 'Y',
    'Z': 'Z',
}

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

    # result file 
    resultfile = Path(RESULTDIR).joinpath(path.with_suffix('.svg').name)

    if path.match('*100*'):
        col = '#B83A00'
    elif path.match('*110*'):
        col = '#11801E'
    elif path.match('*111*'):
        col = '#0001A4'
    else:
        col = '#000000'
        
    # do the plotting
    f = plt.figure()
    plt.plot(file.scan.data[axis], intensities, color=col)
    plt.xlabel(ANGLES[axis])
    plt.ylabel('Intensity (counts)')
    plt.yscale('log') # use log scale for the Y axis
    plt.title(path.name)
    plt.savefig(resultfile)
    plt.close()
