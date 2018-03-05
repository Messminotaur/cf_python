#!/bin/bash
mkdir vendor
pip download -d vendor -r requirements.txt --no-binary :all:
