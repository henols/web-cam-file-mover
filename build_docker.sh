#!/bin/bash
docker build -t henols/copy:latest -t henols/copy:1.1 .
docker push -a henols/copy