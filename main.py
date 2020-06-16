import matplotlib.pyplot as plt
import csv
import glob


def retrieving_signal(path):
    with open(path, "r") as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        data = [row for row in reader]
    
    
    signal = []
    for d in data:
        signal+= [float(c) for c in d]
    return signal[50:150]


def so_chan(signal, initial_max=2, filter_parameter=10):
	"""
	The peaks detection method.
	:signal : An array of ECG values
	:initial_max: 
	"""
    print('BEGINING THE INITIALISATION ...')
    peaks_index = []
    print('Initial maximum = ' + str(initial_max))
    slope_threshold = 0.5 * initial_max
    print('Slope threshold = ' + str(slope_threshold))
    print("Calculating the slope ...")
    slope = []
    for i in range(len(signal) - 5):
        slope.append(-2*signal[i] - signal[i+1] + signal[i+3] + 2*signal[i+4])
    print('Slope have been successfully calculated !')
    print('END OF THE INITIALISATION !\n###################\n')
    print('BEGINNING THE RESEARCH OF PEAKS ...')
    flag = False
    for cpt in range(len(slope)):
        if slope[cpt] > slope_threshold:  # The slope > threshold
            if flag:  # We test if slope[cpt-1] > threshold
                i = cpt
                while i < len(slope) and slope[i] > 0:  # Looking for the max
                    i += 1
                if i != len(slope):
                    print('We have found a new peak at : ' + str(i+2))
                    peaks_index.append(i+2)
                    initial_max = (((signal[i+2] - signal[cpt+2]) - initial_max) / filter_parameter) + initial_max
                    print('Updating initial_max to : ' + str(initial_max))
                    slope_threshold = 0.5 * initial_max
                    print('Updating slope_threshold : ' + str(slope_threshold))
                    flag = False

            else:  # It's the first time slope > threshold
                print('The slope have passed the threshold once !')
                flag = True
        else:
            if flag:  # the slope was > threshold but the next one wasn't
                print('It happened just once ...')
                flag = False
    print('END OF THE SEARCH')
    return peaks_index

def show_peaks(signal):
	"""
	Show the R-peaks on an ECG signal.
	signal : An array of ECG values
	"""
    peaks_index = so_chan(signal)
    peaks = []
    for index in peaks_index:
        peaks.append(signal[index])
    plt.plot(peaks_index, peaks, 'x')
    plt.plot(signal)
    plt.show()

if __name__ == '__main__':
    folder = glob.glob('./data-set/*.csv')
    for path in folder:
        signal = retrieving_signal(path)
        show_peaks(signal)
