# [Module Name]: [Chapter Title]

<!--
CHAPTER TEMPLATE for Physical AI & Humanoid Robotics Book
This template defines the required structure for all module chapter sections.

VALIDATION REQUIREMENTS:
- Every theory section MUST include: 1 diagram, 1 code example, 1 real-world example
- Section order: Overview → Theory (1+) → Lab → Project → Quiz
- All code examples must have validation_status = "passing"
- Markdown must pass markdownlint
-->

---

## Overview (Required)

**Learning Outcomes**:
- [Specific skill/knowledge learners will gain - use action verbs]
- [Example: "Implement ROS 2 publisher/subscriber nodes in Python"]
- [Example: "Explain when to use topics vs services vs actions"]
- [Minimum 3 outcomes per chapter]

**Prerequisites**:
- [Required prior knowledge or completed chapters]
- [Example: "Module 1: ROS 2 Fundamentals - Nodes"]
- [Example: "Basic Python programming (functions, classes)"]

**Estimated Time**: [X minutes reading + Y minutes exercises] (Total: Z minutes)

**Difficulty**: 🟢 Beginner / 🟡 Intermediate / 🔴 Advanced

---

## Theory & Concepts (Required, can be multiple sections)

### [Concept Name 1]

**Intuitive Explanation**:
[High-level explanation in plain language. Focus on "what" and "why" before "how".]
[Use analogies, avoid jargon where possible.]
[Example: "ROS 2 topics work like a radio station: publishers broadcast messages on a channel, and any number of subscribers can tune in to receive them."]

**Key Equation** (if applicable):
```
[Present equation with clear variable definitions]
[Example: v = ω × r  (linear velocity = angular velocity × radius)]
```

**Variables**:
- `v`: Linear velocity (m/s)
- `ω`: Angular velocity (rad/s)
- `r`: Radius (m)

**Intuition**: [Explain what the equation means in practical terms, skip derivation]

**Link to Code**: See [code example ID] which implements this equation.

---

**Real-World Example**:
[2-3 sentence industry application showing where/how this concept is used]
[Example: "Autonomous vehicles use ROS 2 topics to stream LiDAR point clouds at 10Hz from sensors to perception nodes, enabling real-time obstacle detection. Waymo's self-driving stack processes 1.5 million points per second using this publish-subscribe pattern."]

**Source/Reference**: [Company blog, technical paper, or "Industry standard practice"]

---

**Diagram**:
[Include Mermaid diagram or reference to image]

```mermaid
[Mermaid syntax here]
[Example:
graph LR
  A[Publisher Node] -->|/topic_name| B[Subscriber Node]
]
```

**Alt Text**: [Accessibility description of diagram]
[Example: "Flowchart showing publisher node sending messages to subscriber node via /topic_name"]

**Caption**: Figure X.Y: [Brief description]

---

**Code Example**:
Reference: [`[example-id]`](../../code-examples/[module]/[filename])

```python
# Inline snippet (first 10-15 lines) or link to full example
# Full code must be in code-examples/ directory and validated

import rclpy
from rclpy.node import Node

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        # ... (see full example for complete code)
```

**What this demonstrates**: [One sentence explaining the code's purpose]

**Key lines to note**:
- **Line X**: [Explanation of critical line]
- **Line Y**: [Explanation of critical line]

---

### [Concept Name 2]
[Repeat theory section structure for additional concepts]

---

## Hands-On Lab (Required)

**Objective**: [What learners will build/accomplish in this lab]
[Example: "Build a ROS 2 publisher-subscriber system that sends sensor data and visualizes it in real-time"]

**Prerequisites**:
- [Software/setup required before starting]
- [Example: "ROS 2 Humble installed and sourced"]
- [Example: "Completed Module 1 Lab 1 (workspace setup)"]

**Setup Instructions**:
1. [Step-by-step setup commands]
2. [Include all dependencies, environment configuration]
3. [Example: `source /opt/ros/humble/setup.bash`]
4. [Example: `colcon build --packages-select my_package`]

**Implementation Steps**:

### Step 1: [Task Name]
```bash
# Commands or code to execute
[Include clear commands with explanations]
```

**What's happening**: [Explain what this step does]

### Step 2: [Task Name]
[Continue numbered steps]

### Step 3: Testing
```bash
# How to verify the implementation works
[Example: ros2 topic echo /sensor_data]
```

**Expected Output**:
```
[Show what learners should see]
[Example: sensor_data: 42.7]
```

**Success Criteria**:
- [ ] [Checkpoint 1: e.g., "Topic appears in `ros2 topic list`"]
- [ ] [Checkpoint 2: e.g., "Messages received at 1Hz"]
- [ ] [Checkpoint 3: e.g., "No errors in console"]

**Troubleshooting**:

| Issue | Cause | Solution |
|-------|-------|----------|
| "Package not found" | ROS 2 not sourced | Run `source /opt/ros/humble/setup.bash` |
| Messages not received | Topic name mismatch | Verify publisher/subscriber use same topic name |
| [Common issue 3] | [Cause] | [Solution] |

---

## Module Project (Required)

**Requirements**:
[Clear, testable specifications for the project]

1. [Requirement 1: e.g., "Create a ROS 2 package with at least 2 nodes"]
2. [Requirement 2: e.g., "Implement bidirectional communication using topics"]
3. [Requirement 3: e.g., "Add parameter configuration for message rate"]
4. [Minimum 5 requirements]

**Deliverables**:
- [What learners must submit/demonstrate]
- [Example: "Source code pushed to GitHub repository"]
- [Example: "2-minute video showing robot completing task"]
- [Example: "README with setup and execution instructions"]

**Assessment Rubric**:

| Criterion | Points | Description |
|-----------|--------|-------------|
| Functionality | 40 | All requirements met, system works as specified |
| Code Quality | 30 | Clean code, proper naming, comments where needed |
| Documentation | 20 | Clear README, setup instructions, usage examples |
| Creativity | 10 | Bonus for going beyond requirements |
| **Total** | **100** | |

**Grading Notes**:
- Partial credit for partially working solutions (explain what works)
- Deductions for missing documentation (-10 points)
- Bonus (+5) for exceptional error handling or edge cases

**Estimated Time**: [X hours] (Plan for Y hours if first time learning these concepts)

---

## Quiz & Self-Assessment (Required)

**Instructions**: Test your understanding before moving to the next chapter. Answers at the end.

### Multiple Choice Questions

**Question 1**: [Question text]
a) [Option A]
b) [Option B]
c) [Option C]
d) [Option D]

**Question 2**: [Question text]
[Continue for 5-10 questions minimum]

### True/False Questions

**Question 6**: [Statement] (True/False)

### Coding Challenges

**Challenge 1**: [Brief coding task]
```
Example: "Write a ROS 2 subscriber that prints messages in uppercase"
```

**Hints**:
- [Hint 1 for challenge]
- [Hint 2 for challenge]

---

### Self-Check

Can you answer these without looking back?

- [ ] Explain [concept 1] in your own words
- [ ] Implement [skill 1] without referencing the example
- [ ] Identify when to use [approach A] vs [approach B]
- [ ] Debug a [common error] using ROS 2 tools

**If you checked all boxes**: You're ready for the next chapter! ✅
**If not**: Review the sections you're uncertain about. It's worth the time to solidify understanding.

---

## Further Reading (Optional)

### Official Documentation
- [ROS 2 Documentation - [Specific Page]](URL)
- [Library X API Reference](URL)

### Academic Papers
- [Author et al., "Paper Title", Conference/Journal, Year] - [Brief relevance note]

### Video Tutorials
- [Tutorial Title by Author] (Duration) - [What it covers]

### Community Resources
- [ROS Discourse Thread on [Topic]](URL)
- [GitHub Repository: [Relevant Project]](URL)

---

## Answers to Quiz

**Question 1**: [Correct answer letter]
**Explanation**: [Why this is correct, 1-2 sentences]

**Question 2**: [Correct answer]
**Explanation**: [...]

[Continue for all quiz questions]

---

## Metadata (Frontmatter - for Docusaurus)

```yaml
---
id: [section-id]
title: "[Chapter Title]"
sidebar_label: "[Short Title]"
sidebar_position: [number in module]
tags:
  - [tag1]
  - [tag2]
  - [module-name]
---
```

---

**Template Version**: 1.0.0
**Last Updated**: 2025-12-07
**Validation Status**: All sections required unless marked (Optional)
