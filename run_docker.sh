#!/bin/bash
docker run -v '/home/henrik/dev/henrik/ws/web cam file mover/test:/path' -e ROOT_DIR='/path/cam' -e DEST_DIR='/path/X-tmp' henols/copy:latest
