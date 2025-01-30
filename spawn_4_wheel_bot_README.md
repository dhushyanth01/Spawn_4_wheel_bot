
# **spawn_4_wheel_bot**

This ROS 2 package simulates a 4-wheel robot in RViz, with a configuration that shows the robot's model, TF frames, and other necessary tools. It utilizes **ROS 2 Jazzy Jalisa** and **Gazebo Harmonic** for simulation and visualization.

## **Table of Contents**

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## **Overview**

This package is designed to simulate a 4-wheel robot using a URDF model in RViz. The configuration includes TF frames, robot visualization, and other essential tools for simulation and testing.

---

## **Prerequisites**

To run this project, you will need to have the following installed:

- **ROS 2 Jazzy Jalisa**
- **Gazebo Harmonic**
- **Python 3.x** (for ROS 2 Python-based nodes)
- **Ubuntu 24.01 Noble** (or any compatible Linux OS)

---

## **Installation**

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/spawn_4_wheel_bot.git
    cd spawn_4_wheel_bot
    ```

2. **Install dependencies**:
    ```bash
    sudo apt update
    sudo apt install ros-<ros2-distro>-<package-name>
    ```

3. **Build the workspace**:
    ```bash
    colcon build
    ```

4. **Source the workspace**:
    ```bash
    source install/setup.bash
    ```

---

## **Project Structure**

Here’s the directory structure of the project:

```
spawn_4_wheel_bot/
├── launch/
│   └── robot_launch.py       # Launch file for starting the robot in RViz
├── urdf/
│   └── robot_model.urdf      # URDF file describing the robot
├── rviz/
│   └── robot_config.rviz     # RViz configuration file for visualizing the robot
├── meshy/
│   └── robot_mesh.stl        # Mesh file used in the URDF
├── config/
│   └── robot_params.yaml     # Configuration parameters for the robot
├── CMakeLists.txt            # CMake build script for the project
├── package.xml               # ROS 2 package metadata
└── LICENSE                   # License file for the project
```

---

## **Usage**

1. **Launch the project**:
    - To start the robot in RViz, use the following command:
    ```bash
    ros2 launch spawn_4_wheel_bot robot_launch.py
    ```

---

## **Contributing**

If you'd like to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Make your changes and test them.
4. Create a pull request to the `main` branch.

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Acknowledgements**

- ROS 2 Community
- [Any other people or resources you want to mention]
