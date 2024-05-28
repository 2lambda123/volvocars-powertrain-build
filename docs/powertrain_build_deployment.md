# powertrain_build Deployment

[TOC]

<!--:powertrain_build:-->

## Repositories

### powertrain_build Repository

The powertrain_build git repository can be found
[here](https://opendev.org/volvocars/powertrain-build).
The powertrain_build LTS artifactory repository can be found
[here (PLACEHOLDER)](https://artifactory-link).

## Deployment

After changes (important commits, JIRA stories etc.) has been made to powertrain_build,
a new version must be deployed.

## Versioning

powertrain_build use semantic versioning, _MAJOR.MINOR.PATCH_. The version
is changed by setting an annotated tag with the version (only) at the commit
that should be the released commit.

### Development versioning

If distribution of a development version is needed, set a tag
"dev/\<explanatory-name\>". Scripts will update the patch part and add .devN,
where N is the number of commits since last proper sematic versioning tag.

## Instructions

1. Upload the change to Gerrit, have it reviewed, verified and merged.
1. Retrieve the merged commit from Gerrit and ensure it is checked out.
1. Create an annotated tag on the commit.\
`git tag -a -m'<annotation text>' <version>`
    1. For a development version:\
    `git tag -a -m'<annotation text>' dev/<explanatory>`
1. Push the tag to Gerrit:\
`git push origin <tag-name>`
1. Steps after merge can also be done by setting a tag in Gerrit GUI
1. Zuul will now:
    1. Run verification steps.
    1. Check that the version complies with PEP440 and semantic version
    1. Check that there is no package with this version on artifactory already.
    1. Upload the package to artifactory.
1. Modify the _requirements.txt_ file in any repo that requires these
updates.

## Additional notes

If powertrain_build become dependent on a new package, add the dependency to
_\<package\>/requirements.txt_, or _\<package\>/test-requirements.txt_ if the
dependency is needed only for testing the package, not for using it.

powertrain_build use [pbr](https://docs.openstack.org/pbr/latest/) to create
package meta data. Please read and use the features of pbr if updating resource
files or non-python scripts.

## Manual deployment

1. The python package _setuptools_ is required to deploy powertrain_build.
1. Follow the guidelines on the
[LTS artifactory (PLACEHOLDER)](https://artifactory-link)
page about deploying python packages.
    1. [LTS artifactory (PLACEHOLDER)](https://artifactory-link) -> Set Me Up
1. `py -3.6 setup.py sdist`, to build the package.
1. `py -3.6 setup.py sdist upload -r local`, to deploy.
    1. Deployment in this way may overwrite the package on artifactory
    if the user has enough privilege. Be careful not to upload the
    same version twice without intending to, as artifactory has no
    package upload history and an overwritten package is lost.
1. The bullet about _requirements.txt_ in [Instructions](#instructions) is valid here too.
1. The same [additional notes](#additional-notes) apply to manual deployment.
