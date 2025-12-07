# ADR-004: Hardware Integration Model (Simulation-First with Optional Low-Cost Robots)

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-07
- **Feature:** 001-physical-ai-book
- **Context:** Physical robotics hardware provides invaluable hands-on learning but creates barriers: cost ($200-$5000+), shipping/availability (international students), space requirements (dorm rooms), and safety concerns (moving actuators). The book must serve both resourced institutions and individual learners with limited budgets while maintaining pedagogical value.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security? ✅ YES - Impacts examples, exercises, project requirements, GitHub repository structure
     2) Alternatives: Multiple viable options considered with tradeoffs? ✅ YES - Mandatory hardware vs. hardware-free vs. hybrid
     3) Scope: Cross-cutting concern (not an isolated detail)? ✅ YES - Affects budget, accessibility, physical testing sections, capstone feasibility
-->

## Decision

**The course book is simulation-first with optional low-cost robot hardware extensions.**

**Primary Learning Path (Simulation):**
- All core content completable using **Webots, Gazebo, and NVIDIA Isaac** simulations
- Capstone project fully executable in simulation (voice-controlled humanoid navigation)
- Code examples tested in virtual environments (no hardware dependency)
- Success criteria validated purely through simulation metrics

**Optional Hardware Track:**
- **Hardware section** (`book/docs/hardware/`) provides detailed specifications for three tiers:
  1. **Budget Kit ($200-$500):** TurtleBot3 Burger, basic servos, Raspberry Pi 4
  2. **Intermediate Kit ($500-$1500):** Jetson Orin Nano, depth camera, mobile manipulator base
  3. **Advanced Kit ($1500-$5000):** Full humanoid platform (GR-1, Unitree H1 alternatives), RTX workstation
- **Bonus exercises:** "If you have hardware..." sections in chapters (not required for completion)
- **Community contributions:** GitHub repo accepts PRs for hardware integration guides

## Consequences

### Positive

- **Universal Accessibility:** Any student with laptop (Windows/Mac/Linux) can complete full curriculum regardless of budget/location
- **Cost Elimination Barrier:** $0 hardware cost (beyond computer) removes primary obstacle for self-learners in developing countries
- **Safety:** No risk of mechanical injuries from malfunctioning robots; suitable for younger learners (high school robotics clubs)
- **Reproducibility:** Simulation environments deterministic; students get identical results, simplifying grading/troubleshooting
- **Iteration Speed:** Code-test cycle faster in simulation (no battery charging, mechanical wear, recalibration delays)
- **Scalability:** Universities can serve unlimited students without purchasing robot fleets or lab space

### Negative

- **Reality Gap:** Sim-to-real transfer not covered; students may overestimate how well algorithms work on physical robots (friction, sensor noise, latency)
- **Motivation Loss:** Some learners less engaged without tangible robot to show friends/family; simulation feels "less real"
- **Missing Skills:** Never learn hardware debugging (motor driver issues, wiring, power management, mechanical assembly)
- **Industry Mismatch:** Robotics jobs ultimately require physical robot experience; simulation-only training incomplete
- **Limited Sensorimotor Learning:** Can't develop intuition for physical phenomena (inertia, compliance, impact dynamics) through keyboard/mouse
- **Perception Limitations:** Simulated sensors (cameras, LiDAR) lack real-world artifacts (lens distortion, dust, lighting variations) critical for robust perception

## Alternatives Considered

### Alternative A: Mandatory Hardware (Required Physical Robot Kit)
- **Approach:** Course requires purchase of specific robot kit ($500-$1000); all exercises hardware-based
- **Pros:** Forces hands-on skills, prepares for industry, highly engaging, learns troubleshooting/debugging physical systems
- **Cons:** Excludes students without budget, shipping impossible to some countries, institutional lab requirements, safety liability
- **Why Rejected:** Conflicts with accessibility goal; cannot justify mandatory $500+ barrier for educational content meant to be globally available

### Alternative B: Hardware-Free Book (No Physical Robot Section)
- **Approach:** Pure simulation; no hardware recommendations or integration guides; focus entirely on virtual robots
- **Pros:** Simplified curriculum scope, no hardware maintenance content needed, universal applicability
- **Cons:** Disconnects content from "Physical AI" theme, misses opportunities for motivated students with budgets, less industry-relevant
- **Why Rejected:** Leaves gap for advanced learners; hardware section provides value even if optional (career paths, lab setup guidance)

### Alternative C: Cloud-Based Physical Robot Access
- **Approach:** Partner with remote labs (e.g., CloudLabs, AWS RoboMaker) providing web-based access to real robots
- **Pros:** Combines physical robot benefits with accessibility, no local hardware needed, safety managed by lab
- **Cons:** Requires internet (excludes offline learners), scheduling conflicts (shared resources), subscription costs, latency issues for real-time control
- **Why Rejected:** Subscription costs recreate financial barrier; resource scheduling reduces flexibility; emerging service (risky dependency)

### Alternative D: Hybrid Simulation + Required Minimal Hardware
- **Approach:** Simulation primary but requires cheap sensors ($50-$100) for 1-2 chapters (e.g., Arduino + IMU, Raspberry Pi + camera)
- **Pros:** Taste of hardware without full robot cost, teaches sensor interfacing, validates perception algorithms on real data
- **Cons:** Still creates financial barrier (even $50 excludes some learners), fragmented learning (switch between sim and hardware)
- **Why Rejected:** Even minimal hardware cost contradicts accessibility priority; sensor-only exercises don't justify complexity vs. full simulation

## References

- Feature Spec: [specs/001-physical-ai-book/spec.md](../../specs/001-physical-ai-book/spec.md) (Hardware Requirements section)
- Implementation Plan: [specs/001-physical-ai-book/plan.md](../../specs/001-physical-ai-book/plan.md#4-hardware-integration-strategy)
- Hardware Section Structure: `book/docs/hardware/` (plan.md:147-152)
- Research Deliverable: Budget tiers documented in `specs/001-physical-ai-book/research.md` (plan.md:304)
- Related ADRs: ADR-001 (Primary Technology Ecosystem includes simulation tools), ADR-005 (AI Scope affects hardware complexity needs)
- User Input Context: Detailed rationale emphasizing simulation-first approach with optional hardware extensions
