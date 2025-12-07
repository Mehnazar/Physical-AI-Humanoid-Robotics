# ADR-003: Math Depth Strategy (Medium Level with Optional Derivations)

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-07
- **Feature:** 001-physical-ai-book
- **Context:** Robotics fundamentals (kinematics, dynamics, control theory) inherently involve mathematical concepts. The book must balance accessibility for learners with non-mathematics backgrounds against the need for conceptual correctness and practical understanding. The spec requirement "minimal math - high-level concepts only" requires operationalization across diverse topics ranging from forward kinematics to reinforcement learning.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security? ✅ YES - Affects theory chapters, exercises, diagrams, prerequisite requirements
     2) Alternatives: Multiple viable options considered with tradeoffs? ✅ YES - Highly mathematical vs. almost no math vs. balanced approach
     3) Scope: Cross-cutting concern (not an isolated detail)? ✅ YES - Influences every theory section, assessment difficulty, target audience definition
-->

## Decision

**Include essential mathematical foundations (IK, control, dynamics) but keep full derivations optional or in appendices.**

**Math Presentation Guidelines:**
- **Show Equations:** Present key formulas with clear variable definitions (e.g., inverse kinematics Jacobian, PID control law)
- **Explain Intuition:** Provide conceptual explanations before mathematical formulation (what problem does this equation solve?)
- **Code-First Examples:** Implement equations in Python/ROS 2 immediately after introduction (equation → code → simulation)
- **Skip Derivations:** No theorem proving or step-by-step derivations in main content (move to appendices for interested readers)
- **Visual Emphasis:** Use diagrams and animations to convey mathematical relationships (e.g., coordinate frame transformations via 3D visualizations)

**Topic-Specific Guidelines:**
- **Forward/Inverse Kinematics:** Show DH parameters and transformation matrices; explain geometric meaning; skip analytical derivation of Jacobian
- **Control Theory:** Present PID equation with gain explanations; demonstrate tuning via simulation; skip Laplace transform stability proofs
- **Sensor Fusion:** Show Kalman filter equations conceptually; focus on uncertainty representation; skip covariance matrix derivations
- **Reinforcement Learning:** Explain reward functions and policy gradients intuitively; show PyTorch implementations; skip convergence proofs

## Consequences

### Positive

- **Broader Audience Access:** Learners with basic calculus (not advanced linear algebra/differential equations) can participate
- **Practical Focus:** Time spent coding and simulating rather than proving theorems aligns with "Physical AI" applied orientation
- **Reduced Intimidation:** Students less likely to abandon course when encountering equations (balanced presentation vs. wall-of-math)
- **Industry Alignment:** Most robotics engineers use libraries/frameworks implementing math (don't derive from scratch), so this reflects practice
- **Faster Progression:** Covering fewer derivations allows more topics within 13-week curriculum (e.g., include both classical control AND RL)
- **Academic Correctness Maintained:** Showing equations preserves theoretical grounding even if derivations omitted

### Negative

- **Shallow Understanding Risk:** Students may treat equations as "magic formulas" without grasping underlying principles
- **Limited Research Preparation:** Insufficient for graduate-level robotics research requiring theoretical rigor and novel algorithm development
- **Troubleshooting Difficulty:** When code fails, students may struggle to debug without deep mathematical intuition (e.g., singular Jacobians in IK)
- **Advanced Topics Constrained:** Some cutting-edge methods (e.g., differential geometry for motion planning) require heavier math, limiting curriculum depth
- **Credibility Questions:** Academic reviewers may perceive "minimal math" as insufficiently rigorous for university-level robotics course
- **Inconsistent Boundaries:** "Medium level" ambiguous—requires ongoing judgment calls about which derivations to include/exclude

## Alternatives Considered

### Alternative A: Highly Mathematical Approach (Full Derivations)
- **Approach:** Prove all theorems, derive all equations step-by-step, require linear algebra/differential equations prerequisites
- **Pros:** Deep conceptual understanding, prepares students for research, academically rigorous, enables novel algorithm development
- **Cons:** Excludes non-mathematics majors, slower content pace (fewer topics covered), high dropout risk for practitioners seeking applied skills
- **Why Rejected:** Conflicts with spec requirement "minimal math" and target audience including working professionals without advanced math backgrounds

### Alternative B: Almost No Math (Code-Only)
- **Approach:** Omit all equations, present algorithms purely as Python implementations with comments
- **Pros:** Maximum accessibility (high school algebra sufficient), fastest learning curve, immediate hands-on results
- **Cons:** Students can't understand WHY algorithms work, inability to modify/debug when libraries fail, lacks theoretical foundation required for robotics
- **Why Rejected:** Robotics fundamentally requires some mathematical reasoning (coordinate transformations, control laws); purely code-based approach produces "script kiddies" not engineers

### Alternative C: Math-on-Demand Structure
- **Approach:** Main chapters code-only, separate "Theory Deep Dives" appendix with full mathematical treatments
- **Pros:** Serves both audiences (practitioners skip appendix, theorists dive deep), flexible learning paths
- **Cons:** Disconnects theory from practice (students may never read appendices), harder to maintain two parallel treatments, assessments ambiguous (test theory or just code?)
- **Why Rejected:** Risk of students never engaging with theory; integrated approach (equations alongside code) better reinforces connections

### Alternative D: Adaptive Difficulty Tracks
- **Approach:** Mark sections as "Basic" / "Intermediate" / "Advanced" with increasing mathematical depth; students choose track
- **Pros:** Personalized learning, accommodates diverse backgrounds, advanced students not bored by simplifications
- **Cons:** 3x content authoring effort, complex navigation (chapter structure inconsistent), assessment difficulty (which track to test?)
- **Why Rejected:** Violates consistent structure principle (ADR-002), impractical for 13-week timeline given authoring overhead

## References

- Feature Spec: [specs/001-physical-ai-book/spec.md](../../specs/001-physical-ai-book/spec.md) (requirement: "minimal math - high-level concepts only")
- Implementation Plan: [specs/001-physical-ai-book/plan.md](../../specs/001-physical-ai-book/plan.md#3-mathematics-depth-specification)
- Research Guidelines: To be documented in `specs/001-physical-ai-book/research.md` (Phase 0 deliverable, plan.md:244)
- Related ADRs: ADR-002 (Pedagogical Structure defines math section placement), ADR-005 (AI Scope determines which math topics needed)
- User Input Context: Detailed rationale provided in `/sp.adr` command arguments emphasizing balanced approach
