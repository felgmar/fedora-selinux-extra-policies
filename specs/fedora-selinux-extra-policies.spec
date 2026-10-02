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
A collection of custom SELinux policies to fix hardware and software issues.

%prep
%autosetup -c

%build
# Policies are pre-compiled .pp files

%install
mkdir -p %{buildroot}/usr/local/share/fedora-selinux-extra-policies
cp -p policies/*.pp %{buildroot}/usr/local/share/fedora-selinux-extra-policies

%preun
# Remove modules only on complete uninstallation ($1 == 0)
if [ $1 -eq 0 ]
then
    for pp in /usr/local/share/fedora-selinux-extra-policies/*.pp
    do
        if [ -f "$pp" ]
        then
            modname=$(basename "$pp" .pp)
            semodule -r "$modname" || true
        fi
    done
fi

%posttrans
# Automatically install/update modules at the end of transaction
for pp in /usr/local/share/fedora-selinux-extra-policies/*.pp
do
    [ -f "$pp" ] && semodule -i "$pp" && echo "[+] Installed policy: $(basename "$pp")"
done

%files
/usr/local/share/fedora-selinux-extra-policies/*.pp
