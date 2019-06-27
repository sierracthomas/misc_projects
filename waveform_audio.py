!pip install pycbc
!pip install lalsuite

# import utilities
import pylab
from pycbc import waveform
import numpy as np
import scipy


for phase_order in [2]:
    # define test masses, delta_t, and f_lower
    # play with the mass1 and mass2 for different sounds!
    hp, hc = waveform.get_td_waveform(approximant='SEOBNRv2',
                                 mass1=15, mass2=10,
                                 phase_order=phase_order,
                                 delta_t=1.0/4096,
                                 f_lower=30)
    # optimize numbers in arrays
    hp, hc = hp.trim_zeros(), hc.trim_zeros()
    amp = np.array(waveform.utils.amplitude_from_polarizations(hp, hc))
    freq = np.array(waveform.utils.frequency_from_polarizations(hp, hc))
    #normalize hp arrays to get values in [-1,1]
    normalized_hp = np.array(hp)/np.max(np.array(hp))
    #plot waveform
    pylab.clf()
    pylab.plot(hp.sample_times, normalized_hp)

pylab.xlim(-0.1,0.025)
pylab.show()

#write .wav file
scipy.io.wavfile.write("test.wav", 16384, normalized_hp)
