# ADR-006: Chapter Organization Strategy (Learning Progression)

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-07
- **Feature:** 001-physical-ai-book
- **Context:** The book must organize 8-12 chapters covering diverse topics (ROS 2, simulation, perception, VLA, hardware, capstone) into a coherent sequence. Different organizational schemes optimize for different learning goals: topic-based clustering (all ROS 2 content together) vs. skill progression (beginner→advanced regardless of topic) vs. subsystem-based (sensing, planning, control). The chosen structure determines prerequisite flow, navigation logic, and whether learners can skip chapters or must follow linear path.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security? ✅ YES - Affects book table of contents, navigation, teaching flow
     2) Alternatives: Multiple viable options considered with tradeoffs? ✅ YES - Subsystem-based, research area-based, pure difficulty progression
     3) Scope: Cross-cutting concern (not an isolated detail)? ✅ YES - Determines entire book structure, chapter dependencies, Docusaurus sidebar
-->

## Decision

**Organize chapters by learning progression: fundamentals → embodiment → locomotion → manipulation → high-level Physical AI.**

**Book Structure (8-12 chapters):**

1. **Introduction: Why Physical AI Matters** (foundational context)
2. **Prerequisites & Learning Outcomes** (skill assessment)
3. **Module 1: ROS 2 Fundamentals** (middleware/infrastructure)
   - Nodes, topics, services, URDF
4. **Module 2: Simulation Environments** (virtual testing)
   - Gazebo, Unity, sensor modeling
5. **Module 3: NVIDIA Isaac Perception** (sensing/understanding)
   - VSLAM, navigation, synthetic data
6. **Module 4: Vision-Language-Action Systems** (high-level reasoning)
   - LLM planning, Whisper voice, multimodal integration
7. **Capstone: Integrated Humanoid System** (synthesis)
8. **Hardware Specifications** (physical deployment)

**Dependency Flow:**
- **Linear Prerequisites:** Each module builds on previous (can't do Module 4 VLA without Module 1 ROS 2 knowledge)
- **Skill Indicators:** Sections marked "beginner/intermediate/advanced" within modules
- **Skip Guidance:** "If you already know ROS 2..." pointers to jump ahead
- **Reference Back-Links:** Advanced chapters reference specific earlier sections (e.g., "See Module 1: URDF for robot model definition")

## Consequences

### Positive

- **Clear Learning Path:** Beginners know exactly where to start (Introduction) and how to progress sequentially
- **Scaffolding:** Each module builds skills needed for next (ROS 2 → Simulation → Isaac uses ROS 2 knowledge)
- **Motivation Curve:** Progresses from simple (publish/subscribe) → complex (multimodal LLM integration), maintaining engagement
- **Modular Independence (Limited):** Advanced learners can skip modules IF they verify prerequisite knowledge via quizzes
- **Capstone Readiness:** By Module 4 completion, students have all skills needed for integrated capstone project
- **Curriculum Mapping:** 13-week semester structure naturally aligns (Weeks 1-3 Module 1, Weeks 4-6 Module 2, etc.)

### Negative

- **Forced Linearity:** Students interested specifically in VLA (Module 4) must complete Modules 1-3 first, delaying their primary interest
- **Topic Fragmentation:** Related concepts split across modules (e.g., sensor fusion appears in both Module 2 Simulation and Module 3 Isaac)
- **Reference Lookup Difficult:** If seeking specific technical detail (e.g., "How do I configure a LiDAR in Gazebo?"), must navigate multiple modules rather than one comprehensive "Sensors" chapter
- **Prerequisite Ambiguity:** Some sections could reasonably appear in multiple locations (e.g., "Control Theory" relevant to both Module 2 and Module 3)
- **Revision Complexity:** If industry shifts (e.g., Isaac becomes obsolete), must restructure entire progression vs. swapping single standalone chapter

## Alternatives Considered

### Alternative A: Organize by Robot Subsystem (Sense-Think-Act)
- **Approach:** Chapters structured as Perception → Planning → Control → Actuation (mirrors traditional robotics taxonomy)
- **Pros:** Clean conceptual separation, easy reference (all perception in one place), aligns with robotics textbooks (Siciliano, Thrun)
- **Cons:** Doesn't match actual development workflow (build simple systems first, add complexity), students can't build complete robot until final chapters
- **Why Rejected:** Learning progression requires working examples early; sense-think-act structure delays integration until end

### Alternative B: Organize by Research Area
- **Approach:** Chapters as Locomotion, Manipulation, HRI, Navigation, Learning (mirrors academic conference tracks)
- **Pros:** Aligns with research literature, students interested in specific area (e.g., grasping) find all content together
- **Cons:** Heavy prerequisite overlap (all areas need ROS 2, kinematics, simulation), unclear ordering (which area first?), not pedagogical
- **Why Rejected:** Designed for reference (researchers diving into specific area), not learning (students building foundational skills)

### Alternative C: Organize Strictly by Difficulty (Beginner → Expert)
- **Approach:** Chapter 1 = easiest robotics concepts, Chapter 12 = hardest, regardless of topic
- **Pros:** Perfect skill scaffolding, no prerequisite gaps, accommodates self-paced learning
- **Cons:** Topic incoherence (Chapter 3 might jump from ROS 2 to Isaac to Gazebo), hard to design (difficulty subjective), navigation confusing
- **Why Rejected:** Too abstract; students need topic coherence to build mental models (understand "simulation" as a concept, not scattered examples)

### Alternative D: Modular Independent Chapters (Choose Your Own Adventure)
- **Approach:** All chapters standalone with explicit prerequisites; students select learning path (e.g., "Manipulation Track" vs. "Navigation Track")
- **Pros:** Maximum flexibility, serves diverse interests, supports just-in-time learning (working engineers taking specific chapters)
- **Cons:** Overwhelming choice for beginners ("Where do I start?"), duplicated prerequisite content, capstone infeasible (can't assume shared knowledge)
- **Why Rejected:** Spec requirement for "13-week curriculum" implies structured progression, not self-guided exploration

## References

- Feature Spec: [specs/001-physical-ai-book/spec.md](../../specs/001-physical-ai-book/spec.md) (13-week curriculum structure)
- Implementation Plan: [specs/001-physical-ai-book/plan.md](../../specs/001-physical-ai-book/plan.md#6-content-organization-model)
- Book Structure: Docusaurus folder organization (plan.md:103-180)
- Weekly Breakdown: 13-week curriculum mapping (plan.md:377-390 data model)
- Related ADRs: ADR-002 (Pedagogical Structure within each chapter), ADR-005 (AI Scope determines progression from classical to AI methods)
- User Input Context: Emphasis on learning progression from fundamentals through advanced Physical AI integration
