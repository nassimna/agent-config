# Accessibility evidence and checks

Use WCAG 2.2 criteria as specific checks when applicable. A design critique or
a score for visible presentation is not a full conformance assessment.

| Check | Criterion and interpretation |
| --- | --- |
| Text contrast | SC 1.4.3, AA: at least 4.5:1 for ordinary text and 3:1 for large text. Large means at least 18 pt, or 14 pt bold. Apply the criterion's exceptions, including incidental text and logotypes. |
| Non-text contrast | SC 1.4.11, AA: qualifying component indicators and graphical objects require 3:1 against adjacent colors. Check applicability and exceptions before declaring a failure. |
| Color reliance | SC 1.4.1, A: color must not be the only visual means of conveying information, indicating an action, prompting a response, or distinguishing an element. |
| Pointer target size | SC 2.5.8, AA: at least 24 × 24 CSS pixels, or an applicable exception. Smaller targets can meet the spacing exception; inspect the actual target, not just the visible icon. Inline, equivalent, user-agent, and essential exceptions also exist. |
| Keyboard and focus | SC 2.1.1, 2.4.7, and 2.4.11: inspect keyboard operation, visible focus, and focus not entirely hidden by author-created content. These require actual interaction evidence. |

Measure contrast from reliable foreground/background colors and target sizes
from the rendered interface or design properties with known scale. Resized or
compressed screenshots may not support exact measurements. Record the method,
value, and applicable criterion for numerical failures.

From screenshots, describe supported presentation concerns and label unknown
behavior unassessed. Screen-reader semantics, keyboard order, responsive reflow,
and off-screen states need their own evidence. Do not infer a passing score
for those areas from a polished image.

## Sources

Checked 4 November 2026:

- [W3C: WCAG 2.2](https://www.w3.org/TR/WCAG22/), Recommendation dated 12 December 2024 — the normative criteria and exceptions.
- [Understanding SC 1.4.3: Contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), explanatory guidance.
- [Understanding SC 2.5.8: Target Size](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html), explanatory guidance, including spacing and other exceptions.
