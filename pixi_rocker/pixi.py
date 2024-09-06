import grp
import os
import docker
import getpass
import pwd
import pkgutil
from pathlib import Path
from shlex import quote
import subprocess
import sys

from pathlib import Path
from collections import defaultdict
import yaml
import toml
from rocker.extensions import RockerExtension


class PixiExtension(RockerExtension):
    @staticmethod
    def get_name():
        return "pixi"

    def __init__(self):
        self._env_subs = None
        self.name = PixiExtension.get_name()

    def get_preamble(self, cliargs):
        return ""

    def get_snippet(self, cliargs):
        snippet = pkgutil.get_data("pixi_rocker", "templates/curl_snippet.Dockerfile").decode(
            "utf-8"
        )
        return snippet
    
    def get_user_snippet(self, cliargs):
        snippet = pkgutil.get_data("pixi_rocker", f"templates/{self.name}_snippet.Dockerfile").decode(
            "utf-8"
        )
        return snippet

    @staticmethod
    def register_arguments(parser, defaults={}):
        parser.add_argument(
            f"--{PixiExtension.get_name()}",
            action="store_true",
            default=defaults.get("pixi", None),
            help="add pixi dependency manager to your environment",
        )
