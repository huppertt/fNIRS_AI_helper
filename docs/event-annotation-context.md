# Event Annotation Context

**Status:** Code-grounded prototype context; no event operation is executed by
the fNIRS AI Helper.

## Existing Brain Analyzer event representation

In pyNIRS_toolbox recordings, events are represented in a `stim` pandas
DataFrame. The Stimulus Manager uses `trial_type`, `onset`, `duration`, and
`value` as its core columns and can preserve extra columns. Event onsets and
durations are measured in seconds.

For task-model guidance on onset, duration, and amplitude, see
[Video-Lecture Context](video-lecture-context.md). Verify event timing and
duration from the experiment; do not infer them from markers alone.

## Existing onset/offset pairing behavior

The current pyNIRS_toolbox Stimulus Manager has an onset-to-offset operation in
`pyBrainAnalyzIR/vis/stimulus_manager.py`, implemented by
`StimTableModel.apply_onset_to_offset(start, end, remove_offsets)`.

In the Stimulus Manager, right-click the stimulus table and choose
**Edit Timing > Prune by Pattern > Onset to Offset marks**. In the dialog,
choose the **Start** and **End** event types and optionally check
**remove offset marks when finished**. This is a GUI feature; the helper
cannot operate it.

- When `start` and `end` are the same event type, events of that type are sorted
  by onset and paired in sequence: first with second, third with fourth, and so
  on. The first row in each pair receives a duration equal to the second
  event's onset minus the first event's onset.
- When `remove_offsets` is true, the paired second rows are removed from the
  event table.
- When `start` and `end` are different event types, each start is paired with
  the next later event of the end type. The present implementation does not
  consume an end after using it, so multiple starts may select the same end.
  Do not assume this different-type behavior is a one-to-one pairing.
- Pairing is scoped to each recording. The same-type case uses onset order,
  not the order in which the rows happen to be stored.

This operation is implemented on the Qt editor's table model, not yet as a
standalone, UI-independent annotation service or AI tool. The assistant in this
prototype can explain the documented operation but cannot call it.

## Odd/even language must be clarified

The original example description and the test question currently supplied to
the GUI disagree about whether odd or even markers are starts. These
descriptions reverse the pairing order.

The existing same-type pairing behavior pairs consecutive markers in onset
order with the first marker as the start. It therefore corresponds to
first/odd-numbered markers as starts and second/even-numbered markers as ends
when numbering begins at one. The assistant must point out the contradiction
and ask one short question to resolve it before recommending a specific
pairing. Do not provide code or describe multiple possible solutions while
waiting for that answer. Do not infer whether “odd/even” means one-based
chronological marker numbers, zero-based row indices, selected table rows, or
event-type labels without clarification.

## Prototype constraints

- This knowledge describes current code behavior, not a recommendation that
  applies to every study.
- The helper currently has no dataset connection and cannot inspect a
  recording to verify marker count, order, missing values, or timing.
- No marker pairing, event creation, renaming, shifting, or deletion is run by
  the helper.
- Any future mutating integration must validate the selected convention and
  show a concrete preview for user approval before changes are applied.

## Source provenance

Verified against the pyNIRS_toolbox source available locally on 2026-10-08:

- `pyBrainAnalyzIR/vis/stimulus_manager.py`:
  `StimTableModel.apply_onset_to_offset`,
  `OnsetOffsetDialog`, and the Stimulus Manager's onset-to-offset action.

The source repository was a separate working copy with existing uncommitted
changes at the time of inspection. Re-check this behavior against the intended
pyNIRS_toolbox revision before treating this note as version-independent.
