import mne
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os


class EEG_read:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = mne.io.read_raw_eeglab(file_path, preload=True)
        self.stimulus = self.extract_stimulus_from_filename()

    def extract_stimulus_from_filename(self):
        filename = os.path.basename(self.file_path)
        start = filename.find('task-') + len('task-')
        end = filename.find('_eeg')
        return filename[start:end]

    def create_epochs(self, events, event_id, tmin=-0.2, tmax=0.5, baseline=(None, 0)):
        self.epochs = mne.Epochs(
            self.data, events, event_id, tmin, tmax, baseline=baseline, preload=True)
        return self.epochs

    def plot_data(self, start=None, stop=None):
        self.data.plot(start=start, duration=stop -
                       start if start and stop else None)

    def plot_epochs(self, epoch_idx=None):
        if self.epochs:
            self.epochs.plot(epoch_idx=epoch_idx)
        else:
            raise ValueError("No epochs found. Create epochs first.")


class Analyses:
    def __init__(self, eeg_data):
        self.eeg_data = eeg_data.data

    def plot_raw(self, tmin=0, tmax=None):
        """Plot the raw EEG data."""
        if isinstance(self.eeg_data, mne.io.Raw):
            if tmax is None:
                tmax = self.eeg_data.times[-1]
            self.eeg_data.plot(start=tmin, duration=tmax -
                               tmin, title=self.eeg_data.stimulus)
        else:
            print("EEG data is not in MNE Raw format. Unable to plot raw data.")

    def plot_psd(self, tmin=0, tmax=None):
        """Plot the power spectral density (PSD) of the EEG data."""
        if isinstance(self.eeg_data, mne.io.Raw):
            self.eeg_data.plot_psd(tmin=tmin, tmax=tmax,
                                title=self.eeg_data.stimulus)
        else:
            print("EEG data is not in MNE Raw format. Unable to plot PSD.")

    def plot_topomap(self, tmin=0, tmax=None):
        """Plot the topographical map for the EEG data."""
        if isinstance(self.eeg_data, mne.io.Raw):
            if tmax is None:
                tmax = self.eeg_data.times[-1]
            times = self.eeg_data.times[(self.eeg_data.times >= tmin) & (
                self.eeg_data.times <= tmax)]
            self.eeg_data.plot_topomap(
                times=times, title=self.eeg_data.stimulus)
        else:
            print("EEG data is not in MNE Raw format. Unable to plot topomap.")

    def calculate_correlation_matrix(self, tmin=0, tmax=None):
        """Calculate and return the correlation matrix for the EEG data."""
        if isinstance(self.eeg_data, mne.io.Raw):
            if tmax is None:
                tmax = self.eeg_data.times[-1]
            data = self.eeg_data.get_data(tmin=tmin, tmax=tmax)
            correlation_matrix = np.corrcoef(data)
            return correlation_matrix
        else:
            print(
                "EEG data is not in MNE Raw format. Unable to calculate correlation matrix.")
            return None

    def plot_correlation_matrix(self, correlation_matrix):
        """Plot the correlation matrix."""
        if correlation_matrix is not None:
            plt.figure(figsize=(10, 8))
            plt.imshow(correlation_matrix, cmap='hot', interpolation='nearest')
            plt.colorbar()
            plt.title(f'Correlation Matrix - {self.eeg_data.stimulus}')
            plt.show()
