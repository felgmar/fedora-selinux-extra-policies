# Fedora SELinux Extra Policies

This package adds a set of SELinux allow rules for Fedora systems that otherwise hit unexpected access denials when running certain Snap, systemd, or virtualization-related workloads.

It is intended to fix real-world SELinux AVC denials without replacing the system policy entirely. In simple terms, it helps Fedora allow the specific file, directory, and filesystem access that certain workloads need to function correctly.

## What it does

This package is meant for systems that are running with SELinux in enforcing mode and encounter blocking errors such as:

- Snap and snapd access problems
- tmpfs and mount-related denials
- temporary system sleep/resume file access issues
- virtualization helper access to FUSE-backed filesystems

The result is that the affected software can work normally instead of being stopped by SELinux policy restrictions.

## What it is

This is a Fedora RPM package that installs a small group of custom SELinux policy modules to address known compatibility issues. It is specifically useful for users who want a practical fix for SELinux rule denials without building a custom policy from scratch.

## Download and install

Download the RPM from the repository Releases page and install it on your Fedora system:

```bash
rpm -i fedora-selinux-extra-policies-<version>.rpm
```

Once installed, the package applies the required SELinux rules automatically.

## Notes

This package is focused and targeted. It is not a general-purpose SELinux policy replacement, and it should be used only for the specific scenarios it is designed to address.
