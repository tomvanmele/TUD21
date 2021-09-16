# TU Delft 21 - COMPAS intro

## Update `earthy` environment

```bash
conda activate earthy
conda install compas compas_cgal compas_view2 --yes
```

## Install for Rhino

```bash
python -m compas_rhino.install -v 7.0
```

## Install for Blender

For Blender 2.83 LTS you need an environment with Python 3.7
For Blender 2.93 LTS you need an environment with Python 3.9
If the `earthy` environment is not one of those, consider making a new environment.

```bash
python -m compas_blender.install /Applications/Blender.app/Contents/Resources/2.83
```

For more info aboout Blender, see the COMPAS docs
<https://compas.dev/compas/dev/gettingstarted/blender.html>
