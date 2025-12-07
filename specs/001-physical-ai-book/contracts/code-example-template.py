"""
Code Example Template for Physical AI & Humanoid Robotics Book

VALIDATION REQUIREMENTS:
- Must include complete docstring header with all fields
- Prerequisites must be specific and actionable
- Expected output must show what learners will see
- Code must pass validation before book deployment (validation_status = "passing")
- Last validated date must be within 30 days

USAGE:
1. Copy this template to code-examples/[module]/[descriptive-name].py
2. Fill in all header fields
3. Implement the example with extensive comments
4. Test locally to ensure it runs
5. Run validation script: python scripts/validate-code-examples.py
6. Reference from chapter markdown using example_id
"""

# ==============================================================================
# HEADER METADATA (Required - Do not remove)
# ==============================================================================

"""
Code Example: [Descriptive Name of Example]

Example ID: [unique-slug-for-referencing]
    Format: [module]-[concept]-[variant]
    Examples: "ros2-publisher-basic", "isaac-object-detection-yolo"

Module: [Module Name]
    One of: "ROS 2 Fundamentals", "Simulation", "NVIDIA Isaac", "Vision-Language-Action", "Capstone"

Purpose: [One-sentence description of what this demonstrates]
    Example: "Demonstrates basic ROS 2 publisher node sending string messages to a topic at 1Hz"

Prerequisites:
    - [Prerequisite 1: Specific installation/setup requirement]
    - [Prerequisite 2: Configuration step]
    - [Prerequisite 3: Prior completed example or knowledge]

    Examples:
    - ROS 2 Humble installed (sudo apt install ros-humble-desktop)
    - ROS 2 environment sourced (source /opt/ros/humble/setup.bash)
    - Workspace created (mkdir -p ~/ros2_ws/src && cd ~/ros2_ws)
    - Basic understanding of ROS 2 nodes (see chapter X.Y)

Expected Output:
    [Describe what learners should see when running this code]
    [Include sample output text, or describe visual output for GUI/simulation examples]

    Example:
    [INFO] [minimal_publisher]: Publishing: 'Hello World: 0'
    [INFO] [minimal_publisher]: Publishing: 'Hello World: 1'
    [INFO] [minimal_publisher]: Publishing: 'Hello World: 2'
    (Messages appear every 1 second)

Validation Status: [untested | passing | failing]
    This will be updated by scripts/validate-code-examples.py
    Initial value: untested

Last Validated: [YYYY-MM-DD]
    Date when validation script last confirmed this example works
    Initial value: [Current date when creating example]

Author: [Your Name or "Book Authors"]
Version: 1.0.0
"""

# ==============================================================================
# SETUP INSTRUCTIONS (As code comments for easy copy-paste)
# ==============================================================================

# Step 1: [First setup step]
# Example: Create a ROS 2 workspace if you don't have one
#   mkdir -p ~/ros2_ws/src
#   cd ~/ros2_ws/src

# Step 2: [Second setup step]
# Example: Create a Python package for this example
#   ros2 pkg create --build-type ament_python my_package_name

# Step 3: [Configuration step if needed]
# Example: Install additional dependencies
#   pip install [dependency]

# Step 4: [How to run this specific example]
# Example: Run this node with:
#   cd ~/ros2_ws
#   colcon build --packages-select my_package_name
#   source install/setup.bash
#   ros2 run my_package_name [node_name]

# ==============================================================================
# IMPORTS
# ==============================================================================

# Standard library imports
import sys
import time

# Third-party imports
# import numpy as np
# import cv2

# ROS 2 imports (if applicable)
# import rclpy
# from rclpy.node import Node
# from std_msgs.msg import String

# ==============================================================================
# CONSTANTS AND CONFIGURATION
# ==============================================================================

# Define constants at module level with UPPER_CASE names
DEFAULT_PUBLISH_RATE = 1.0  # Hz
DEFAULT_TOPIC_NAME = "/example_topic"

# ==============================================================================
# MAIN CODE
# ==============================================================================

class ExampleClass:
    """
    [Brief class description]

    This class demonstrates [what concept/pattern].

    Attributes:
        [attribute1] ([type]): [Description]
        [attribute2] ([type]): [Description]

    Methods:
        [method1]: [Brief description]
        [method2]: [Brief description]
    """

    def __init__(self, param1, param2):
        """
        Initialize the [ExampleClass].

        Args:
            param1 ([type]): [Description of parameter]
            param2 ([type]): [Description of parameter]
        """
        # Explain what this initialization does
        self.param1 = param1
        self.param2 = param2

        # More initialization with comments explaining WHY, not just WHAT
        # Example: "Create timer to publish at regular intervals"
        # self.timer = ...

    def example_method(self):
        """
        [Method description - what it does and why]

        Returns:
            [type]: [Description of return value]

        Raises:
            [ExceptionType]: [When this exception occurs]
        """
        # Implementation with inline comments for key lines
        pass


def main(args=None):
    """
    Main entry point for the example.

    This function demonstrates the complete workflow of [what this example shows].

    Args:
        args ([type], optional): Command-line arguments. Defaults to None.

    Steps:
        1. [High-level step 1]
        2. [High-level step 2]
        3. [High-level step 3]
    """
    print("=" * 60)
    print("Example: [Example Name]")
    print("=" * 60)

    # Step 1: [Initialization]
    # Explain what's being set up and why
    # example_obj = ExampleClass(param1, param2)

    # Step 2: [Main logic]
    # Explain the core functionality
    # result = example_obj.example_method()

    # Step 3: [Output/Verification]
    # Show results or verify success
    # print(f"Result: {result}")

    print("\n" + "=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


# ==============================================================================
# ENTRY POINT
# ==============================================================================

if __name__ == "__main__":
    """
    Direct execution entry point.

    When run directly (python example.py), this block executes main().
    When imported as a module, this block is skipped.
    """
    try:
        main()
    except KeyboardInterrupt:
        print("\nExample interrupted by user (Ctrl+C)")
        sys.exit(0)
    except Exception as e:
        print(f"\nError occurred: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

# ==============================================================================
# ADDITIONAL NOTES FOR LEARNERS (Optional)
# ==============================================================================

"""
LEARNING NOTES:
--------------
[Key concepts demonstrated in this example]
- [Concept 1]: [Brief explanation]
- [Concept 2]: [Brief explanation]

COMMON MODIFICATIONS:
-------------------
To adapt this example for your use case:
1. [Modification suggestion 1]
2. [Modification suggestion 2]

TROUBLESHOOTING:
---------------
Issue: [Common error message]
Solution: [How to fix]

Issue: [Another common error]
Solution: [How to fix]

NEXT STEPS:
----------
After understanding this example:
1. Try [suggested exercise 1]
2. Experiment with [suggested modification]
3. Combine with [related example ID] to build [more complex application]
"""
