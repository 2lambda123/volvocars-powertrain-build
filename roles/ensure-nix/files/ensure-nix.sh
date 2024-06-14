#!/usr/bin/env sh

set -eu

NIX_INSTALLER="/usr/bin/nix-installer"
NIX_INSTALLER_URL="https://github.com/DeterminateSystems/nix-installer/releases/download/v0.17.1/nix-installer-x86_64-linux"
NIX_INSTALLER_CHECKSUM="dc91db36f96b15e8651383dbbfe0d6917e22dca199a046c7e25aad38efeccc80"
NIX_INSTALLER_LOCKFILE="/tmp/nix-installer.lock"
NIX_INSTALLER_INSTALL_LOCKFILE="/tmp/nix-installer-install.lock"

LOCK_TIMEOUT=30

releaseLock() {
  lockFile="$1"; shift
  echo "Releasing lock: $lockFile"
  rm -rf "$lockFile"
}

acquireLock() {
  lockFile="$1"; shift
  start="$(date +%s)"
  echo "Acquiring lock: $lockFile"
  while true; do
    now="$(date +%s)"
    if [ $(( now - start )) -gt "$LOCK_TIMEOUT" ]; then
      return 1
    fi

    if mkdir "$lockFile"; then
      echo "Acquired lock: $lockFile"
      return 0
    fi
    echo "Waiting for lock"
    sleep 1
  done
}

checkForNixInstaller() {
  command -v "$NIX_INSTALLER"
}

testNixInstallation() {
  "$NIX_INSTALLER" self-test
}

getNixInstaller() {
  echo "Fetching nix installer"
  NIX_INSTALLER_WORKDIR="$(mktemp -d)"

  curl \
    -L "$NIX_INSTALLER_URL" \
    -o "$NIX_INSTALLER_WORKDIR/nix-installer"
  echo "$NIX_INSTALLER_CHECKSUM $NIX_INSTALLER_WORKDIR/nix-installer" | sha256sum -c
  chmod +x "$NIX_INSTALLER_WORKDIR/nix-installer"

  mv "$NIX_INSTALLER_WORKDIR/nix-installer" "$NIX_INSTALLER"
  rm -rf "$NIX_INSTALLER_WORKDIR"
}

installNix() {
  echo "Installing nix"
  "$NIX_INSTALLER" \
    install linux \
    --extra-conf "experimental-features = nix-command flakes" \
    --no-confirm \
    --force
}

# Only fetch the installer if it is not already installed.
if acquireLock "$NIX_INSTALLER_LOCKFILE"; then
  trap 'releaseLock "$NIX_INSTALLER_LOCKFILE"; exit' EXIT
  if ! checkForNixInstaller; then
    getNixInstaller
  fi

  if ! releaseLock "$NIX_INSTALLER_LOCKFILE"; then
    echo "Failed to release lock: $NIX_INSTALLER_LOCKFILE"
    exit 1
  fi
  trap - EXIT INT
else
  echo "Timeout waiting for lockfile: $NIX_INSTALLER_LOCKFILE"
  exit 1
fi

# Only install nix if it is not already installed.
if acquireLock "$NIX_INSTALLER_INSTALL_LOCKFILE"; then
  trap 'releaseLock "$NIX_INSTALLER_INSTALL_LOCKFILE"; exit' EXIT

  if ! testNixInstallation; then
    installNix
  fi

  if ! releaseLock "$NIX_INSTALLER_INSTALL_LOCKFILE"; then
    echo "Failed to release lock: $NIX_INSTALLER_INSTALL_LOCKFILE"
    exit 1
  fi
  trap - EXIT INT
else
  echo "Timeout waiting for lockfile: $NIX_INSTALLER_INSTALL_LOCKFILE"
  exit 1
fi

echo "Installation successful."
