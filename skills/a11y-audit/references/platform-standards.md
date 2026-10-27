# Platform Accessibility References

Check the current version and applicability when starting an audit. Do not mix measurement units or present a recommendation as a normative requirement.

- **Web:** [WCAG 2.2](https://www.w3.org/TR/WCAG22/) is the W3C Recommendation. Use the [ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/) for widget patterns; APG examples do not replace WCAG evaluation.
- **Android:** [Android accessibility principles](https://developer.android.com/guide/topics/ui/accessibility) and [touch target guidance](https://support.google.com/accessibility/android/answer/7101858). Android uses dp for layout/touch guidance; do not convert it to CSS px or Apple points.
- **Apple platforms:** [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) and platform accessibility documentation. Test VoiceOver, Dynamic Type, platform gestures, and actual hit regions on supported builds.
- **Voice and natural language:** [W3C COGA voice research module](https://www.w3.org/TR/coga-voice/) is a Group Note Draft, and [Natural Language Interface Accessibility User Requirements](https://www.w3.org/TR/naur/) is a user-needs reference. Neither replaces evaluation of the full interface against applicable standards.

The supplied toolkit describes WCAG 2.2 target size at 24×24 CSS px with exceptions and Android's 48×48 dp as platform guidance. Verify the criterion text and exception conditions before applying them to a finding.
