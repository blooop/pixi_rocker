# pixi_rocker



## Continuous Integration Status

[![Ci](https://github.com/blooop/pixi_rocker/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/blooop/pixi_rocker/actions/workflows/ci.yml?query=branch%3Amain)
[![Codecov](https://codecov.io/gh/blooop/pixi_rocker/branch/main/graph/badge.svg?token=Y212GW1PG6)](https://codecov.io/gh/blooop/pixi_rocker)
[![GitHub issues](https://img.shields.io/github/issues/blooop/pixi_rocker.svg)](https://GitHub.com/blooop/pixi_rocker/issues/)
[![GitHub pull-requests merged](https://badgen.net/github/merged-prs/blooop/pixi_rocker)](https://github.com/blooop/pixi_rocker/pulls?q=is%3Amerged)
[![GitHub release](https://img.shields.io/github/release/blooop/pixi_rocker.svg)](https://GitHub.com/blooop/pixi_rocker/releases/)
[![License](https://img.shields.io/github/license/blooop/pixi_rocker
)](https://opensource.org/license/mit/)
[![Python](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)](https://www.python.org/downloads/)
[![Pixi Badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/prefix-dev/pixi/main/assets/badge/v0.json)](https://pixi.sh)

## Intro

This is a [rocker](https://github.com/tfoote/rocker) extension for adding [pixi](https://pixi.sh) to a docker container

## Installation

```
pip install pixi-rocker
```

## Usage

To install pixi in a container use the --pixi flag

```
rocker --pixi ubuntu:latest
```
