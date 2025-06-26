# MSAF-CycleGAN  
Multi-scale Attention & Frequency-constrained CycleGAN for Seismic-Data Denoising
--------------------------------------------------------------------------------

This repo contains the **official PyTorch implementation** of the paper  

> **“Multi-scale Attention and Frequency-constrained Generative Adversarial Network for Seismic Data Denoising.”*  

The model introduces three key innovations on top of CycleGAN for single-trace and section-level seismic-image denoising:

1. **Spatial-Attention Blocks** in every ResNet block of the generator – the network learns to focus on structurally important reflectors and suppress random noise.  
2. **Multi-scale Discriminators** – several PatchGANs operating at successively down-sampled resolutions yield better perceptual realism across scales.  
3. **Frequency-domain Loss** – an L<sub>1</sub> loss computed on FFT amplitude spectra enforces consistency in the wavenumber domain, preserving geologic structures while removing incoherent noise.


| Path / File                                | Description |
|--------------------------------------------|-------------|
| **checkpoints/**                           | Saved model weights produced during training (organized by experiment name). |
| **data/**                                  | Data loading & preprocessing modules.<br>• `base_dataset.py` – abstract base class.<br>• `unaligned_dataset.py` – non-paired loader for CycleGAN.<br>• `single_dataset.py` – single-domain loader for inference. |
| **datasets/**                              | Store the dataset. |
| **models/**                                | Network and loss definitions.<br>• `cycle_gan_model.py` – main model with attention & spectral loss.<br>• `networks.py` – generators, discriminators, `SpatialAttention`, `MultiScaleDiscriminator`, etc. |
| **options/**                               | Command-line option parsers.<br>• `train_options.py`, `test_options.py`, `base_options.py`. |
| **results/**                               | Outputs from `test.py` (images & generated HTML). |
| **util/**                                  | Helper utilities (image buffer, HTML visualizer, misc tools). |
| **train.py**                               | Main training entry point. |
| **test.py**                                | Main inference entry point. |
| **CycleGAN.ipynb**                         | Interactive notebook with ablation studies / demos. |
| **environment.yml** / **requirements.txt** | Conda / pip dependency lists. |
| **LICENSE**                                | Combined BSD & MIT license inherited from original CycleGAN . |
| **README.md**                              | Project documentation (this file). |
| **.replit**                                | Config for running on Replit . |
| **example_test**                           | The experiments on the PseudoClean dataset in the paper can be obtained by running. |
