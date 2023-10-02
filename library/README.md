### GPX-GPX Python code

Ocassionally some gpx files are corrupted and they fail to load in handheld devices. 

This utility in Python will clean up the gpx file so that it confirms to GPX XML Schema.

See [GPX 1.1 Schema Documentation](https://www.topografix.com/GPX/1/1/).

For example, you have a `hiking.gpx` file you want to clean up:
```
$python3 gpx2gpx.py hiking
```
Use these codes on your own risks. 