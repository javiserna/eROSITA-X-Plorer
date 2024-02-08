from astropy.io import fits
import matplotlib.pyplot as plt
data=fits.open('em01_080156_020_LightCurve_00002_c010.fits')
sec2day = 1.15741e-5
plt.plot(data[1].data.TIME*sec2day, (data[1].data.RATE)[:,0], label="0.2-0.6 KeV", marker='o', linestyle='--')
plt.plot(data[1].data.TIME*sec2day, (data[1].data.RATE)[:,1], label="0.6-2.3 KeV", marker='o', linestyle='--')
plt.plot(data[1].data.TIME*sec2day, (data[1].data.RATE)[:,2], label="2.3-5.0 KeV", marker='o', linestyle='--')
plt.legend()
plt.ylim(0,)
plt.title('AB_Dor (eRASS1)')
plt.xlabel('Time (days)')
plt.ylabel('Count rate (cts/sec)')
plt.savefig('eRASS1_AB_Dor.png', dpi=300)
plt.show()
