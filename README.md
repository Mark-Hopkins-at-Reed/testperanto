<div align="center">
    <br>
    <h1>testperanto</h1>
    <img alt="screenshot" src="images/screenshot.jpeg">
    <p>
    an apache 2.0 python package for artificial language generation
    </p> 
    <hr/>
</div>
<p align="center">
    <a href="https://github.com/Mark-Hopkins-at-Williams/testperanto/blob/main/LICENSE.md">
        <img alt="License" src="https://img.shields.io/badge/license-apache2.0-blue">
    </a>
    <br/>
</p>

`testperanto` is designed to facilitate the generation of "linguistically realistic"
artificial languages. Among its intended uses:
- to investigate the inductive biases of neural models for specific linguistic typologies
- to provide realistic proxy data for developing models for low-resource languages


### getting started

#### installation (with anaconda, from testperanto root directory)

    conda create -n tpo python=3.8
    conda activate tpo
    pip install -e .

#### installation (with venv, from testperanto root directory)

    python3 -m venv tpo
    source tpo/bin/activate
    pip install -e .
    
#### running the unit tests (from testperanto root directory)

    python -m unittest

#### generating sentences from an example JSON config cascade (from testperanto root directory)

    python scripts/generate.py -c examples/svo/amr.json examples/svo/middleman.json examples/svo/english.json --sents -n 5

#### generating a parallel corpus from an example YAML config (from testperanto root directory)

    python scripts/parallel_gen.py -c experiments/eng-ger-1.yaml -o eng-ger -n 5

This will generate files `eng-ger.0` (English renderings of the sentences) and `eng-ger.1` (German rendering of the sentences).

### tutorials

`testperanto` comes with several tutorials to help learn how the
package can be used. These tutorials take the form of Jupyter Notebooks
and are located in the `/tutorials` subdirectory.



