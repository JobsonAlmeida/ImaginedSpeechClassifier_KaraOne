import MDS_SCRIPTS as mds
import matplotlib.pyplot as plt

subject_1 = mds.Dataset("MM05")

PATH_TO_DATA = "C:\\Users\\jobso\\PastaGeral\\MestradoUnicamp\\Kara Dataset"

subject_1.load_data(PATH_TO_DATA, raw=True, filtered=False)
print(subject_1.eeg_data.ch_names)


data, times = subject_1.eeg_data.get_data(picks='Trigger', return_times=True)

plt.plot(times, data[0])
plt.title('Trigger')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (V)")
plt.show()


print(subject_1.name)
