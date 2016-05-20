Name:           puppet-timezone
Version:        XXX
Release:        XXX
Summary:        Manage timezone settings via Puppet.
License:        Apache License, Version 2.0

URL:            https://github.com/saz/puppet-timezone

Source0:        https://github.com/saz/puppet-timezone/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
UNKNOWN

%prep
%setup -q -n %{name}-%{version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/timezone/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/timezone/



%files
%{_datadir}/openstack-puppet/modules/timezone/


%changelog

