# Basic Pipeline Context

**Status:** Initial code-grounded inventory; not clinical or analysis
recommendations.

**Scope:** Pipeline modules that the current Pipeline Manager displays when
“Show Advanced Modules” is unchecked. This is a UI classification, not a claim
that the operations are universally appropriate, risk-free, or beginner-level.

## How the classification works

The Pipeline Manager discovers classes derived from `cedalion_module` and reads
their `advanced_module` attribute. When the checkbox is unchecked, it displays
modules for which that attribute is false. The base pipeline module defaults to
advanced, so individual modules must explicitly set `advanced_module = False` to
appear in the basic list.

The current list contains preprocessing, filtering, motion correction, and
analysis modules. In particular, GLM, connectivity, and mixed-effects analysis
are in the same visible list as optical-density conversion and resampling.
An AI assistant must therefore not treat “basic” as an independent safety or
competence label.

`input_data` is an important exception: its default is `advanced_module = True`,
although the built-in default pipelines use it. It is hidden from the available
module list when advanced modules are hidden, but a pipeline can still include
it.

## Modules shown in the basic list

The names below are the user-facing module names in the current source. Inputs
and outputs refer to recording time-series names unless noted otherwise.
“Last” means the module's configured input/output is the most recently stored
time series.

| Pipeline Manager name | Python class | Purpose and important defaults |
| --- | --- | --- |
| Resample | `preproccessing.resample` | Resamples the selected time series; default target rate is 4 Hz. The module notes that a rate well below the original rate low-pass filters the signal. |
| Calculate Optical Density | `preproccessing.intensity_opticaldensity` | Converts raw intensity `amp` to optical density `od`. |
| Calculate Modified Beer-Lambert | `preproccessing.mbll` | Converts `od` to concentration `conc` using the modified Beer-Lambert law. Defaults: Prahl spectrum and DPF `[6, 6]`, ordered to match the probe wavelengths. |
| Trim Pre/Post Baseline | `preproccessing.TrimBaseline` | Trims time-series data around the stimulus interval. Defaults: keep up to 30 seconds before the first event and after the last event; do not reset time; trim auxiliary time series. |
| Band-Pass Filter | `filters.bandpass_filter` | Filters the selected time series. Defaults: 0.016–1 Hz, fourth-order Butterworth. The documented guidance cautions that the lower cutoff should remain below the slowest stimulus frequency. |
| PCA Filter | `filters.pca_filter` | Applies a PCA-based filter. Defaults: `ncomp=0.8` and separate processing by data type. The option describes values from 0 to 1 as the fraction of variance removed; values at least 1 select a component count. |
| TDDR | `motion_correction.TDDR` | Applies Temporal Derivative Distribution Repair motion correction. Defaults: treat positive and negative shifts separately and apply PCA before TDDR. |
| GLM Model | `glm.GLM` | Fits a first-level General Linear Model and stores statistics. Default noise model is `ar_irls`; defaults also include autoregressive order 30 and a configured temporal basis function. This is an analysis step, not just signal preprocessing. |
| Resting State Connectivity | `connectivity.resting_state_connectivity` | Computes resting-state connectivity and stores a connectivity result. Defaults include AR order 18, robust estimation, and short-separation correction. |
| Hyperscanning Connectivity | `connectivity.hyperscanning` | Computes a connectivity result for hyperscanning data. This is an analysis step; its paired-recording assumptions should be reviewed before an assistant recommends it. |
| Mixed Effects Model | `mixedeffects.MixedEffects` | Fits a group-level model from statistics. Defaults include fixed formula `Beta ~ 0 + Condition`, random formula `~Condition`, robust fitting, covariance weighting, and mean-centering numeric demographics. This is an analysis step. |

The class identifiers above are Python module/class names; the displayed labels
come from each class's `name` property. The class options and code are the source
of truth for exact behavior.

## Built-in pipeline context

The predefined pipelines show some intended compositions:

- **Basic preprocessing:** input data → intensity-to-optical-density conversion
  → modified Beer-Lambert conversion → resampling to 4 Hz.
- **Pediatric preprocessing:** the same sequence with TDDR motion correction
  before resampling.
- **First-level analysis:** the basic preprocessing sequence followed by GLM
  using `ar_irls`.

These are examples of configured pipelines, not universal prescriptions.
Researchers must choose settings and processing steps appropriate to their
acquisition and study design.

## Implications for an AI helper

1. The `advanced_module` flag is useful metadata for organizing module
   documentation, but is not sufficient by itself to define allowed AI tools.
2. Pipeline modules are executable processing stages, not necessarily
   read-only or event-only actions. An assistant should not run them just
   because they are marked basic.
3. Tool definitions should state the module's required inputs, output,
   parameters and defaults, side effects, and relevant preconditions.
4. Analysis modules should be described separately from preprocessing and
   filters, even though they share the same Pipeline Manager visibility flag.
5. Where exact parameter behavior is unclear, the assistant should ask the
   researcher or provide the default and request confirmation instead of
   inventing a recommendation.

## Source map

This inventory was checked against the current local pyNIRS_toolbox working
copy on 2026-10-08. The source tree is a separate project and is not vendored
here. The local working copy contains uncommitted changes, so re-check module
flags, names, and options against the intended upstream revision before treating
this document as a release-specific reference.

Relevant source files in pyNIRS_toolbox:

- `pyBrainAnalyzIR/vis/pipeline_manager.py` — discovers modules and filters the
  list by `advanced_module`.
- `pyBrainAnalyzIR/pipelines/pipeline.py` — base pipeline module defaults.
- `pyBrainAnalyzIR/pipelines/default_pipelines.py` — built-in pipeline
  compositions.
- `pyBrainAnalyzIR/pipelines/modules/preproccessing.py` — conversion,
  resampling, and baseline trimming.
- `pyBrainAnalyzIR/pipelines/modules/filters.py` — signal filters.
- `pyBrainAnalyzIR/pipelines/modules/motion_correction.py` — motion correction.
- `pyBrainAnalyzIR/pipelines/modules/glm.py` — first-level GLM.
- `pyBrainAnalyzIR/pipelines/modules/connectivity.py` — connectivity analysis.
- `pyBrainAnalyzIR/pipelines/modules/mixedeffects.py` — group-level model.
