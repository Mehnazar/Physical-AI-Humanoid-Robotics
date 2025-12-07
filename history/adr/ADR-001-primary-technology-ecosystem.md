# ADR-001: Primary Technology Ecosystem (ROS 2 + Python + Webots)

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-07
- **Feature:** 001-physical-ai-book
- **Context:** The educational book requires a technology stack that balances accessibility for students, realism for robotics learning, and industry relevance for career preparation. The stack must support simulation environments, code examples, and hands-on learning while remaining installable on consumer hardware.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security? ✅ YES - Affects all code examples, API explanations, project templates
     2) Alternatives: Multiple viable options considered with tradeoffs? ✅ YES - ROS 1, C++-only, Gazebo/Isaac alternatives considered
     3) Scope: Cross-cutting concern (not an isolated detail)? ✅ YES - Impacts curriculum structure, installation requirements, all chapters
-->

## Decision

Use **ROS 2** as the robotics middleware, **Python** as the primary coding language, and **Webots** as the simulation environment for the Physical AI & Humanoid Robotics educational book.

**Technology Components:**
- **Middleware:** ROS 2 Humble (industry-standard robotics framework)
- **Primary Language:** Python 3.10+ (accessibility, extensive libraries)
- **Simulation Environment:** Webots (lightweight, realistic, cross-platform)
- **Supporting Tools:** Gazebo (advanced physics), Unity (VR/AR integration), NVIDIA Isaac (perception/AI)

## Consequences

### Positive

- **Industry Relevance:** ROS 2 is the current industry standard used by research labs and robotics companies (Boston Dynamics, Agility Robotics workflows are ROS-compatible)
- **Accessibility:** Python has gentle learning curve compared to C++, enabling broader audience participation
- **Cross-Platform:** Webots runs on Windows/Mac/Linux without requiring dedicated GPU, lowering hardware barriers
- **Ecosystem Maturity:** Extensive ROS 2 packages, community support, and third-party integrations available
- **Simulation Realism:** Webots provides physics-accurate simulation suitable for educational demonstrations without heavy compute requirements
- **Career Preparation:** Skills directly transfer to industry robotics engineering roles

### Negative

- **Version Dependency Risk:** ROS 2 updates may break code examples, requiring ongoing maintenance and versioning documentation
- **Installation Complexity:** ROS 2 installation on Windows/Mac more complex than on Linux, may frustrate beginners
- **Performance Limitations:** Python slower than C++ for real-time control (though acceptable for educational purposes)
- **Webots Limitations:** Less feature-rich than Gazebo/Isaac for advanced scenarios (mitigated by including both as optional advanced tracks)
- **Learning Overhead:** Students must learn both ROS 2 paradigms (nodes, topics, services) AND Python robotics libraries

## Alternatives Considered

### Alternative A: ROS 1 + Python + Gazebo
- **Pros:** More mature documentation, larger community, Gazebo tightly integrated
- **Cons:** ROS 1 officially deprecated (EOL 2025), teaching obsolete technology harms student careers
- **Why Rejected:** Cannot justify teaching deprecated framework when ROS 2 is industry future

### Alternative B: C++-Only Approach (ROS 2 + C++ + Gazebo)
- **Pros:** Better performance, matches production robotics code, deeper systems understanding
- **Cons:** Steep learning curve excludes non-CS majors, longer time-to-first-working-example, harder to debug
- **Why Rejected:** Spec requirement "minimal math, high-level concepts" implies accessibility priority; Python better aligns with target audience

### Alternative C: Gazebo / Isaac Sim (without Webots)
- **Pros:** More realistic physics (Gazebo), cutting-edge AI capabilities (Isaac Sim)
- **Cons:** Higher hardware requirements (RTX GPU mandatory for Isaac), larger installation size, steeper learning curve
- **Why Rejected:** Gazebo included as advanced option, Isaac as optional Module 3; Webots remains primary for accessibility

### Alternative D: Proprietary Simulation (MATLAB/Simulink, V-REP)
- **Pros:** Industry use in automotive/aerospace, integrated toolchains
- **Cons:** Licensing costs prohibitive for students, not open-source (conflicts with educational accessibility), less robotics-specific than ROS
- **Why Rejected:** Must remain free and open-source per project constraints

## References

- Feature Spec: [specs/001-physical-ai-book/spec.md](../../specs/001-physical-ai-book/spec.md)
- Implementation Plan: [specs/001-physical-ai-book/plan.md](../../specs/001-physical-ai-book/plan.md#phase-0-research--architecture-decisions)
- Related ADRs: ADR-004 (Hardware Integration Model), ADR-005 (AI Scope Strategy)
- User Input Context: Detailed decision rationale provided in `/sp.adr` command arguments
