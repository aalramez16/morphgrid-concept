it's pretty basic but at the top there's 4 inputs that are arrays. Once fully decoded a sound sample should be an array somewhere between -1 and 1. If you run it'll print what 2 iterations of generating a morph table looks like. The arrays at the corners are the inputs. Every other array is a morph in the direction from its parent array to the next. The array in the center is an average of all 4 corners.

You can change how many iterations are printed by changing the number (currently set at 2) in ecursive_pop_v(x,2) and ecursive_pop_h(x,2).

The inputs are ideally to be replaced by audio samples using a cpp decoding library once one is found. The morph process is performed by averaging sample energies to create new intermediate waveforms.

An alternative input rather than samples could be FFT data of frequency distributions. In this instance, there would need to be a function that decomposed an input into its spectral data, and recomposed it afterwards. This may be more costly.
