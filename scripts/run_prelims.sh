#!/usr/bin/env bash

# pip install prelims-cli
cd ..
prelims-cli --config-dir ./scripts/config --config-name myconfig hydra.run.dir=. hydra.output_subdir=null hydra/job_logging=disabled hydra/hydra_logging=disabled
