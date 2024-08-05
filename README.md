# EEg-FMRI
our research proposes a method that leverages multimodal neural data integrated with a visual semantic space to create a cognitive basis model  mapping the sequence of interactions and transformations using EEG–fMRI data  .
OUR ROADMAP:
### 1. Data Acquisition and Preprocessing
1. **Download Dataset**: Obtain EEG and fMRI data from the specified dataset: [NITRC INDI Dataset](https://fcon_1000.projects.nitrc.org/indi/retro/nat_view.html).
2. **Preprocess Data**:
   - **EEG Data**:
     - Perform standard preprocessing steps (e.g., filtering, artifact removal).
     - Localize EEG sources to obtain spatial activation maps.
 - **fMRI Data**:
     - Preprocess fMRI images (e.g., slice timing correction, motion correction, normalization, smoothing).
3. **Correlate Data**:
   - Correlate EEG source localization maps with EEG channels.(this might seem redundant with the fmri but bold data only corresponds to high levels of activity sometimes  )
   - Correlate EEG data with corresponding fMRI voxel data.
4. **Train First VAE (Unsupervised)**:
   - Input: Preprocessed EEG and fMRI data.(this is to correlat temporal and spatial representations )
   - Task: Reconstruct its input.
5. **Train Second VAE**:
   - Input: Preprocessed EEG and fMRI data.
   - Task: Reconstruct the stimulus associated with the data.(ssl )
6. **Masking**:
   - Mask each timestamp of EEG data post-training.
   - Mask each voxel of fMRI data post-training.
7. **Feature Analysis**:
   - Look for features in the data that change probabilities post-masking in both VAEs.
   - Annotate the masked timestamps/voxels with the features that show significant probability changes in both VAEs.(in vae 1 it would be the voxels that changed probability due to the eeg 
     masking and eeg timestamps that changed probabilities for voxel ).
8. **Post-Processing**:
   - Convert the identified features and their annotations into a structured format.
   - Organize the results into a comprehensive report or dataset for further analysis or interpretation.

