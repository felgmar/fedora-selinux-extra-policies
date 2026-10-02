#!/bin/bash
set -e

# Require an exact Git tag on the current commit
TAG="${GITHUB_REF_NAME:-$(git describe --tags --exact-match HEAD 2>/dev/null || true)}"

if [ -z "$TAG" ]
then
    echo "[!] Error: Current commit is not tagged. Aborting build."
    exit 1
fi

VERSION="${TAG#v}"
echo "[-] Building version from tag: $VERSION"

# Update version in spec file
sed -i "s/^Version:.*/Version: $VERSION/" specs/fedora-selinux-extra-policies.spec

# Setup RPM build tree
mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

# Create tarball and build
TARBALL_NAME="fedora-selinux-extra-policies-$VERSION.tar.gz"
tar -czvf "$TARBALL_NAME" policies/
mv "$TARBALL_NAME" ~/rpmbuild/SOURCES/
cp specs/fedora-selinux-extra-policies.spec ~/rpmbuild/SPECS/

rpmbuild -bb ~/rpmbuild/SPECS/fedora-selinux-extra-policies.spec
