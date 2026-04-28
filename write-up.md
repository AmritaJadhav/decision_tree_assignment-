# Design Rationale – Deterministic Reflection Agent

## 1. Why These Questions
- Axis 1 (Locus): I chose questions that surface whether the employee sees agency in their day or feels controlled by external factors. Example: “Did you complete your tasks today?” followed by “Was it due to external factors?” These highlight internal vs external locus of control.
- Axis 2 (Orientation): I designed questions around contribution vs entitlement. Example: “Think about one interaction you had today. Were you giving or expecting?” This makes invisible entitlement visible without shaming.
- Axis 3 (Radius): I asked about perspective. Example: “When you think about today’s biggest challenge, who comes to mind?” Options progress from self to team to customer, surfacing how wide the employee’s concern is.

## 2. Branching Design
- Each axis has at least two question nodes and reflection nodes.
- Decision nodes route answers deterministically (e.g., “Yes” → contribution branch, “No” → entitlement branch).
- Bridge nodes connect axes smoothly, so the conversation feels like one flow rather than three separate quizzes.
- Reflections are written to reframe, not judge. They encourage awareness without moralizing.

## 3. Psychological Sources
- **Julian Rotter (1954)** – Locus of Control: internal vs external agency.
- **Carol Dweck (2006)** – Growth Mindset: effort and adaptation vs fixed talent.
- **Campbell et al. (2004)** – Psychological Entitlement: belief in deserving more than others.
- **Organ (1988)** – Organizational Citizenship Behavior: discretionary effort beyond formal role.
- **Maslow (1969)** – Self-Transcendence: orienting outward toward others.
- **Batson (2011)** – Perspective-Taking: empathy as understanding.

## 4. Trade-offs
- I kept options short and distinct (3–5 choices per question) to avoid overlap and confusion.
- I avoided free-text input to maintain determinism.
- I balanced depth with simplicity: enough nodes to meet requirements (25+) but not so many that the user feels overwhelmed.

## 5. Improvements With More Time
- Add richer reflections that interpolate earlier answers (e.g., “You said today was ‘Tough’, but you also helped a colleague — that shows agency.”).
- Build a web UI for smoother interaction.
- Expand the tree with more nuanced options (e.g., stress, recognition, collaboration).
- Test with different personas to refine wording and ensure questions feel natural.

