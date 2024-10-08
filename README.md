# pixi_rocker



## Continuous Integration Status

[![Ci](https://github.com/blooop/pixi_rocker/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/blooop/pixi_rocker/actions/workflows/ci.yml?query=branch%3Amain)
[![Codecov](https://codecov.io/gh/blooop/pixi_rocker/branch/main/graph/badge.svg?token=Y212GW1PG6)](https://codecov.io/gh/blooop/pixi_rocker)
[![GitHub issues](https://img.shields.io/github/issues/blooop/pixi_rocker.svg)](https://GitHub.com/blooop/pixi_rocker/issues/)
[![GitHub pull-requests merged](https://badgen.net/github/merged-prs/blooop/pixi_rocker)](https://github.com/blooop/pixi_rocker/pulls?q=is%3Amerged)
[![GitHub release](https://img.shields.io/github/release/blooop/pixi_rocker.svg)](https://GitHub.com/blooop/pixi_rocker/releases/)
[![License](https://img.shields.io/github/license/blooop/pixi_rocker)](https://opensource.org/license/mit/)
[![Python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/downloads/)
[![Pixi Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/prefix-dev/pixi/main/assets/badge/v0.json)](https://pixi.sh)

## Intro

This is a [rocker](https://github.com/osrf/rocker) extension for adding [pixi](https://pixi.sh) to an existing docker image. Look at the rocker GitHub page for more context of how rocker and rocker extensions work, but in a nutshell rocker lets you add custom capabilities to existing docker containers. Rocker extensions

[Pixi](https://github.com/prefix-dev/pixi) is a cross-platform package manager based on the conda ecosystem.  It provides a simple and performant way of reproducing a development environment and running user defined tasks and workflows.  It is more lightweight than docker, but does not provide the same level of isolation or generality. 

### But Why??

The most common question I get is is why would you need to use pixi in docker as pixi is already taking care of your environment for you.  Unfortunately there are some packages/configuration that pixi is not able to handle yet and so one way of handling that is managing those dependencies/configuration in docker and leave the the rest up to pixi. 

Another benefit of pixi in docker is that you are more isolated from your host machine and have more flexibility to make changes without worrying about conflicting with other projects. 

If you use vscode to attach to your development container it makes it easier to set up specific extensions for each project that don't need to be installed globally. 

## Installation

```
pip install pixi-rocker
```

## Usage

To install pixi in an image use the --pixi flag

```
#add pixi to the ubuntu:22.04 image
rocker --pixi ubuntu:22.04

# add pixi to the nvidia/cuda image
rocker --pixi nvidia/cuda
```
