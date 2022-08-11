from typing import Dict, Tuple
from pathlib import Path


class Plugin:
    def fatman_job_types(self, docker_registry_prefix: str) -> Dict[str, Tuple[str, Path]]:
        """
        Job types supported by this plugin
        :param docker_registry_prefix: prefix for the image names (docker registry + namespace)
        :return dict of job name -> (base image name, dockerfile template path)
        """
        return {
            'rust': (
                f'{docker_registry_prefix}/rust:1.0.0', 
                self.plugin_dir / 'fatman-template.Dockerfile',
            ),
        }