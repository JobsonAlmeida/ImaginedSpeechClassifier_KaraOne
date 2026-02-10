import MDS_SCRIPTS as mds
import matplotlib.pyplot as plt
import copy
import numpy as np
import glob
import scipy.io as spio



subject = mds.Dataset("MM05")

PATH_TO_DATA = "C:\\Users\\jobso\\PastaGeral\\MestradoUnicamp\\Kara Dataset"

subject.load_data(PATH_TO_DATA, raw=True, filtered=False)


events = copy.deepcopy(subject.epoch_inds['thinking_inds'])


for f in glob.glob("epoch_inds.mat"):
    subject.epoch_inds = spio.loadmat(f, variable_names=('clearing_inds', 'thinking_inds'))

print('subject.epoch_inds')
print("dim: ",subject.epoch_inds.ndim)
print("shape: ", subject.epoch_inds.shape)
print("type: ", type(subject.epoch_inds))
print("dtype: ", subject.epoch_inds.dtype)
print(subject.epoch_inds)




print('raw events')
print("dim: ",events.ndim)
print("shape: ", events.shape)
print("type: ", type(events))
print("dtype: ", events.dtype)
print(events)
events = np.reshape(events, (events.shape[1], 1))

print('reshaped events')

print("dim: ",events.ndim)
print("shape: ", events.shape)
print("type: ", type(events))
print("dtype: ", events.dtype)
print(events)


print( "------ events[0] ----------")
print("dim: ",events[0].ndim)
print("shape: ", events[0].shape)
print("type: ", type(events[0]))
print("dtype: ", events[0].dtype)
print(events[0])



print( "------events[0][0]-----------")
print("dim: ",events[0][0].ndim)
print("shape: ", events[0][0].shape)
print("type: ", type(events[0][0]))
print("dtype: ", events[0][0].dtype)
print(events[0][0])


print( "------events[0][0][0]-----------")
print("dim: ",events[0][0][0].ndim)
print("shape: ", events[0][0][0].shape)
print("type: ", type(events[0][0][0]))
print("dtype: ", events[0][0][0].dtype)
print(events[0][0][0])

print( "------events[0][0][0][0]-----------")
print("dim: ",events[0][0][0][0].ndim)
print("shape: ", events[0][0][0][0].shape)
print("type: ", type(events[0][0][0][0]))
print("dtype: ", events[0][0][0][0].dtype)
print(events[0][0][0][0])

print( "------events[0][0][0][1]-----------")
print("dim: ",events[0][0][0][1].ndim)
print("shape: ", events[0][0][0][1].shape)
print("type: ", type(events[0][0][0][1]))
print("dtype: ", events[0][0][0][1].dtype)
print(events[0][0][0][1])





# print(subject_1.eeg_data.ch_names)


# data, times = subject_1.eeg_data.get_data(picks='Trigger', return_times=True)

# plt.plot(times, data[0])
# plt.title('Trigger')
# plt.xlabel("Time (s)")
# plt.ylabel("Amplitude (V)")
# plt.show()


# print(subject_1.name)
