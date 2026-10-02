Name:           fedora-selinux-extra-policies
Version:        1.0
Release:        1%{?dist}
Summary:        Custom SELinux policies to fix hardware and software issues.
License:        Public Domain
BuildArch:      noarch

Source0:        %{name}-%{version}.tar.gz

Requires:       policycoreutils
Requires:       selinux-policy-base

%description
A collection of custom local SELinux policy modules (.pp) for system fixes.

%prep
%autosetup -c

%build
# Policies are pre-compiled .pp files

%install
mkdir -p %{buildroot}/usr/share/selinux/packages
cp -p policies/*.pp %{buildroot}/usr/share/selinux/packages/

%preun
# Remove modules only on complete uninstallation ($1 == 0)
if [ $1 -eq 0 ]; then
    for pp in /usr/share/selinux/packages/*.pp; do
        if [ -f "$pp" ]; then
            modname=$(basename "$pp" .pp)
            semodule -r "$modname" || true
        fi
    done
fi

%posttrans
# Automatically install/update modules at the end of transaction
for pp in /usr/share/selinux/packages/*.pp; do
    [ -f "$pp" ] && semodule -i "$pp"
done

%files
/usr/share/selinux/packages/*.pp
