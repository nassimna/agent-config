# Dashboard review

## Match the task

Identify whether the dashboard primarily supports time-sensitive monitoring or
analysis. Monitoring needs quickly recognizable exceptions and relevant next
actions. Analysis needs understandable comparisons and context. Use the actual
brief; do not force every dashboard into a single-screen layout.

## Inspect quantitative communication

- For precise comparisons, consider whether aligned position or length would
  communicate the relationship more clearly than area or angle. Explain the
  tradeoff in context; do not automatically reject every pie chart or treemap.
- Check whether emphasis highlights the important exception rather than
  decorative content. Use consistent encodings for comparable series, with
  labels or other cues alongside color.
- Check labels, units, periods, active filters, baselines, and comparison
  context before judging a trend. A positive change is not universally good.
- Distinguish missing or unavailable data from measured zero. Flag unsupported
  certainty when estimates are displayed as if exact, but do not invent the
  underlying data quality or statistical significance.
- When uncertainty could materially change a comparison or decision, check
  whether the chart communicates it with understandable ranges or context.
  Do not require uncertainty bands when they would add noise without changing
  the interpretation.
- Inspect whether written context helps users interpret the data. A dashboard
  should not require users to reconstruct every important insight themselves.

Score metric meaning, data visualization, filter clarity, and actionability
separately. If the filter is visible but untested, assess its presented scope
and labels, leaving its functional behavior unassessed.

## Sources

Paraphrased guidance, checked 4 November 2026:

- [NN/g: Dashboards — Making Charts and Graphs Easier to Understand](https://www.nngroup.com/articles/dashboards-preattentive/), 18 June 2017 — monitoring versus analysis and quantitative perception.
- [ONS: Dashboards](https://service-manual.ons.gov.uk/data-visualisation/guidance/dashboards), undated — prominent insights, explanatory context, user needs, and allowing scrolling.
- [ONS: Showing uncertainty in charts](https://service-manual.ons.gov.uk/data-visualisation/guidance/showing-uncertainty-in-charts), undated — communicate uncertainty when it affects interpretation.
