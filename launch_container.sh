#!/bin/bash
docker run -v $(pwd):/shared -w /shared -ti dolfinx/dolfinx:v0.6.0-r1
