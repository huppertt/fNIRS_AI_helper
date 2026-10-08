# Basic fNIRS Modality Workflows

**Status:** Code- and example-grounded orientation; not a clinical or
study-specific processing recommendation.

**Scope:** Core pipeline modules whose current pyNIRS_toolbox classes set
`advanced_module = False`. The Pipeline Manager flag is a visibility category,
not evidence that a method is suitable for every dataset or that its defaults
are universally recommended. See [Basic Pipeline Context](basic-pipeline-context.md)
for the full visible-module inventory and current defaults.

## What the examples show

The Python examples and MATLAB demos describe a family of related processing
steps, not one mandatory sequence. They differ in module order, sampling rate,
and some model options. Treat these as worked examples, and choose settings
based on the acquisition, probe, stimulus design, and analysis question.

### Signal preprocessing and first-level task analysis

The Python default pipelines in `default_pipelines.py` include:

- **Basic preprocessing:** raw intensity (`amp`) -> optical density (`od`) ->
  concentration (`conc`) using the modified Beer-Lambert law -> resample to
  4 Hz.
- **Pediatric preprocessing:** the same conversions, then TDDR, then resample
  to 4 Hz.
- **First-level analysis:** the basic preprocessing sequence followed by a
  GLM using `ar_irls`.

The Python `02_PipelineCreation.ipynb` example demonstrates constructing a
chain of processing modules, inspecting options and help, setting options
across the chain, and running the result on a recording. It also demonstrates
event renaming/removal and TDDR; event-manipulation modules are outside this
guide's basic-modality scope, and TDDR's inclusion in the notebook is an
example rather than a universal prescription.

The MATLAB `demos/fnirs_analysis_demo.m` walks through a similar broad path:
remove stimulus-less files, rename conditions, resample, trim excess baseline,
convert intensity to optical density, convert optical density to hemoglobin,
then fit a first-level GLM. Its hand-built example uses a 2 Hz rate to reduce
demo runtime, and the MATLAB default single-subject pipeline shown in other
demos places resampling before the conversions. The Python defaults use 4 Hz
and place resampling after conversions. These differences are evidence that a
demo's values and order should not be copied as universal settings.

Python regression tests also exercise trimming around two known stimulus
windows, preserving stimulus onsets by default, shifting the time vector and
onsets when `resetTime` is enabled, retaining all samples when both baseline
limits are `None`, and warning when no events are present.

In the current Python implementation, the conversion modules produce named
time series: `intensity_opticaldensity` reads `amp` and writes `od`;
`mbll` reads `od` and writes `conc`. Resampling and filters default to operating
on the last time series. `GLM` defaults to input `conc` and writes first-level
`stats`. The MATLAB demo describes its GLM on hemoglobin data (`hb`) and notes
that it can also be run on optical density. These package conventions should
not be assumed to be identical.

### First-level GLM

The Python examples and end-to-end tests fit the GLM after preprocessing.
Tests exercise both OLS and AR-IRLS and check that simulated-data runs produce
statistics, finite p-values, and condition labels. The current Python default
is `ar_irls`; `test_analysis_pipeline.py` uses a deliberately reduced
autoregressive order for its small simulated case, while module defaults use a
higher order. Those test settings are chosen for test execution and are not
study recommendations.

The MATLAB first-level demo describes a canonical HRF as the default temporal
basis, illustrates trend regressors, and produces subject-level statistics
including coefficients and covariance information for downstream group
analysis. Python also offers multiple temporal basis presets. The FIR-like or
Gaussian-kernel/deconvolution examples require explicit design choices and
should not be presented as automatic defaults simply because the GLM module is
visible in the basic list.

For lecture-derived statistical and design guidance, see [Video-Lecture
Context](video-lecture-context.md); verify all settings against current Python
module help.

### Group analysis and demographics

The Python `08_GroupAnalysis.ipynb` example builds a `DataSet`, associates
demographics with its recordings, runs preprocessing and first-level GLMs over
the dataset, then runs `MixedEffects` to produce `groupstats`. It shows two
ways to attach demographic tables: by dataset row order or by matching a
variable. Matching by a stable subject identifier is preferable when row order
is not guaranteed; the example does not make row-order matching safe if the
orders differ.

The MATLAB analysis demo likewise adds demographics to subject statistics and
then runs a mixed-effects model. In Python, `MixedEffects` expects first-level
`stats` and demographics on a dataset and writes `groupstats`. Its current
default fixed-effects formula is `Beta ~ 0 + Condition`; the current default
random-effects formula is `~Condition`. The example tests also check that
nuisance regressors are excluded by default and that numeric demographics can
be included in a formula. Model formula, matching key, missing data, grouping,
and study design require researcher decisions.

### Connectivity

The Python `09_RestingStateConnectivity.ipynb` and
`12_fNIRS_Connectivity_Demo.ipynb` examples use simulated recordings with
known connectivity structure. They illustrate an important distinction:
ordinary correlation can report apparent connections when the signals share
slow hemodynamic or superficial physiology. The connectivity module's
short-separation correction is enabled by default when the recording has
short-separation channels. Tests compare this integrated correction with
running the explicit short-separation filter first, and test behavior when
short channels are absent.

Resting-state connectivity may also use stimulus events to divide the recording
into event and rest windows. In the current Python code this is opt-in:
`divide_events` defaults to false; the configured defaults for minimum event
duration and excluded transition time are 30 s and 10 s, respectively. Tests
verify the generated windows and contrasts such as `task - rest`; these values
are implementation defaults, not recommended thresholds for every experiment.

Hyperscanning is a separate basic-list module for connectivity between
recordings. The Python example and tests group recordings using a demographic
dyad/pair field; the tests also exercise event/rest windows and confirm that
outputs link geometries across recordings. It is not a single-recording
resting-state analysis. Before describing its use, verify subject pairing,
stimulus timing compatibility, recording alignment, and the meaning of the
grouping variable.

The MATLAB `demos/fnirs_connectivity_demo.m` and Python
`12_fNIRS_Connectivity_Demo.ipynb` compare correlation and AR-based
connectivity estimators on simulated and example data. They include ROC and
sensitivity/specificity demonstrations. These are validation/teaching
workflows, not evidence that a particular method will control error at the same
rate in every real dataset. MATLAB's demo labels itself a work in progress and
discusses limitations of its lagged/Granger-style analysis; lagged connectivity
is not part of this basic workflow guide.

## Basic-list modules and evidence coverage

| Basic-list module | Role in an analysis | What the reviewed examples/tests establish |
| --- | --- | --- |
| Resample | Changes the selected time series' sampling frequency. | End-to-end test checks the resulting rate; examples use multiple rates for different purposes. |
| Calculate Optical Density | Converts intensity `amp` to `od`. | End-to-end preprocessing and GLM tests use this conversion. |
| Calculate Modified Beer-Lambert | Converts `od` to `conc`. | End-to-end preprocessing and GLM tests use this conversion. |
| Trim Pre/Post Baseline | Trims samples before the first and after the last stimulus, with configurable limits. | Python regression tests check trimming, time reset, unlimited baselines, and the no-event warning; MATLAB analysis demo illustrates 30 s pre/post limits. |
| Band-Pass Filter | Filters the selected time series by configured frequency bounds. | The reviewed tests establish module/options plumbing; no reviewed basic-workflow integration test demonstrates a universal cutoff. |
| PCA Filter | Applies a PCA-based filter to the selected time series. | The reviewed tests establish module/options plumbing; no reviewed basic-workflow example establishes a general parameter choice. |
| TDDR | Motion-correction operation, with options for PCA and separate positive/negative shifts. | Appears in Python pipeline examples and a predefined pediatric pipeline; the reviewed end-to-end tests do not quantify its benefit across studies. |
| GLM Model | Fits a first-level model and writes `stats`. | Simulated-data tests exercise OLS/AR-IRLS and output structure; examples show task-evoked analysis. |
| Resting State Connectivity | Computes within-recording connectivity; can optionally divide event/rest windows and apply short-separation correction. | Simulated connectivity notebooks and tests exercise correction, event windows, contrasts, and output shape. |
| Hyperscanning Connectivity | Computes between-recording connectivity for grouped recordings. | Simulated examples and tests use dataset demographics to form dyads and check outputs. |
| Mixed Effects Model | Fits a group model from first-level statistics and demographics, writing `groupstats`. | Simulated dataset tests and group-analysis examples exercise the first-level-to-group workflow. |

The generic module tests check that pipeline modules expose documented options
and validate option values. Such tests do not by themselves show that an
analysis is scientifically appropriate or that each option has been
end-to-end-tested on real data.

## Scope exclusions and caution

- Python event rename/remove/keep operations are marked advanced in the current
  module source, even though examples use them during setup. They are not
  included as basic modalities here; see [Event Annotation Context](event-annotation-context.md).
- The standalone `Short Separation Filter` is marked advanced. Basic
  connectivity modules can apply short-separation correction internally.
- Resampling, filters, motion correction, trimming, GLM, and connectivity alter
  or add in-memory analysis data/results. Their visibility flag does not imply
  they modify the original raw file, nor does it guarantee that a particular
  output is scientifically appropriate.
- No single preprocessing order, sample rate, filter setting, GLM basis, or
  group formula is prescribed by this document.
- The Python tests mainly use synthetic data and small parameter choices for
  reliable test runs. MATLAB examples may download sample data when run; they
  were inspected, not executed for this documentation.

## Source map and provenance

Reviewed on 2026-10-08 against local working copies. The source projects are
separate from this repository and are not vendored here. Re-check against the
intended source revisions before treating implementation details as
release-specific.

Python examples:

- `pyNIRS_toolbox/pyNIRS_toolbox/examples/02_PipelineCreation.ipynb`
- `pyNIRS_toolbox/pyNIRS_toolbox/examples/08_GroupAnalysis.ipynb`
- `pyNIRS_toolbox/pyNIRS_toolbox/examples/09_RestingStateConnectivity.ipynb`
- `pyNIRS_toolbox/pyNIRS_toolbox/examples/12_fNIRS_Connectivity_Demo.ipynb`

Python tests and implementation:

- `pyNIRS_toolbox/pyNIRS_toolbox/tests/test_analysis_pipeline.py`
- `pyNIRS_toolbox/pyNIRS_toolbox/tests/test_pipeline_modules.py`
- `pyNIRS_toolbox/pyNIRS_toolbox/tests/test_glm_basis.py`
- `pyNIRS_toolbox/pyNIRS_toolbox/tests/test_connectivity_events.py`
- `pyNIRS_toolbox/pyNIRS_toolbox/tests/test_short_separation.py`
- `pyNIRS_toolbox/pyNIRS_toolbox/tests/test_roc_group.py`
- `pyNIRS_toolbox/pyNIRS_toolbox/pyBrainAnalyzIR/pipelines/default_pipelines.py`
- `pyNIRS_toolbox/pyNIRS_toolbox/pyBrainAnalyzIR/pipelines/modules/`

MATLAB demos:

- `nirs-toolbox/demos/fnirs_analysis_demo.m`
- `nirs-toolbox/demos/fnirs_analysis_demo2.m` (advanced FIR/deconvolution and
  group-model examples; referenced only to mark those topics as beyond the
  basic workflow summary)
- `nirs-toolbox/demos/fnirs_connectivity_demo.m`
