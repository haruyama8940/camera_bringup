from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    packages_name = "camera_tools"
    xacro_file_name = "orne_box.urdf.xacro"
    config_file = "camera_bringup.yaml"

    camera_config_file = PathJoinSubstitution(
        [FindPackageShare(packages_name), "config", config_file]
    )

    v4ls2_camera_node = Node(
        package="v4l2_camera",
        executable="v4l2_camera_node",
        output="screen",
        parameters=[{
                    "video_device": "/dev/video0",
                    "output_encoding": "rgb8",
                    "camera_frame_id": "camera",
                    "pixel_format":  "YUYV",
                    "image_size": [640,480],
                    "time_per_frame": [1,30]
                    }]
    )
        # parameters=[{"robot_params": camera_config_file}]

    nodes = [
        v4ls2_camera_node
    ]
    return LaunchDescription(nodes)