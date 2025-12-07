# ADR-005: AI Scope Strategy (Hybrid Classical + Learning-Based Methods)

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-07
- **Feature:** 001-physical-ai-book
- **Context:** Humanoid robotics historically relied on classical control methods (PID, model predictive control) but is rapidly shifting toward learning-based approaches (reinforcement learning, imitation learning, foundation models). The book titled "Physical AI & Humanoid Robotics" must position itself within this transition, determining whether to teach legacy methods, cutting-edge AI, or both. This decision affects curriculum structure, prerequisites, industry relevance, and pedagogical complexity.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security? ✅ YES - Affects curriculum structure, chapter dependencies, diagrams, simulation examples
     2) Alternatives: Multiple viable options considered with tradeoffs? ✅ YES - Classical-only vs. AI-only vs. hybrid progression
     3) Scope: Cross-cutting concern (not an isolated detail)? ✅ YES - Determines which topics covered, prerequisite depth, capstone project design
-->

## Decision

**Teach both classical robotics (PID, IK, kinematics, motion planning) and modern AI-based approaches (RL locomotion, policy learning, VLA systems) in a progressive hybrid curriculum.**

**Curriculum Structure:**

**Weeks 1-6: Classical Foundations**
- Forward/inverse kinematics (geometric methods)
- PID control and trajectory tracking
- Motion planning (RRT, A*)
- Sensor fusion (Kalman filtering)
- **Rationale:** Establish fundamental understanding of robot mechanics, state estimation, and control before introducing learned policies

**Weeks 7-13: AI-Enhanced Methods**
- Reinforcement learning for locomotion (PPO, SAC)
- Imitation learning from demonstrations
- Vision-Language-Action models (LLM planning + Whisper voice)
- Sim-to-real transfer techniques
- **Rationale:** Build on classical foundation with data-driven approaches that address limitations (hand-tuned gains, brittle planning)

**Integration Points:**
- **Week 6 Transition:** Demonstrate classical control limitations (high-dimensional state spaces, complex dynamics) motivating AI approaches
- **Capstone Project:** Hybrid system combining classical motion planning with learned policies for humanoid navigation
- **Comparative Exercises:** Implement same task (e.g., bipedal walking) using both classical (ZMP-based) and RL-based (PPO) methods

## Consequences

### Positive

- **Industry Alignment:** Reflects current robotics R&D reality where teams combine classical control (low-level) with learned policies (high-level)
- **Comprehensive Skill Set:** Graduates understand both paradigms, employable at companies using either approach (traditional manufacturing vs. AI robotics startups)
- **Troubleshooting Capability:** Classical foundation enables debugging when learned policies fail (check if kinematics correct, sensors calibrated, etc.)
- **Research Preparation:** Students can contribute to cutting-edge humanoid AI (Tesla Bot, Figure 01, Sanctuary AI) which all use hybrid architectures
- **Pedagogical Progression:** Classical methods easier to understand (deterministic, interpretable), providing scaffolding before stochastic policies
- **Future-Proofing:** If AI methods mature further, students have foundation to adopt new techniques; if AI hype fades, classical skills remain valuable

### Negative

- **Curriculum Overload:** Covering both approaches nearly doubles content volume, risking superficial treatment of each
- **Prerequisite Expansion:** Requires both control theory background (Laplace transforms) AND machine learning (neural networks, optimization), narrowing audience
- **Conflicting Mental Models:** Students may confuse when to use classical vs. learned approaches, leading to inappropriate method selection
- **Implementation Complexity:** RL training requires GPU compute, hyperparameter tuning, long convergence times—difficult within 13-week course
- **Maintenance Burden:** Must track updates to both control libraries (ROS 2 control) and ML frameworks (PyTorch, Stable-Baselines3)
- **Time Constraints:** Deep coverage sacrificed for breadth; students may master neither classical nor AI methods fully

## Alternatives Considered

### Alternative A: Classical Control Only (No AI/ML Methods)
- **Approach:** Focus entirely on kinematics, dynamics, PID, MPC, classical motion planning; omit neural networks and RL
- **Pros:** Simpler prerequisites (no ML required), mature stable algorithms, deterministic behavior easier to teach/debug
- **Cons:** Outdated relative to "Physical AI" theme, misses industry shift toward learning (Tesla Optimus, Figure 01 both RL-based), less engaging for AI-interested students
- **Why Rejected:** Book title "Physical AI" explicitly signals AI integration; classical-only approach false advertising and misses primary innovation area

### Alternative B: AI-Only (Reinforcement Learning from Scratch)
- **Approach:** Skip classical control; teach locomotion/manipulation purely via RL and imitation learning; treat robot as black-box environment
- **Pros:** Aligns with cutting-edge research, engaging for ML practitioners, avoids "boring" control theory, faster path to impressive demos
- **Cons:** Students can't debug failures (don't understand kinematics, dynamics), brittle policies (no fallback), misses robotics fundamentals required for industry
- **Why Rejected:** Insufficient foundational understanding; produces ML engineers who happen to work on robots, not roboticists who use ML

### Alternative C: AI-First Progression (Reverse Order)
- **Approach:** Start with RL/imitation learning (Weeks 1-6), introduce classical control later as "backup methods" (Weeks 7-13)
- **Pros:** Immediate engagement with AI (student motivation), demonstrates need for classical methods through RL failures
- **Cons:** Students lack debugging skills when RL training fails (is reward function wrong? or kinematics misconfigured?), pedagogically backwards (complex before simple)
- **Why Rejected:** Violates learning science (scaffolding requires simple→complex); frustration risk when students can't diagnose RL issues

### Alternative D: Parallel Tracks (Students Choose Classical OR AI Track)
- **Approach:** Weeks 1-3 shared foundation, then students select track: Track A (classical control) or Track B (AI methods)
- **Pros:** Personalized learning paths, each track goes deeper (no breadth compromise), students focus on career interest
- **Cons:** 2x content authoring, splits community (students can't collaborate across tracks), misses hybrid integration (the actual industry practice)
- **Why Rejected:** Hybrid approach is industry standard (not either/or); splitting prevents teaching most valuable skill (knowing when to use each)

## References

- Feature Spec: [specs/001-physical-ai-book/spec.md](../../specs/001-physical-ai-book/spec.md) (Module 4: Vision-Language-Action explicitly requires AI methods)
- Implementation Plan: [specs/001-physical-ai-book/plan.md](../../specs/001-physical-ai-book/plan.md#5-aicontrol-scope-definition)
- Research Deliverable: Control curriculum map in `specs/001-physical-ai-book/research.md` (plan.md:305)
- Curriculum Structure: Weekly breakdown (plan.md:107) shows ROS 2/Simulation first, then Isaac/VLA
- Related ADRs: ADR-003 (Math Depth affects control theory prerequisites), ADR-004 (Hardware model affects RL sim-to-real transfer feasibility)
- User Input Context: Explicit requirement to cover both classical and learning-based methods in hybrid curriculum
