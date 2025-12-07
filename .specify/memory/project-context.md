# Project Context: Physical AI & Humanoid Robotics Book

**Last Updated**: 2025-12-07
**Project**: Physical AI & Humanoid Robotics Educational Book
**Branch**: 001-physical-ai-book
**Status**: Planning Phase Complete

---

## Project Overview

An educational book on Physical AI and Humanoid Robotics built with Docusaurus v3, covering a 13-week curriculum from ROS 2 fundamentals through advanced Vision-Language-Action systems, culminating in a voice-controlled humanoid robot capstone project.

---

## Technology Stack

### Documentation & Build
- **Docusaurus v3** (static site generator)
  - React 18 (UI components)
  - MDX (enhanced markdown with React components)
  - Prism (syntax highlighting)
  - Mermaid (diagram generation)

### Deployment & CI/CD
- **GitHub Actions** (continuous integration/deployment)
- **GitHub Pages** (static site hosting, free tier)
- Node.js 18+ (build environment)

### Validation & Testing
- **markdownlint** (markdown quality checking)
- **Pytest** (Python code example validation)
- **JSON Schema** (assessment structure validation)
- Custom scripts (link checking, content coverage)

---

## Content Domain

### Robotics Technologies
- **ROS 2** (Robot Operating System 2)
  - Humble LTS distribution
  - rclpy (Python client library)
  - URDF (Unified Robot Description Format)
  - Nodes, topics, services, actions, parameters
  - MoveIt 2 (motion planning)
  - Nav2 (navigation stack)

- **Simulation Environments**
  - Gazebo Classic 11 / Gazebo Sim (Fortress/Garden)
  - Unity 2022 LTS + ROS TCP Connector (optional)
  - Webots R2023b (lightweight examples, optional)
  - Physics engines, sensor simulation, digital twins

- **NVIDIA Isaac**
  - Isaac Sim 2023.1+ (advanced perception, optional)
  - VSLAM (Visual Simultaneous Localization and Mapping)
  - Navigation pipelines
  - Synthetic data generation
  - TensorRT (inference optimization)

### AI/ML Technologies
- **Vision-Language-Action (VLA)**
  - OpenAI API (Whisper ASR, GPT for planning)
  - HuggingFace Transformers (open-source LLMs)
  - PyTorch / TensorFlow (model training)

- **Control Systems**
  - Classical control (PID, inverse kinematics)
  - Reinforcement Learning (PPO, SAC algorithms)
  - Stable-Baselines3 (RL library)
  - Sim-to-real transfer techniques

---

## Code Examples Language Stack

### Primary Language
- **Python 3.10+**
  - ROS 2 node implementations
  - Isaac perception scripts
  - VLA pipeline integration
  - RL training scripts

### Configuration Languages
- **YAML** (ROS 2 configuration, parameters)
- **XML** (URDF robot descriptions, SDF simulation worlds)
- **JSON** (assessment schemas, metadata)
- **Bash** (setup scripts, environment configuration)

### Optional Advanced
- **C++** (performance-critical ROS 2 nodes, mentioned but not required)

---

## Key Constraints & Design Decisions

### Content Approach
- **Minimal Math**: Intuition-focused, code-first examples, skip derivations
- **Reproducible Examples**: All code validated before publication (validation_status = "passing")
- **Consistent Structure**: 7-part chapter format (Overview → Theory → Lab → Project → Quiz)
- **Accessibility**: WCAG AA compliance (alt text for images, semantic HTML)

### Technical Constraints
- **GitHub Pages Limits**: <1GB total site size
- **GitHub Actions**: 2000 minutes/month free tier
- **Target Audience**: Intermediate learners (Python proficiency, Linux basics, ML familiarity)
- **Hardware**: Simulation-primary, physical hardware optional

### Validation Requirements
- Every theory section: 1 diagram + 1 code example + 1 real-world example
- Every module: ≥5 assessment questions
- Every code example: prerequisites + expected output + validation_status
- All diagrams: alt text (accessibility)
- Markdown: passes markdownlint
- Build: completes without errors

---

## Project Structure Reference

```
book/                   # Docusaurus site
├── docs/              # Content (modules, capstone, hardware)
├── static/            # Images, diagrams
├── src/               # Custom React components
└── code-examples/     # Validated Python examples

specs/001-physical-ai-book/
├── spec.md            # Feature requirements
├── plan.md            # Implementation plan
├── research.md        # Architecture decisions
├── data-model.md      # Content entity definitions
├── contracts/         # Templates (chapter, code, assessment)
├── quickstart.md      # Development guide
└── tasks.md           # Implementation tasks (to be generated)

scripts/               # Validation tools
tests/                 # Build and coverage tests
.github/workflows/     # CI/CD automation
```

---

## Success Criteria (from Constitution & Spec)

### Constitution Alignment
- ✅ Clarity and Correctness: Technical accuracy validated against authoritative sources
- ✅ AI-Assisted Drafting: Developer-friendly, practical utility focus
- ✅ Consistency: Standardized templates, terminology, formatting
- ✅ Reproducibility: All examples tested, simulation-based
- ✅ Security/Privacy: Educational content, no sensitive data

### Spec Success Metrics (SC-001 to SC-012)
- Navigation <30s to any topic (Docusaurus search + sidebar)
- 100% module content coverage (4 core modules complete)
- 13-week breakdown, 8-12 hours/week balance
- Actionable hardware specifications
- Completable capstone project from guide
- Responsive design (mobile/desktop)
- Deployment <5 minutes (GitHub Actions)
- All code with setup + expected output
- Architecture diagrams present (3 minimum)
- ≥5 assessment questions per module
- Prerequisites clearly stated
- ≥5 real-world applications in intro

---

## Development Workflow Commands

### Local Development
```bash
cd book && npm start        # Dev server with hot-reload
npm run build              # Production build
npm run serve              # Preview production build
```

### Validation
```bash
npm run lint:md                        # Markdown linting
python scripts/validate-code-examples.py  # Test code examples
node scripts/check-links.js            # Link validation
node tests/content-coverage.js         # Coverage check
```

### Deployment
```bash
git push origin main       # Triggers auto-deployment via GitHub Actions
```

---

## Content Creation References

### Templates
- Chapter: `specs/001-physical-ai-book/contracts/chapter-template.md`
- Code Example: `specs/001-physical-ai-book/contracts/code-example-template.py`
- Assessment: `specs/001-physical-ai-book/contracts/assessment-schema.json`

### Data Model
- Entities: CourseModule, ChapterSection, WeeklyBreakdown, CodeExample, Assessment, etc.
- Validation rules defined in `specs/001-physical-ai-book/data-model.md`

### Research Decisions
- Target audience: Intermediate (Python + Linux + ML basics)
- Tech stack: ROS 2 Humble + Python + Gazebo (primary)
- Math approach: Conceptual equations, code-first
- Hardware model: Simulation-primary, optional budget hardware
- AI scope: Classical foundations → RL-based control (both)
- Structure: Topic-based modules with dependencies

---

## Citation Style

**Format**: IEEE/ACM (standard in robotics)
```
[Author(s), "Title", Publication, Year]
```

**Examples**:
- [Siciliano et al., "Robotics: Modelling, Planning and Control", Springer, 2009]
- [Lynch & Park, "Modern Robotics", Cambridge University Press, 2017]

---

## Next Phase

**Status**: Phase 0 (Research) and Phase 1 (Design) complete
**Next**: Run `/sp.tasks` to generate `tasks.md` with actionable implementation tasks

**Deliverables Ready**:
- ✅ research.md (architecture decisions)
- ✅ data-model.md (entity definitions)
- ✅ contracts/ (chapter, code, assessment templates)
- ✅ quickstart.md (development guide)
- ✅ project-context.md (this file)

---

**Maintained By**: AI Agent (Claude Code)
**Auto-Generated**: Yes (from /sp.plan workflow)
**Manual Updates**: Allowed between markers (if added)
