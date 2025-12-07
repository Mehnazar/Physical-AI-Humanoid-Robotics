#!/usr/bin/env python3
"""
Code Example: Basic ROS 2 Node with Timer

Example ID: ros2-basic-node-01
Module: ROS 2 Fundamentals
Purpose: Demonstrates basic ROS 2 node creation with periodic timer callback

Prerequisites:
    - ROS 2 Humble installed (sudo apt install ros-humble-desktop)
    - ROS 2 environment sourced (source /opt/ros/humble/setup.bash)
    - Python 3.10+ installed
    - Basic understanding of Python classes

Expected Output:
    [INFO] [hello_node]: Hello Node has been started!
    [INFO] [hello_node]: Hello, ROS 2! (count: 1)
    [INFO] [hello_node]: Hello, ROS 2! (count: 2)
    [INFO] [hello_node]: Hello, ROS 2! (count: 3)
    (Messages appear every 1 second until Ctrl+C)

Validation Status: passing
Last Validated: 2025-12-07
Author: Physical AI Book Authors
Version: 1.0.0
"""

# ==============================================================================
# SETUP INSTRUCTIONS
# ==============================================================================

# Step 1: Create a ROS 2 workspace if you don't have one
#   mkdir -p ~/ros2_ws/src
#   cd ~/ros2_ws/src

# Step 2: Create a Python package for this example
#   ros2 pkg create --build-type ament_python my_robot_package

# Step 3: Copy this file to the package
#   cp 01_basic_node.py ~/ros2_ws/src/my_robot_package/my_robot_package/

# Step 4: Add entry point to setup.py
#   Edit ~/ros2_ws/src/my_robot_package/setup.py:
#   entry_points={
#       'console_scripts': [
#           'hello_node = my_robot_package.01_basic_node:main',
#       ],
#   },

# Step 5: Build the package
#   cd ~/ros2_ws
#   colcon build --packages-select my_robot_package
#   source install/setup.bash

# Step 6: Run this node with:
#   ros2 run my_robot_package hello_node

# ==============================================================================
# IMPORTS
# ==============================================================================

import rclpy
from rclpy.node import Node

# ==============================================================================
# NODE CLASS
# ==============================================================================

class HelloNode(Node):
    """
    Basic ROS 2 node that prints messages periodically.

    This node demonstrates fundamental ROS 2 concepts:
    - Node creation and initialization
    - Timer creation for periodic callbacks
    - Logging with different severity levels

    Attributes:
        timer (Timer): Timer object that triggers callbacks every 1.0 seconds
        counter (int): Counter incremented with each timer callback
    """

    def __init__(self):
        """
        Initialize the HelloNode.

        This constructor:
        1. Calls parent Node.__init__() with node name 'hello_node'
        2. Logs startup message
        3. Creates timer that fires every 1.0 second
        4. Initializes message counter
        """
        # Initialize parent Node class with name 'hello_node'
        super().__init__('hello_node')

        # Log informational message when node starts
        self.get_logger().info('Hello Node has been started!')

        # Create timer that calls timer_callback every 1.0 second
        # Timer period is in seconds (1.0 = 1 Hz frequency)
        self.timer = self.create_timer(1.0, self.timer_callback)

        # Initialize counter to track number of messages sent
        self.counter = 0

    def timer_callback(self):
        """
        Timer callback function called every 1.0 seconds.

        This method:
        - Increments the message counter
        - Logs "Hello, ROS 2!" message with current count
        - Demonstrates basic logging functionality
        """
        # Increment counter each time callback is triggered
        self.counter += 1

        # Log message with current count
        # f-string formatting allows embedding variables in strings
        self.get_logger().info(f'Hello, ROS 2! (count: {self.counter})')

# ==============================================================================
# MAIN ENTRY POINT
# ==============================================================================

def main(args=None):
    """
    Main entry point for the node.

    This function handles the complete lifecycle:
    1. Initialize rclpy (ROS 2 Python client library)
    2. Create node instance
    3. Spin node to process callbacks (blocks until Ctrl+C)
    4. Clean up resources on shutdown

    Args:
        args (list, optional): Command-line arguments. Defaults to None.
    """
    # Step 1: Initialize ROS 2 Python client library
    # MUST be called before creating any nodes
    rclpy.init(args=args)

    # Step 2: Create instance of HelloNode
    node = HelloNode()

    # Step 3: Spin (process callbacks) until interrupted
    # This blocks and keeps the node running
    # Press Ctrl+C to stop
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        node.get_logger().info('Node stopped by user (Ctrl+C)')

    # Step 4: Clean up
    # Destroy node and shutdown ROS 2
    node.destroy_node()
    rclpy.shutdown()

# ==============================================================================
# DIRECT EXECUTION
# ==============================================================================

if __name__ == '__main__':
    """
    Direct execution entry point.

    When run directly (python3 01_basic_node.py), this block executes main().
    When imported as a module, this block is skipped.
    """
    main()

# ==============================================================================
# LEARNING NOTES
# ==============================================================================

"""
KEY CONCEPTS DEMONSTRATED:
---------------------------
1. Node Creation: Inherit from rclpy.node.Node base class
2. Timer Callbacks: Use create_timer() for periodic execution
3. Logging: get_logger().info() for runtime messages
4. ROS 2 Lifecycle: init() → spin() → destroy_node() → shutdown()

COMMON MODIFICATIONS:
---------------------
To adapt this example for your use case:
1. Change timer period: Modify 1.0 in create_timer(1.0, ...) to your desired frequency
2. Add parameters: Use declare_parameter() and get_parameter() for runtime configuration
3. Change log level: Use debug(), warn(), error() instead of info() for different severities
4. Add cleanup: Override destroy_node() to clean up custom resources

TROUBLESHOOTING:
----------------
Issue: "ros2: command not found"
Solution: Source ROS 2 setup: source /opt/ros/humble/setup.bash

Issue: Timer callback not firing
Solution: Ensure rclpy.spin() is called in main()

Issue: Node name conflict
Solution: Change node name in super().__init__('hello_node') to unique name

NEXT STEPS:
-----------
After understanding this example:
1. Try changing the timer frequency (e.g., 0.5 for 2 Hz)
2. Add a parameter for max_count and shutdown after N messages
3. Combine with example 02_pubsub.py to publish data instead of logging
"""
