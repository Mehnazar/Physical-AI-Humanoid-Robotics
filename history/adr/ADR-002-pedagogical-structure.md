# ADR-002: Pedagogical Structure (Concept → Theory → Math → Code → Simulation → Exercises)

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-07
- **Feature:** 001-physical-ai-book
- **Context:** The book requires a consistent pedagogical structure that serves both beginner learners (who need progressive scaffolding) and advanced learners (who want reference material). The structure must support the "minimal math, practical focus" requirement while maintaining academic rigor. All chapters must follow a predictable pattern to reduce cognitive load and improve navigation.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security? ✅ YES - Shapes entire book layout, writing process, Docusaurus design
     2) Alternatives: Multiple viable options considered with tradeoffs? ✅ YES - Free-form, research-paper style, theory-only/practice-only formats
     3) Scope: Cross-cutting concern (not an isolated detail)? ✅ YES - Affects every chapter, navigation, student learning outcomes
-->

## Decision

Each chapter follows a **consistent 7-part pedagogical structure**:

1. **Overview** - Learning outcomes, prerequisites, estimated time
2. **Theory & Concepts** - Intuitive explanations with minimal math
3. **Mathematical Foundations** - Key equations with variable definitions (derivations optional/appendix)
4. **Code Examples** - Validated Python/ROS 2 implementations
5. **Simulation Lab** - Hands-on Webots/Gazebo exercises
6. **Module Project** - Integrative challenge with rubric
7. **Quiz & Self-Assessment** - 5+ questions per module

**Template Enforcement:**
- `contracts/chapter-template.md` defines mandatory sections
- Markdown validation checks structural compliance
- Every concept requires: 1 diagram, 1 code example, 1 real-world application

## Consequences

### Positive

- **Cognitive Predictability:** Students know what to expect in each chapter, reducing mental load when navigating content
- **Learning Progression:** Natural flow from abstract (theory) → concrete (code) → experiential (simulation) → assessment
- **Multi-Modal Learning:** Accommodates different learning styles (visual: diagrams, kinesthetic: labs, logical: math)
- **Beginner-Friendly:** Clear scaffolding from concepts to implementation reduces intimidation factor
- **Advanced-Learner Support:** Experienced students can skip to code/simulation sections while still accessing reference material
- **Content Completeness:** Template checklist ensures no critical sections omitted (e.g., every theory has corresponding code)
- **Quality Assurance:** Structural consistency enables automated validation (markdown linting, coverage checks)

### Negative

- **Rigidity Constraints:** Authors must fit content into prescribed structure even when alternative flow might be clearer for specific topics
- **Repetitive Writing:** Template requirements may feel formulaic, potentially reducing creativity in presentation
- **Length Inflation:** Mandatory sections (especially diagrams, projects, quizzes) increase content volume and writing time
- **Unnatural Topic Fits:** Some topics (e.g., high-level architecture discussions) don't naturally map to "code → simulation → project" flow
- **Maintenance Overhead:** Changing structure later requires updating all chapters uniformly, creating migration complexity

## Alternatives Considered

### Alternative A: Free-Form Chapter Writing
- **Approach:** Authors choose structure per topic (some chapters mostly theory, others mostly code)
- **Pros:** Flexibility for optimal topic presentation, shorter chapters for simple concepts, author creativity
- **Cons:** Inconsistent navigation experience, advanced learners can't predict where to find information, harder to validate completeness
- **Why Rejected:** Spec requirement for "consistent structure" prioritizes learner navigation over author flexibility

### Alternative B: Research-Paper Style Chapters
- **Approach:** Abstract → Related Work → Methodology → Results → Conclusion (academic format)
- **Pros:** Familiar to graduate students, emphasizes rigor and citations, supports deeper theoretical exploration
- **Cons:** Intimidating for undergraduates, overly formal for applied content, doesn't align with "practical focus" spec requirement
- **Why Rejected:** Educational book targets practitioners, not researchers; need accessible tone

### Alternative C: Mostly Theoretical or Mostly Practical Formats
- **Approach:** Separate "theory volume" and "practice volume" books
- **Pros:** Clearer audience segmentation, each volume optimized for its purpose, allows deeper dives
- **Cons:** Students lose integration between theory and practice (key to robotics understanding), doubles content maintenance
- **Why Rejected:** "Physical AI" concept requires tight theory-practice integration; simulation validates theoretical understanding

### Alternative D: Problem-Based Learning Structure
- **Approach:** Each chapter starts with a challenge, students explore solutions, theory introduced as needed
- **Pros:** High engagement, motivation through authentic problems, discovery learning
- **Cons:** Harder for reference lookup (theory scattered), requires skilled problem design, may confuse weaker students
- **Why Rejected:** While engaging, harder to maintain consistency and risks incomplete theory coverage

## References

- Feature Spec: [specs/001-physical-ai-book/spec.md](../../specs/001-physical-ai-book/spec.md)
- Implementation Plan: [specs/001-physical-ai-book/plan.md](../../specs/001-physical-ai-book/plan.md#12-content-structure-contracts-contracts)
- Chapter Template: `.specify/templates/contracts/chapter-template.md` (referenced in plan.md:482-543)
- Related ADRs: ADR-003 (Math Depth Strategy), ADR-007 (Chapter Organization by Learning Progression)
- User Input Context: Detailed rationale provided in `/sp.adr` command arguments
