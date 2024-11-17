# A Deep Learning Approach to Understanding Human Cognition Through iEEG-Video Analysis


**Abstract** Intracranial Electroencephalography (iEEG) provides a high-resolution, non-invasive method for directly recording neural activity from the human brain. This technique offers a unique opportunity to study complex cognitive processes with unprecedented temporal and spatial precision. In this study, we leverage the power of deep learning to model and interpret iEEG data, aiming to gain insights into the underlying neural mechanisms of human cognition.
By applying advanced deep learning techniques to iEEG data, we seek to develop accurate models that can decode cognitive states and predict behavior. Furthermore, we aim to utilize interpretability methods to delve into the inner workings of these models, shedding light on the neural representations learned by the network. This approach may ultimately contribute to a deeper understanding of the relationship between neural activity and cognitive function.

**Dataset** The iEEG dataset used here was collected by exposing the subjects to a short audio-visual film, while simultaneously tracking their brain activity through electrodes inserted into certain selected regions of thier brain.  The final dataset would be an amalgamation of the video frames and the iEEG channel data, where each frame would have a corresponding window of iEEG channel waves.

**Methodology** Here is a rough pipeline for this study:

- <ins>Pre-Processing</ins>. The iEEG data, although already preprocessed, must be further processed before using as an input to a model. The number of channels between each subjects differ, hence only the channels which are common among all the subjects must be included. The temporal consistency must also be maintained between each subject's iEEG data (and to be matched with that of the video frames). The window size for the final iEEG data must correspond to one video frame.
- <ins>Modelling iEEG data of a single person</ins>. A toy model must be selected to model the data of a single person. Since the data consists of multiple continous waves, an appropriate model must be selected and the loss must be driven to near zero (overfitted). The overfitting of the model may seem like a malpractice at first, but is indeed a good first step: it proves that the model architecture can indeed learn the underlying distribution, and all that is left is to regularize it.
- <ins>Extending the toy model to include video frame</ins>. This would logically be the next step. The video and iEEG data must be first projected into a common latent space, where the model would learn a joint distribution of the iEEG data and the video data, which can help us extract semantic meaning from the iEEG data as well. (If each video frame can be accompanied with a text describing it, than a well-trained image-to-text model can be used to extend to the iEEG data, and can be used to make a iEEG-to-text model. *Note: this is speculative*).
- <ins>Scaling up</ins> the toy model. This would include taking into account the all the iEEG data of the subjects provided. Model stability must be maintained while training, and this time the model should not be allowed to overtrain, and generalization must be the end goal.
- <ins>Interpretation</ins>. Given that the scaled up final model has learned to generalize well with the given dataset, a connection could be made between it's inner working and how the brain *might* work. The inner workings can be explored through the process of mechanistic interpretability, which might explain the *why* of the inner workings of the model.
- <ins>Connection to cognitive science</ins>. The final interpretations can be compared with other well known results to either validate, disprove or extend upon known theories.




