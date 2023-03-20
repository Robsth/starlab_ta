#!/bin/bash

black app && \
isort app && \
prospector app
