# powertrain-build Deployment

[TOC]

<!--:powertrain-build:-->

After changes has been made to powertrain-build, a new version must be deployed.

## Repositories

The powertrain-build git repository can be found
[here](https://opendev.org/volvocars/powertrain-build).

The powertrain-build PyPi repository can be found
[here](https://pypi.org/project/powertrain-build/).

## Creating a Release

powertrain-build use [pbr](https://docs.openstack.org/pbr/latest/) to create package meta data.
Please read and use the features of pbr if updating resource files or non-python scripts.

powertrain-build use semantic versioning, _MAJOR.MINOR.PATCH_.
The version is changed by creating and pushing a signed tag with the version on the commit that should be the released commit.

Creating a tag will trigger the release pipeline which will run a Zuul jobs that uploads to PyPi.
For more information about creating releases in an opendev project,
see <https://docs.opendev.org/opendev/infra-manual/latest/drivers.html#tagging-a-release>.

### Development Releases

Currently, due to the use of pbr, it is hard to utilize the experimental pipeline to upload development releases.
Therefore, we recommend building and uploading locally,
following [this](https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives) guideline.
Note that the Zuul release job also use the _build_ and _twine_ python modules.

If you have access to the powertrain-build api token, development releases can be uploaded to the official PyPi repository.
Otherwise, we recommend creating your own TestPyPi package, see [TestPyPi](https://packaging.python.org/en/latest/guides/using-testpypi/).

If distribution of a development version is needed, `.devN` should be used as postfix,
where "N" equals the release number of the development release.
Note that pbr creates this postfix automatically.

## Additional Notes

If powertrain-build become dependent on a new package, add the dependency to _/requirements.txt_,
or _test-requirements.txt_ if the dependency is needed only for testing the package, not for using it.
