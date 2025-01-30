import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    
    # Locate the package share directory
    package_share = FindPackageShare('four_wheel_bot')
    rviz_default_config = PathJoinSubstitution([package_share, 'rviz', 'check.rviz'])

    # ennabling the joint state publisher GUI
    joint_gui_arg = DeclareLaunchArgument(
        name='enable_gui', 
        default_value='true', 
        choices=['true', 'false'],
        description='Enable or disable the joint_state_publisher GUI'
    )
    
    # Rviz Config file Path
    rviz_config_arg = DeclareLaunchArgument(
        name='rviz_config_file',
        default_value=rviz_default_config,
        description='Full path to the RViz configuration file'
    )
    
    # URDF Model FIle
    urdf_model_arg = DeclareLaunchArgument(
        name='robot_model', 
        default_value='zayn_bot.urdf',  # <-------------- Replace with Your URDF File
        description='URDF model file to be loaded'
    )

    # Include the built-in URDF display launch file
    urdf_display_launch = IncludeLaunchDescription(
        PathJoinSubstitution([FindPackageShare('urdf_launch'), 'launch', 'display.launch.py']),
        launch_arguments={
            'urdf_package': 'four_wheel_bot',
            'urdf_package_path': PathJoinSubstitution(['urdf', LaunchConfiguration('robot_model')]),
            'rviz_config': LaunchConfiguration('rviz_config_file'),
            'jsp_gui': LaunchConfiguration('enable_gui')
        }.items()
    )

    # Create the launch description object and add all actions
    launch_desc = LaunchDescription()
    launch_desc.add_action(joint_gui_arg)
    launch_desc.add_action(rviz_config_arg)
    launch_desc.add_action(urdf_model_arg)
    launch_desc.add_action(urdf_display_launch)

    return launch_desc
