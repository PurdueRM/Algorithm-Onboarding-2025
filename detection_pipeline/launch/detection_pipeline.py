from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Armor detector node - subscribes to camera/image_raw and processes frames
        Node(
            package='detection_pipeline',
            executable='armor_detector_node',
            name='armor_detector',
            output='screen',
            emulate_tty=True,
        ),

        # Camera publisher node - publishes video frames to camera/image_raw topic
        Node(
            package='detection_pipeline',
            executable='camera_publisher_node',
            name='camera_publisher',
            output='screen',
            emulate_tty=True,
        ),
    ])
